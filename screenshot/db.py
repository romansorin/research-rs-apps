from sqlalchemy import (create_engine, Column, Enum,  ForeignKey, Boolean, Integer, String)
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship, backref
import os
import enum
from sqlalchemy.ext.declarative import declarative_base

DB = os.path.join(os.path.dirname(__file__), 'screenshots.sqlite3')
conn_string = f'sqlite:///{DB}'
engine = create_engine(conn_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

def migrate():
    Base.metadata.create_all(engine)
    print("Migrated tables")


def drop():
    Base.metadata.drop_all(engine)
    print("Dropped tables")


class ScreenshotEnum(enum.Enum):
    RGB = "RGB"
    GREYSCALE = "GREYSCALE"

class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    host = Column(String)
    children = relationship('Screenshot', backref='site', cascade='all,delete')


# Models
class Screenshot(Base):
    __tablename__ = 'screenshots'

    id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey('sites.id', ondelete='CASCADE'))
    path = Column(String)
    type = Column(Enum(ScreenshotEnum))
    parent = relationship(Site, backref=backref('screenshot', cascade='all,delete', passive_deletes=True))


# drop()
# migrate()


session.add(Site(name='romansorin', host='https://romansorin.com'))
session.add(Screenshot(site_id=1, path='test', type=ScreenshotEnum['RGB']))
# session.add(Site())
# session.add(Screenshot(site_id=1))
# session.add(Screenshot(site_id=1))
# print(ScreenshotEnum.GREYSCALE)
# session.add(Screenshot(site_id=1))
# site = session.query(Site).filter(Site.id == 1).first()
# session.delete(site)
session.commit()

# TODO: REMIGRATE
