import sqlite3


class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.initialized = False

        return cls.instance

    def __init__(self):
        if not self.initialized:

            self.conn = sqlite3.connect("./db.sqlite")

            self.initialized = True


a = Singleton()
b = Singleton()
c = Singleton()
d = Singleton()
e = Singleton()

a.conn.execute("CREATE TABLE IF NOT EXISTS person (name TEXT, age INTEGER)")

b.conn.execute("INSERT INTO person (name, age) VALUES ('Jack', 24)")
c.conn.execute("INSERT INTO person (name, age) VALUES ('Joe', 30)")
rows = d.conn.execute("SELECT * FROM person")

for row in rows:
    print(row)
