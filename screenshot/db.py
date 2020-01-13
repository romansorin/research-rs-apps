from sqlalchemy import (create_engine, Column, Enum, ForeignKey, Boolean, Integer, String)
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship
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


def drop():
    Base.metadata.drop_all(engine)
    print("Dropped tables")

class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    host = Column(String)
    screenshot = relationship('Screenshot', backref='sites', passive_deletes=True)


# Models
class Screenshot(Base):
    __tablename__ = 'screenshots'

    id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey('sites.id', ondelete='cascade'))
    site = relationship('Site', backref='screenshots', passive_deletes=True)
    # path = Column(String)
    # type = Column(Enum)



session = connect()
drop()
migrate()
