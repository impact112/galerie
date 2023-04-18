from routes.common import *
from auth import *
from forms import Form, Field
import forms.validators as validators


class CommentForm(Form):

    id = 'comment_form'

    parent_id = Field(
        name='parent_id'
    )

    text_body = Field(
        name='text_body',
        validators=[validators.NotEmpty()]
    )


async def addcomment_route(post_id: int):

    form = CommentForm()

    if not g.current_account:
        return jsonify({'errors': 'Not logged in.'}), 400

    post = dbsession.query(Post).filter(Post.id == post_id).first()

    if await form.load(request):

        parent_comment = dbsession.query(Comment).filter(Comment.id == form.parent_id.data).first()

        comment = Comment(
            content=form.text_body.data
        )

        dbsession.add(comment)

        if parent_comment:
            parent_comment.replies.append(comment)
        else:
            post.replies.append(comment)
        
        comment.uploader = g.current_account

        dbsession.commit()
        dbsession.refresh(comment)

        return jsonify({'comment_id': comment.id})

    else:
        return jsonify({'errors': form.errors}), 400
