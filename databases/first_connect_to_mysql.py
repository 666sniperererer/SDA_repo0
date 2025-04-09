from mysql.connector import connect, Error

filename = r"./heslo.txt"
with open(filename, "rt") as f:
    password = f.readline()

print(password)

try:
    with connect(host="localhost", user="root", password=password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            print(cursor.fetchall())
            print(conn.user)


except Error as e:
    print(e)
