import psycopg

Conn = psycopg.connect(
    host="localhost",
    dbname="Budget_tracker",
    user="postgres",
    password="$praj$"
)

print("connected!")

Conn.close()

cursor = Conn.cursor

cursor.execute(
    """
    insert into expenses (category, amount)
    values (%s, %s)
    """,
    ("food" , 100)
)

Conn.commit()

print("expense added")

Conn.close()