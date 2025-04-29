from sqlalchemy import create_engine

from shop_definition import Base

filename = r"./heslo.txt"
with open(filename, "rt") as f:
    password = f.readline()

# connection string
db = create_engine(f"mysql+mysqlconnector://root:{password}@localhost:3306/sql_orm")


Base.metadata.create_all(db)
