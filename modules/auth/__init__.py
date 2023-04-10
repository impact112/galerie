
from database import *
from routes.common import *
from argon2 import PasswordHasher
from functools import wraps
import secrets


ag2 = PasswordHasher()

def generate_token_for_account( account: Account ) -> None:
    token_data = secrets.token_urlsafe(64)
    token = SessionToken( account_id = account.id, token = token_data )
    dbsession.add( token )
    dbsession.commit()
    session['secret'] = token_data

def get_account_from_session() -> Account:
    if 'secret' not in session:
        return 0
    return dbsession.query( Account ).join( SessionToken, SessionToken.account_id == Account.id ).filter( SessionToken.token == session['secret'] ).first()

def clear_session() -> None:
    if not get_account_from_session():
        return
    token = dbsession.query( SessionToken ).filter( SessionToken.token == session['secret'] ).first()
    dbsession.delete( token )
    dbsession.commit()
    session.clear()

def auth( func ):
    @wraps( func )
    async def decorated( *args, **kwargs ):
        current_account: Account = get_account_from_session()
        return await func(
            current_account = current_account,
            *args, **kwargs
        )
    return decorated
