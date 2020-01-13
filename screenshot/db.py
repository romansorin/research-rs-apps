from sqlalchemy import (create_engine, Column, Enum, ForeignKey, Boolean, Integer, String)
from sqlalchemy.orm.session import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base

DB = os.path.join(os.path.dirname(__file__), 'screenshots.sqlite3')
conn_string = f'sqlite:///{DB}'
engine = create_engine(conn_string)
Base = declarative_base()


def connect():
    return sessionmaker(bind=engine)


def migrate():
    Base.metadata.create_all(engine)
    print("Migrated tables")


class Site(Base):
    __tablename__ = 'sites'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    host = Column(String, nullable=False, unique=True)


# Models
class Screenshot(Base):
    __tablename__ = 'screenshots'
    id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey(Site.id), primary_key=True,)
    path = Column(String, nullable=False, unique=True)
    type = Column(Enum, nullable=False)

session = connect()
migrate()
