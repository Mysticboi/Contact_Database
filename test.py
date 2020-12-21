import sqlite3
insert()

def insert(cur,name,adress,phone,email):
    try:
        cur.execute(''' INSERT INTO Contact (name,adress,phone,email)
        VALUES (?,?,?,?)
        ''',(name,adress,phone,email))
        print('Sucess: The contact:',(name,adress,phone,email),'has been added to the database')
    except:
        print('Failed: The contact name already exists.... ')

def update(cur,name):
    cur.execute('SELECT * FROM Contact WHERE name= ?',(name,))
    row=cur.fetchone()
    if row is None:
        print("Failed: Contact doesn't exist in the database")
    else:
        print("Contact found please enter new informations")
        adress=input('Enter new adress: ')
        phone=input('Enter new phone: ')
        email=input('Enter new email: ')
        cur.execute('''UPDATE Contact SET adress= ?,
        phone= ?,
        email= ?
        WHERE name= ? ''',(adress,phone,email,name))
        print("Sucess: Contact has been updated")
    
conn=sqlite3.connect('db.sqlite')
cur=conn.cursor()
email=''
#email=input('Enter your email')
print('Your email is',email)
name=input ('Enter Name: ')
adress='TestAdress'
email='TestEmail'
phone='TestPhone'
insert(cur,name,adress,email,phone)
conn.commit()
cur.execute('SELECT * FROM Contact WHERE name= ?',(name,))
row=cur.fetchone()
if row is None:
    print('Contact not found in the database')
else:
    print('Contact found')
    print('\tName:',row[0])
    print('\tAdress:',row[1])
    print('\tEmail:',row[2])
    print('\tPhone:',row[3])

conn.commit()

print('------UDPATE TESTING ---------')
name=input('Enter name: ')
update(cur,name)
conn.commit()
