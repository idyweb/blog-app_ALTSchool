from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from db.base_class import Base


class ExpiredToken(Base):
    id = Column(Integer, primary_key=True)
    access_token = Column(String, nullable=False)
