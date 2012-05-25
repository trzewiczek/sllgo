# coding: utf-8
import csv
import sqlite3

con = sqlite3.connect('bestia.db')
cur = con.cursor()

# I N C O M E S
reader = csv.reader( open('data/_Rb27s_csv.csv'), delimiter=';', quotechar='"' )
reader.next()

try:
    cur.execute('''CREATE TABLE income
                   (voivod text, poviat text, parish text, type text,
                    part text, subpart text, paragraph text, source int,
                    plan real, income real)''')
except:
    pass

for p in reader:
    values = [ p[1], p[2], p[3], p[4], p[8], p[9], p[10], p[11], p[12], p[15] ]
    values = [ e.decode('utf-8') for e in values ]

    cur.execute('''INSERT INTO income VALUES (?,?,?,?,?,?,?,?,?,?)''', tuple(values) )

con.commit()


# S P E N D I N G S
reader = csv.reader( open('data/_Rb28s_csv.csv'), delimiter=';', quotechar='"' )
reader.next()
try:
    cur.execute('''CREATE TABLE outcome
                   (voivod text, poviat text, parish text, type text,
                    part text, subpart text, paragraph text, source int,
                    plan real, outcome real)''')
except:
    pass

for p in reader:
    values = [ p[1], p[2], p[3], p[4], p[8], p[9], p[10], p[11], p[12], p[14] ]
    values = [ e.decode('utf-8') for e in values ]

    cur.execute('''INSERT INTO outcome VALUES (?,?,?,?,?,?,?,?,?,?)''', tuple(values) )

con.commit()
cur.close()
