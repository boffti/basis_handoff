from sqlalchemy import Column, Integer, String
from database import Base

# Create model classes

# System Data Table
class Handoff(Base):
    __tablename__ = 'handoff_data'
    id = Column(Integer, primary_key=True)
    date = Column(String(), nullable=False)
    shift = Column(String(), nullable=False)
    tag = Column(String(), nullable=False)
    long_description = Column(String(), nullable=False)
    author = Column(String(), nullable=False)

    # Constructor
    def __init__(self, date=None, shift=None, tag=None, long_description=None, author=None):
        self.date = date
        self.shift = shift
        self.tag = tag
        self.long_description = long_description
        self.author = author

    # Print object
    def __repr__(self):
        return '<Post %r>' % (self.hostName)