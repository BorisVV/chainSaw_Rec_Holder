from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configure_recordHolder
from configure_recordHolder import RecordHolders

engine = create_engine('sqlite:///record_holders.db', echo=False)   # echo=True turns on logging

# Session = sessionmaker()
# This is the way the doc for sqlalchemy is written
# Session.configure(bind=engine)

Session = sessionmaker(bind=engine) # Use engine created above.and

# This is used for the session and is closed at the end in the main()
session = Session()


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


# Add new record holders
def addHolders():
    # Ask user for the information
    allHoldes = [] # Stores all the data the user enters as tuples in the while loop
    print('Pleas enter a name, country and number of catches')

    # The program will ask the user if it wants to add another record holder.
    while True:
        number = 0
        holder = input('Enter the name of the new record holder: ')
        country = input('Enter the country: ')
        while True: # This while loop is for the int that is needed for number of times
            try:
                number = int(input('Enter number of catches: '))
                break # This breaks ones the user has enterd an integer
            except Exception as e:
                continue
        # This appends the items as tuple to the array list.
        # allHoldes.append((None, str(holder), str(country), int(number)))
        session.add(RecordHolders(name = holder, country = country, number = number))
        session.commit()
        resp = input('Do you want to add another record holder to the list Y/N: ')
        if resp != 'Y'.lower(): # Checks for response to break the loop
            print_row
            break
             # If the user enter 'y' the program loops again



def delete_option():
    print_row() # Prints headers for the columns and the values below
    # The user is asked to enter the id from the list.
    print('Select from list above\n')
    enterId = int(input('Enter the "ID" of the raw that you want to deleted:\n'))
    for row in session.query(RecordHolders):
        if enterId == row.id:
            session.delete(row) # This deletes the whole row.
            session.commit()
            print(' {} \n Deleted Succesfully!'.format(row))
            break
        else:
            session.rollback()



def print_row():
    '''This prints the headers and display the list of item for the user to select or see'''
    # Prints headers for the columns and the values below
    print(' ID -> Name -> Country -> Number of Catches') # These are used headers
    for row in session.query(RecordHolders):
        print(row)
    print()

def update_option():
    '''Updates or edit the selected ID, and updates the table'''
    print_row() # Prints headers for the columns and the values below

    # This is to verify that the user enters an integer.
    global holderID
    while True:
        try:  # This loop is used to check for int validation.
            holderID = int(input("Enter the ID number to UPDATE: "))
            break
        except Exception as e:
            continue

    # This is to confirm that the user selects from one of the choices below.
    global choose_option # This is used for the user input option.
    while True:
        choose_option = input("*Enter* \n'q' to exit, \n'1' for name, \n'2' for country, \n'3' for number of times:\n ")
        if choose_option != 'q' and choose_option != '1' and choose_option != '2' and choose_option != '3':
            continue
        else:
            break

    # This will loop in the items and if the number matches to one in the list then it check the choose_option var and
    # applies its changes.
    for row in session.query(RecordHolders):
        if row.id == holderID and choose_option == '1':
            new_name = input("Enter new name: ")
            row.name = new_name
            session.commit()
            print('The holder with id #{} \nwas updated succefully with the new name "{}" \n{}'.format(row.id, row.name, row))
            break

        if row.id == holderID and choose_option == '2':
            new_country = input("Enter new country: ")
            row.country = new_country
            session.commit()
            print('The holder with id #{} \nwas updated succefully with the new name "{}" \n{}'.format(row.id, row.country, row))
            break

        if row.id == holderID and choose_option == '3':
            new_number = input("Enter new number of catches: ")
            row.number = new_number
            session.commit()
            print('The holder with id #{} \nwas updated succefully with the new name "{}" \n{}'.format(row.id, row.name, row))
            break

        else:
            session.rollback()


def main():
    choice()
    session.close() # This close the session()


if __name__ == '__main__':
    print('Welcome to the \nCHAINSAW JUGGLING RECORD HOLDERS DB')

    ''' You might want to comment this initial list so it doe't duplicat everytime you run the up'''
    # record1 = RecordHolders(name='John', country='United States', number=10)
    # record2 = RecordHolders(name='Mark', country='England', number=15)
    # record3 = RecordHolders(name='Bladimir', country='Russia', number=25)
    # record4 = RecordHolders(name='Juan', country='Mexico', number=30)
    # record5 = RecordHolders(name='Ernest', country='Ireland', number=18)
    #     #Add all the new records to the table.
    # session.add_all([record1, record2, record3, record4, record5])
    # session.commit() # Don't forget to commit.
    ''' of the section that should be commented after running the app for the first time.'''

    main()
