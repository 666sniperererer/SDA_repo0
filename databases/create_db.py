from mysql.connector import connect, Error

filename = r"./heslo.txt"
with open(filename, "rt") as f:
    password = f.readline()

"""
try:
    with connect(host="localhost", user="root", password=password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE online_movie_rating")

except Error as e:
    print(e)
"""

try:
    with connect(host="localhost", user="root", password=password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE automobilka")

except Error as e:
    print(e)
