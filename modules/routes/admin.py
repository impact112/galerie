
from routes.common import *
from routes import app
from auth import *

@app.route('/admin')
async def admin_index_route():
    if not g.current_account:
        return 'You must be logged in'
    
    if g.current_account.power_level != 99:
        return 'You must be admin'
    
    accounts = dbsession.query( Account ).all()
    tags = dbsession.query( Tag ).all()
    
    return await render_page(
        'admin_index.html',
        accounts = accounts,
        tags = tags
    )

@app.route('/admin/deluser')
async def delete_user_route():
    return 'a'

@app.route( '/admin/addtag', methods = [ 'POST' ] )
async def add_tag_route():
    current_account: Account = get_account_from_session()
    if not account:
        return 'You must be logged in'
        if not current_account.power_level != 99:
            return 'You must be admin'
    
    return 'Not implemented'
    
