import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ToDoTable(Base):
    __tablename__ = 'ToDoTable'

    id = sa.Column(sa.Integer, primary_key=True)
    done = sa.Column(sa.Boolean)
    text = sa.Column(sa.String)
