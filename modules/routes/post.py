
from routes.common import *
from routes import app
from database import *
from auth import *

@app.route('/post/<int:post_id>')
async def post_route( post_id:int ):
    current_account: Account = get_account_from_session()
    post = dbsession.query( Post ).filter( Post.id == post_id ).first()
    if not post:
        return '404', 404
    return await render_page( 'post.html', post = post )
