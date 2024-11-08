import sqlite3

con = sqlite3.connect("tutorial.bd")
cur = con.cursor()

cur.execute("CREATE TABLE movie(title, year, score)")

res = cur.execute("SELECT name FROM sqlite_master")

res.fetchone()

res = cur.execute("SELECT name FROM sqlite_master WHERE name ='spam'")

res.fetchone() is None

cur.execute("""
	INSERT INTO movie VALUES 
		('Monty Python and the Holy Grail', 1975, 8.2),
		('Inception', 2010, 8.8)
""")

con.commit()

data = [
	("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
	("Monty Python's The Meaning of Life", 1983, 7.5),
	("Monty Python's Life of Brian", 1979, 8.0),
]

cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
	print(row)

con.close()
new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, tear = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, realeased in {year}')

