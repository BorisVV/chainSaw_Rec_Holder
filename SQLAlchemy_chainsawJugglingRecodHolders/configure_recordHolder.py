from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Integer, String, Column, Sequence
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import event
from sqlalchemy.engine import Engine

# This is to enforce foreign keys
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=OFF")
    cursor.close()
## end SQLite specific code

Base = declarative_base()
engine = create_engine('sqlite:///record_holders.db', echo=True) # echo=True is for debbuging.


class RecordHolders(Base):
    ''' Defines metadata about the record's holders. create objects form rows in the table. '''

    __tablename__ = 'recordHolders' # Name of table.

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    country = Column(String(50))
    number = Column(Integer)

    def __repr__(self):
        return 'Holder: id = {} name = {} country = {} number_of_catches = {}'.format(self.id, self.name, self.country, self.number)

Base.metadata.create_all(engine)
