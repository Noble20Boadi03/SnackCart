from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#settting up the database
db_url = 'postgresql://postgres:StrongPass123@localhost:5432/Bras'
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

