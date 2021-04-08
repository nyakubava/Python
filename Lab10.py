import sqlite3

# connect with db
con = sqlite3.connect('yakubava.db')
query = '''INSERT OR IGNORE INTO PopByRegion (Region, Population)
        VALUES (?, ?)'''
records = [('Central Africa', 330993),
           ('Southeastern Africa', 743112),
           ('Japan', 100562)]
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS PopByRegion')
# creating table
cur.execute('CREATE TABLE PopByRegion (Region TEXT,'
            ' Population INTEGER)')
# insert data to table
cur.executemany(query, records)
con.commit()
# execute queries
cur.execute('SELECT Region, Population FROM PopByRegion')
record = cur.fetchall()
print(record)
cur.execute('SELECT Region, Population FROM PopByRegion'
            ' ORDER by Region')
record = cur.fetchall()
print(record)
cur.execute('SELECT Region FROM PopByRegion')
record = cur.fetchall()
print(record)
cur.execute('SELECT Region FROM PopbyRegion WHERE Population'
            ' > 400000')
record = cur.fetchall()
print(record)
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
record = cur.fetchall()
print(record)
cur.execute('''UPDATE PopByRegion SET Population = 100600
             WHERE Region = "Japan"''')
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
record = cur.fetchall()
print(record)
cur.execute('DELETE FROM PopByRegion WHERE Region < "S"')
cur.execute('SELECT * FROM PopByRegion')
record = cur.fetchall()
print(record)
# close
cur.close()
con.close()
