
from database.common import *
from database.entities.post import Post
from database.entities.tag import Tag
from database.entities.account import Account
from database.entities.session_token import SessionToken
from database.entities.media_item import MediaItem
from database.entities.comment import Comment

engine = create_engine( 'sqlite:///data/galerie.db', echo = True )
Base.metadata.create_all( engine )

Session = sessionmaker( bind = engine )
dbsession = Session()

def get_posts_by_tags( tags:list, neg_tags:list ) -> list:
    return dbsession.query( Post ).join(Post.tags).filter( Tag.name.in_(tags) ).filter( ~Tag.name.in_( neg_tags ) if neg_tags else True ).group_by( Post.id ).having( func.count(Tag.id) == len(tags) ).all()
