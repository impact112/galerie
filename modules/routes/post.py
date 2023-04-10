
from routes.common import *
from database import *


async def post_route(post_id: int):
    post = dbsession.query(Post).filter(Post.id == post_id).first()
    if not post:
        return '404', 404
    return await render_page('post.html', post=post)
