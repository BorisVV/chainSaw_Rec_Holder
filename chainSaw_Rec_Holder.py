import sqlite3

db = sqlite3.connect('chainSawRecorHolder.db') # creates or opens database file
cur = db.cursor() # Need a cursor object and
# Create a table if not exists...
cur.execute('create table if not exists recordHolder (fileId INTEGER PRIMARY KEY, holder text, country text, number int)')

def choice():
    options = '''What would you like to do:
        1. Add
        2. Show list
        3. Delete
        4. Update
        5. Exit
        '''     # This is printed to have the user select an option.

    while True:
        print(options)
        choice = input('Enter your selection: ')
        if choice == '1':
            addHolders() # Add new record holder function
        elif choice == '2':
            show_list() # Displays the list function
        elif choice == '3':
            delete_option()
        elif choice == '5':
            break
            # quit() # Closes the db


def addHolders():
    # Ask user for the information
    allHoldes = [] # Stores all the data the user enters as tuples in the while loop
    print('Pleas enter a name, country and number of catches')

    # The program will ask the user if it wants to add another record holder.
    while True:
        fileId = 'NULL'
        holder = input('Enter the name of the record holder: ')
        country = input('Enter the country: ')
        while True: # This while loop is for the int that is needed for number of times
            try:
                number = int(input('Enter number of catches: '))
                break # This breaks ones the user has enterd an integer
            except Exception as e:
                continue
        # This appends the items as tuple to the array list.
        allHoldes.append((None, str(holder), str(country), int(number)))
        resp = input('Do you want to add another record holder to the list Y/N: ')
        if resp != 'Y'.lower(): # Checks for response to break the loop
            break
             # If the user enter 'y' the program loops again

    # This line uses the array allHolders add to db with executemany.
    cur.executemany('insert into recordHolder values (?, ?, ?, ?)', (allHoldes))

    # Fetch and display
    cur.execute('select * from recordHolder')

    # for loop
    print_rows() # Calls funcion to print headers
    for row in cur:
        print(row)

    db.commit() # Saves changes



def delete_option():
    cur.execute('select * from recordHolder')
    print_rows() # Prints headers for the columns and the values below
    for value in cur:
        print(value)
    # The user is asked to enter the id from the list.
    enterId = int(input('Enter the "ID" of the raw that you want deleted: '))
    delete_raw = 'DELETE FROM recordHolder WHERE fileId=?' # This deletes the by id
    cur.execute(delete_raw, (enterId,)) # Executes the delete action
    print("Operation done successfully")
    db.commit() # saves data




def show_list():
    '''This display the list of items stored'''
    cur.execute('select * from recordHolder')
    print('This is your list:')
    print_rows() # Prints headers for the columns and the values below
    for value in cur:
        print(value)

def print_rows():
    # Prints headers for the columns and the values below
    return print('ID, Name, Country, Number of Catcher')


def main():
    choice()
    db.commit()
    db.close()

if __name__ == '__main__':
        main()
