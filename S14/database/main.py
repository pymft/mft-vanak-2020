import sqlite3

with sqlite3.connect("./db.sqlite") as conn:

    conn.execute("CREATE TABLE IF NOT EXISTS person (name TEXT, age INTEGER)")

    conn.execute("INSERT INTO person (name, age) VALUES ('Jack', 24)")
    conn.execute("INSERT INTO person (name, age) VALUES ('Joe', 30)")
    conn.commit()

    rows = conn.execute("SELECT * FROM person")

    for row in rows:
        print(row)