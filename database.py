from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+mysqldb://root:MyNewPass@localhost/blogapplication'

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit = False, bind=engine)
Base=declarative_base()