import sqlite3

db = sqlite3.connect('chainSawRecorHolder.db') # creates or opens database file
cur = db.cursor() # Need a cursor objectand
# Create a table if not exists...
cur.execute('create table if not exists recordHolder (holder text, country text, number int)')


def choice():
    print(''''What would you like to do:
        1. Add
        2. Delete
        3. Update
        4. Exit
        ''')

    choice = input('Enter your selection: ')
    while True:
        if choice == '1':
            addHolders()
        elif choice == '2':
            delete_option()
        elif choice == '4':
            break
            quit() # Closes the db


def addHolders():
    # Ask user for the information
    allHoldes = [] # Stores all the data the user enters as tuples in the while loop
    print('Pleas enter a name, country and number of catches')

    # The program will ask the user if it wants to add another record holder.
    while True:
        holder = input('Enter the name of the holder: ')
        country = input('Enter the country: ')
        while True:
            try:
                number = int(input('Enter number of catches: '))
                break # This breaks ones the user has enterd an integer
            except Exception as e:
                continue
        allHoldes.append((str(holder), str(country), int(number)))
        resp = input('Do you want to add another record holder to the list Y/N: ')
        if resp == 'Y'.lower():
            continue
        else:     # If the user enter 'y' the program loops again
            break

    # Use of parameters ? as place holders
    # cur.execute('insert into recordHolder values (?, ?, ?)', (holder, country, number))

    # This line uses the array allHolders add to db with executemany.
    cur.executemany('insert into recordHolder values (?, ?, ?)', (allHoldes))

    # Fetch and display
    cur.execute('select * from recordHolder')

    # for loop
    print('Name,   Country,  Number of Catcher')
    for row in cur:
        print(row)

    db.commit() # Saves changes
    db.close() # Closes the db

def delete_option():
    cur.execute('select * from recordHolder')
    print("Opened database successfully")
    for row in cur:
         print(row)
    # name = input('Enter name of holder: ')
    cur.execute("delete * from recordHolder")
    db.commit


    # cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    # for row in cursor:
    #     print row
    #
    print("Operation done successfully")
    db.close()

def quit():
    db.close()

def main():
    choice()

if __name__ == '__main__':
        main()
