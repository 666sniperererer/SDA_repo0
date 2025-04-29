from sqlalchemy import create_engine, text

# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

filename = r"./heslo.txt"
with open(filename, "rt") as f:
    password = f.readline()

# connection string
db = create_engine(f"mysql+mysqlconnector://root:{password}@localhost:3306/")

Base = declarative_base()
Session = sessionmaker(bind=db)

session = Session()

# test connection with SELECT 1
result = session.execute(text("SELECT 1"))
for row in result:
    print(row[0])

# session.execute(text("CREATE DATABASE sql_orm"))
