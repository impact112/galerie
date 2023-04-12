
from routes.common import *
from database import *
from forms import Form, Field, validators


def get_posts_by_tags(tags: list, neg_tags: list = []):

    q = db.session.query(Post).join(Post.tags)

    if tags:
        q = q.filter(Tag.id.in_([tag.id for tag in tags]))

    if neg_tags:
        q = q.filter(~Tag.id.in_([tag.id for tag in neg_tags]))

    q = q.group_by(Post.id).having(func.count(Tag.id) == len(tags))

    return q


class SearchForm(Form):

    tag_list = Field(
        name='tags',
        placeholders='Search for multiple tags',
        validators=[validators.NotEmpty()]
    )

    def get_posts():
        pass


async def search_route():
    form = SearchForm()
    if await form.load(request):
        return jsonify(form.data)
    else:
        return jsonify({'errors': form.errors})
