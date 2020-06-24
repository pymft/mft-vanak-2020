import sqlite3

with sqlite3.connect("./chinook.db") as conn:
    result = conn.execute("""
    SELECT t.name, t.milliseconds/60000, a.Title, s.Name FROM tracks  AS t 
    JOIN albums AS a  ON t.trackid = a.albumid
    JOIN artists as s ON a.ArtistId = s.ArtistId
    WHERE t.genreid = 1
    ORDER BY t.milliseconds desc
    LIMIT 10
    """)


for row in result:
    print(row)