from mysql.connector import connect, Error

filename = r"./heslo.txt"
with open(filename, "rt") as f:
    password = f.readline()

try:
    with connect(
        host="localhost", user="root", password=password, database="online_movie_rating"
    ) as conn:
        """vytvoření tabulky zakomentováno, nebudeme tvořit podruhé
        with conn.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE movies("
                "id INT AUTO_INCREMENT PRIMARY KEY,"
                "title VARCHAR(100)"
                ")"
            )
        """
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO movies (title) VALUES ('Hellraiser')")
            conn.commit()

except Error as e:
    print(e)
