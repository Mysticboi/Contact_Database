import sqlite3

def insert(cur,name,adress,phone,email):
    try:
        cur.execute(''' INSERT INTO Contact (name,adress,phone,email)
        VALUES (?,?,?,?)
        ''',(name,adress,phone,email))
        print('Sucess: The contact:',(name,adress,phone,email),'has been added to the database')
    except:
        print('Failed: The contact name already exists.... ')

def find(cur,name):
    cur.execute('SELECT * FROM Contact WHERE name= ?',(name,))
    row=cur.fetchone()
    if row is None:
        print('Contact not found in the database')
    else:
        print('Contact found')
        print('\tName:',row[0])
        print('\tAdress:',row[1])
        print('\tPhone:',row[2])
        print('\tEmail:',row[3])

def delete(cur,name):
    cur.execute('SELECT * FROM Contact WHERE name= ?',(name,))
    row=cur.fetchone()
    if row is None:
        print("Failed: Contact doesn't exist in the database")
    else:
        cur.execute('DELETE FROM Contact WHERE name= ?',(name,))
        print("Sucess: The contact",name,"has been deleted from the database")

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

#----------START-------------
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
#Creating the menu
while True:
    print('-----Starting Contact_Database-----')
    print('\t0: Exiting Contact_Database')
    print('\t1: Inserting into the database')
    print('\t2: Finding a contact using a name')
    print('\t3: Deleting from the database using a name')
    print('\t4: Updating a contact in the database using a name')
    choice=input('Choose a number to choose an option: ')

    if choice in('0','1','2','3','4'):

        if(choice=='0'):
            print('-----Exiting Contact_Database-----')
            conn.close()
            break
        
        elif(choice=='1'):
            name=input('Enter name: ')
            adress=input('Enter adress: ')
            phone=input('Enter phone: ')
            email=input('Enter email: ')
            insert(cur,name,adress,phone,email)
            conn.commit()
        
        elif(choice=='2'):
            name=input('Enter name: ')
            find(cur,name)
            conn.commit()
        
        elif(choice=='3'):
            name=input('Enter name: ')
            delete(cur,name)
            conn.commit()

        elif(choice=='4'):
            name=input('Enter name: ')
            update(cur,name)
            conn.commit()
    
    else:
        print('Invalid input, try again...')
