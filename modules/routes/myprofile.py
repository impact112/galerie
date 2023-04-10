
from routes.common import *
from routes.forms import *
from routes import app
from auth import *

@app.route( '/profile' )
async def profile_route():
    if not g.current_account:
        return redirect( url_for( 'login_route' ) )
    return str( g.current_account.username )

