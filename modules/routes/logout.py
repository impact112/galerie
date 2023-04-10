
from routes.common import *
from routes import app
from auth import *

@app.route( '/logout' )
async def logout_route():
    clear_session()
    return redirect( url_for( 'index_route' ) )
