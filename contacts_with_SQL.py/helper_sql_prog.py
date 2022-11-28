import sqlite3

#build the sql table
con = sqlite3.connect("ShirContacts.db") 
cur = con.cursor()
# cur.execute("create TABLE Contacts(contactID ,NAME, PhoneNumber)")
 
def add_contact():
    contactID_user= input ("enter id: ")
    Name_user = input ("enter name: ")
    PhoneNumber_user = input ("enter number: ")
    cur.execute("insert into contacts (contactID ,NAME, PhoneNumber) VALUES (?, ?, ?)", (contactID_user, Name_user, PhoneNumber_user))
    con.commit()

def search_a_contact():
    name_2_search = input("enter a name you want to search: ")
    data = cur.execute (f"select NAME, PhoneNumber FROM Contacts where NAME = '{name_2_search}'")
    rows = (data.fetchall())
    if len(rows) != 0 :
        for row in rows:
            print(f'your contact name : {row[0]}')
            print(f'your contact number : {row[1]}')
    else :
        print("your contact not found")

def delete_contact ():
    name_2_delete = input("enter a name you want to delete: ")
    data = cur.execute (f"select NAME FROM Contacts where NAME = '{name_2_delete}'")
    rows = (data.fetchall())
    if len(rows) != 0 :
        for row in rows:
            print (f'{row[0]} will be delete from your contacts list')
        cur.execute(f"delete from contacts where NAME = '{name_2_delete}'")
    else :
        print("your contact not found")
    con.commit()

def print_all():
    data = cur.execute ("select * from contacts where NAME is not NULL")
    all_data = (data.fetchall())
    print (f"contacts: {all_data}")



