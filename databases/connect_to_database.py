from mysql.connector import connect, Error

filename = r"./heslo.txt"
with open(filename, "rt") as f:
    password = f.readline()

# vypíšeme databáze na serveru
try:
    with connect(host="localhost", user="root", password=password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SHOW DATABASES")  # uložíme výsledek execute do kurzoru
            print(cursor.fetchall())  # získáme všechny výsledky uložené v kurzoru
            print(conn.user)

except Error as e:
    print(e)

# vypíšeme tabulky z databáze
try:
    with connect(
        host="localhost", user="root", password=password, database="world"
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            print(cursor.fetchall())

except Error as e:
    print(e)
