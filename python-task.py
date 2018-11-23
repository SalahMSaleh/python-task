import sqlite3
#===========================================================================================================
# Start connection to in memory database
#===========================================================================================================
con = sqlite3.connect(':memory:')
c = con.cursor()
#===========================================================================================================
# Create two tables in database TODO Task && TODO_MIRROR
#===========================================================================================================
def create_tables():
    c.execute("""CREATE TABLE TODO_Task (ID unique, Name text, Description text)""")
    c.execute("""CREATE TABLE TODO_MIRROR (ID unique, Name text, Description text)""")
#===========================================================================================================
# The main page for the database and the user choose the table he wants to operat on
#===========================================================================================================
def start():
    num=input('Which Table do you want?\n1-TODO Task\n2-TODO MIRROR\n3-Print Tables\n0-Exit\n')
    if (num == '1' or num == '2'):
        operation(num)
    if (num == '3'):# For Printing
        print_tables()
        start()
#===========================================================================================================
# The operation page and the user enters the operation he wants to do on the table he chose
#===========================================================================================================
def operation(table):
    num=input('What Operation you want to do?\n1-ADD\n2-Modify\n3-Delete\n4-Print\n00-Back\n')
    if (num == '1'):# For Adding 
        insert()
    if (num == '2'):# For Modifying
        modify()
    if (num == '3'):# For Deleting
        delete()
    if (num == '00'):# To Back to the main page
        start()
#===========================================================================================================
# The user enters the ID,Name and Description of the record he wants to add with makeing sure the ID dosent duplicate    
#===========================================================================================================
def insert():
    
    try:
        ID = input('ID: ')
        Name = input('Name: ')
        Description = input('Description: ')
        c.execute("INSERT INTO TODO_Task VALUES (:ID, :Name, :Description)", {'ID': ID, 'Name': Name, 'Description': Description})
        c.execute("INSERT INTO TODO_MIRROR VALUES (:ID, :Name, :Description)", {'ID': ID, 'Name': Name, 'Description': Description})
    except:
        print('\nID already taken')
        insert()
    start()
#===========================================================================================================
# If the user wants to modify a record he enters the ID of the record he wants to modify 
#===========================================================================================================
def modify():
    print_tables()
    ID =input('What is the ID of the record you want to modify?\n')
    Name = input('Name: ')
    Description = input('Description: ')
    c.execute("UPDATE TODO_Task SET  Name = :Name, Description = :Description WHERE ID = :ID", {'ID': ID,'Name': Name, 'Description': Description})
    c.execute("UPDATE TODO_MIRROR SET Name = :Name, Description = :Description WHERE ID = :ID", {'ID': ID, 'Name': Name, 'Description': Description})
    start()
#===========================================================================================================
# If the user wants to delete a record he enters the ID of the record he wants to delete
#===========================================================================================================
def delete():
    print_tables()
    ID =input('What is the ID of the record you want to delet?\n')
    c.execute("DELETE FROM TODO_Task WHERE ID = :ID ", {'ID': ID})
    c.execute("DELETE FROM TODO_MIRROR WHERE ID = :ID ", {'ID': ID})
    start()
#===========================================================================================================
# To print both tables
#===========================================================================================================
def print_tables():
        print('\nTODO_Task Table')
        c.execute("SELECT * FROM TODO_Task")
        print(c.fetchall())
        print('TODO_MIRROR Table')
        c.execute("SELECT * FROM TODO_MIRROR")
        print(c.fetchall())

#===========================================================================================================
#first time the script runs it creats two tables and start the main page
#===========================================================================================================        
create_tables()
start()

