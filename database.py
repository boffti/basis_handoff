from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Go to https://goo.gl/SL28qS for DB Query Cheat Sheet

# DB Created
engine = create_engine('sqlite:///handoff.db', convert_unicode=True)

# Import this in other Packages to Query the DB #########################################
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
#########################################################################################

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)