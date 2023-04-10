
from auth import *
from routes.common import *

app = Quart(
    __name__,
    template_folder = '../../templates',
    static_url_path = '/res',
    static_folder = '../../data/res'
)

app.secret_key = 'secret'

@app.before_request
async def before_request():
    g.current_account = get_account_from_session()

import routes.post
import routes.index
import routes.login
import routes.register
import routes.logout
