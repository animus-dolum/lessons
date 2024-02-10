import sqlite3

con = sqlite3.connect(input())

cur = con.cursor()

result = set(cur.execute("""SELECT year
    FROM films
WHERE title like "Х%"
""").fetchall())

for elem in result:
    print(*elem)

con.close()
