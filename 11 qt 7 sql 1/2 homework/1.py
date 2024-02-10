import sqlite3

con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute('''
SELECT title FROM films
    WHERE year between 1995 and 2000 and genre = (
SELECT id from genres
    WHERE title = 'детектив')
''').fetchall()

for elem in result:
    print(*elem)

con.close()
