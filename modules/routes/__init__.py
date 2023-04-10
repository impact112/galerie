
from auth import get_account_from_session

from routes.index import index_route
from routes.login import login_route
from routes.register import register_route
from routes.logout import logout_route
from routes.post import post_route
from routes.upload import upload_route

from routes.common import *

app = Quart(
    __name__,
    template_folder='../../templates',
    static_url_path='/res',
    static_folder='../../data/res'
)

app.secret_key = 'secret'
app.add_url_rule('/', 'index_route', index_route)
app.add_url_rule('/login', 'login_route', login_route, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register_route', register_route, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout_route', logout_route)
app.add_url_rule('/post/<int:post_id>', 'post_route', post_route)
app.add_url_rule('/upload', 'upload_route', upload_route, methods=['GET', 'POST'])


@app.before_request
async def before_request():
    g.current_account = get_account_from_session()
