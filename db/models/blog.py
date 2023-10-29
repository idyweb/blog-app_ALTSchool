from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from db.base_class import Base

# from db.models.user import User


class Blog(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    username = Column(String, ForeignKey("user.username"))
    author = relationship("User", backref="blogs", foreign_keys=[author_id])
    created_at = Column(DateTime, default=datetime.now)  # Use a callable function
