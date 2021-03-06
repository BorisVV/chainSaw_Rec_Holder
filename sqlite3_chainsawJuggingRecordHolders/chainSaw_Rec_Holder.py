import sqlite3

db = sqlite3.connect('chainSawRecorHolder.db') # creates or opens database file
cur = db.cursor() # Need a cursor object and
# Create a table if not exists...
cur.execute('create table if not exists recordHolder (fileId INTEGER PRIMARY KEY, holder text, country text, number int)')

def choice():
    options = '''\nWhat would you like to do:
    1. Add / Insert to table
    2. Show table's items
    3. Delete row in table
    4. Update / Edit table
    5. Exit '''     # This is printed to have the user select an option.

    while True:
        print(options)
        choice = input('Enter your selection (*number*): ')
        if choice == '1':
            addHolders() # Add new record holder function
        elif choice == '2':
            show_list() # Displays the list function
        elif choice == '3':
            delete_option()
        elif choice == '4':
            update_option()
        elif choice == '5':
            break
            # quit() # Closes the db


def addHolders():
    # Ask user for the information
    allHoldes = [] # Stores all the data the user enters as tuples in the while loop
    print('Pleas enter a name, country and number of catches')

    # The program will ask the user if it wants to add another record holder.
    while True:
        # fileId = 'NULL'
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
    print_rows() # Prints headers for the columns and the values below
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
    '''This prints the headers and display the list of item for the user to select or see'''
    # Prints headers for the columns and the values below
    cur.execute('select * from recordHolder')
    print('This is your list: \n')
    print(' ID  |Name  |Country  |Number of Catch') # These are used headers
    for value in cur:
        print(value)
    print()

def update_option():
    '''Updates or edit the selected ID, and updates the table'''
    print_rows() # Prints headers for the columns and the values below
    global holderID
    while True:
        try:  # This loop is used to check for int validation.
            holderID = int(input("Enter the ID number to UPDATE: "))
            break
        except Exception as e:
            continue
    global choose_option # This is used for the user input option.
    while True:
        choose_option = input("*Enter* \n'q' to exit, \n'1' for name, \n'2' for country, \n'3' for number of times:\n ")
        if choose_option != 'q' and choose_option != '1' and choose_option != '2' and choose_option != '3':
            continue
        else:
            break

    if choose_option == '1':  # If user enters one, the name is updated
        new_name = input("Enter new name: ")
        # update use parameter to store the values.
        update = 'UPDATE recordHolder SET holder = ? WHERE fileId =?'
        cur.execute(update, (new_name,  holderID))
        db.commit()

    elif choose_option == '2':  # If user enters two, the country is updated
        new_country = input("Enter new country: ")
        update = 'UPDATE recordHolder SET country = ? WHERE fileId =?'
        cur.execute(update, (new_country,  holderID))
        db.commit()

    elif choose_option == '3':  # If user enters three, the number of times is updated
        while True:
            try:
                new_number = int(input("Enter new number of catches: "))
                break
            except:
                continue
        update = 'UPDATE recordHolder SET number = ? WHERE fileId =?'
        cur.execute(update, (new_number,  holderID))
        db.commit()



def main():
    choice()
    db.commit()
    db.close()

if __name__ == '__main__':
        main()
