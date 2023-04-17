
from routes.common import *
from database import *
from forms import Form, Field, validators


def get_posts_by_tags(tags: list, neg_tags: list = []):

    q = dbsession.query(Post).join(Post.tags)

    if tags:
        q = q.filter(Tag.id.in_([tag.id for tag in tags]))

    if neg_tags:
        q = q.filter(~Tag.id.in_([tag.id for tag in neg_tags]))

    q = q.group_by(Post.id).having(func.count(Tag.id) == len(tags))

    return q


class SearchForm(Form):

    tag_list = Field(
        name='tag_list',
        placeholders='Search for multiple tags',
    )

    def get_posts(self):
        tags: list = []
        neg_tags: list = []
        for tag_name in self.tag_list.data.split():
            tag = dbsession.query(Tag).filter(Tag.name == tag_name).first()
            tags.append(tag)
        return get_posts_by_tags(tags, neg_tags)


async def search_route():
    form = SearchForm()
    if await form.load(request):
        posts = form.get_posts()
        return await render_page('index.html', posts=posts)
    else:
        return jsonify({'errors': form.errors})
