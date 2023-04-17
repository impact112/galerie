
from database.common import *
from database.entities.tag_relationship import tag_relationships
from database.entities.account import Account


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('posts.id'))

    title = Column(String(256), nullable=False)
    description = Column(Text)
    uploader_id = Column(Integer, ForeignKey('accounts.id'))
    views = Column(Integer, default=0)

    upload_ts = Column(Integer)
    edit_ts = Column(Integer)
    visibility = Column(Integer)
    # 0 = public, 1 = unlisted, 2 = requires_login, 3 = hidden

    child_posts = relationship(
        'Post'
    )

    tags = relationship(
        'Tag',
        secondary=tag_relationships,
        back_populates='posts'
    )

    mediaitems = relationship(
        'MediaItem'
    )

    uploader = relationship(
        'Account'
    )

    replies = relationship(
        'Comment'
    )
