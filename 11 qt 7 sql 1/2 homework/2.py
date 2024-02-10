import sqlite3

con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute('''
SELECT title FROM genres
    WHERE id in (
SELECT DISTINCT genre from films
    WHERE year between 2010 and 2011)
''').fetchall()

for elem in result:
    print(*elem)

con.close()
