
from database.common import *


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    parent_id = Column(Integer, ForeignKey('comments.id'))
    uploader_id = Column(Integer, ForeignKey('accounts.id'))

    content = Column(Text)

    upload_ts = Column(Integer)
    edit_ts = Column(Integer)
    visibility = Column(Integer)

    parent_post = relationship(
        'Post',
        uselist=False
    )

    parent_reply = relationship(
        'Comment',
        remote_side=[id],
        back_populates='replies'
    )

    replies = relationship(
        'Comment',
        back_populates='parent_reply'
    )

    uploader = relationship(
        'Account',
        uselist=False
    )
