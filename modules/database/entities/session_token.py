
from database.common import *
from database.entities.account import Account

class SessionToken(Base):
    __tablename__ = 'session_tokens'
    id = Column( Integer, primary_key = True )
    account_id = Column( Integer, ForeignKey('accounts.id') )
    
    token = Column( String(64), unique = True )
    max_age = Column( Integer )
    
    account = relationship( Account )  


