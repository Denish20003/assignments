import csv
import sqlite3

with open('service.csv', newline='') as f:
     reader = csv.reader(f)
     data = [tuple(row) for row in reader]

conn = sqlite3.connect('keyclub.sqlite')
c = conn.cursor() 
c.executemany('INSERT INTO service VALUES(?,?,?,?)', data)

conn.commit()
conn.close()
