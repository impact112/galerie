
from database.common import *
from pathlib import Path

class MediaItem( Base ):
    __tablename__ = 'mediaitems'
    id = Column( Integer, primary_key = True )
    filename = Column( String(256), unique = True )
    mediatype = Column( String(256), index = True )
    parent_post_id = Column( Integer, ForeignKey('posts.id') )
    parent_account_id = Column( Integer, ForeignKey('accounts.id') )

    @property
    def local_path( self ) -> Path:
        return Path('data/res').joinpath( 'thumb' if self.mediatype == 'thumbnail' else 'img' ).joinpath( self.filename )
    
    @property
    def server_path( self ) -> str:
        return str( Path('/res').joinpath( 'thumb' if self.mediatype == 'thumbnail' else 'img' ).joinpath( self.filename ) )
