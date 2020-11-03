import sqlite3
def insert(cur,name,adress,phone,email):
    cur.execute(''' INSERT INTO Contact (name,adress,phone,email)
    VALUES (?,?,?,?)
    ''',(name,adress,phone,email))
    

print('-----Starting Contact_Database-----')
conn=sqlite3.connect('db.sqlite')
cur=conn.cursor()
table_exists=False
if table_exists==False:
    cur.execute('DROP TABLE IF EXISTS Contact')
    cur.execute('''
    CREATE TABLE Contact (
        name TEXT UNIQUE,
        adress TEXT,
        phone TEXT,
        email TEXT
    )
    ''')

name='Walid'
adress='20 Avenue Albert Einstein'
phone='06923820'
email='test@hotmail.fr'
insert(cur,name,adress,phone,email)
conn.commit()

