
from routes.common import *
from routes import app
from database import *

@app.route('/')
async def index_route():
    posts = dbsession.query( Post ).all()
    return await render_page( 'index.html', posts = posts )
