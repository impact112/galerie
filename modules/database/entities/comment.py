
from database.common import *


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    parent_id = Column(Integer, ForeignKey('comments.id'))
    uploader_id = Column(Integer, ForeignKey('accounts.id'))

    title = Column(String(128))
    content = Column(Text)

    upload_ts = Column(Integer)
    edit_ts = Column(Integer)
    visibility = Column(Integer)
