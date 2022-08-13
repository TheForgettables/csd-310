###
#Title: WhatABook - Final
#uthor : Sean Geraghty
#Date 8/9/2022
#Description: Program designed to work alongside the WhatABook Database (Final for CYBR Class)
###




import sys
from typing import final
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print("\n -- MAIN MENU --\n")
    print("Choose One.\n")
    print(
          "1 - Books Available.\n"
          "2 - WhatABook Stores.\n"
          "3 - Account.\n"
          "4 - Exit.\n"
          )
    try:
        choice = int(input('Select a Number: '))

        return choice
    except ValueError:
        print("\n No Input Found - Try Again\n")

        sys.exit(0)

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    
    locations = _cursor.fetchall()
    print("\n -- Store Locations --")

    for locations in locations: 
         print("  Locale: {}\n".format(locations[1]))

def show_books(_cursor):

    _cursor.execute("SELECT book_id, book_name, author, details from book")

    books = _cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")

    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

def validate_user():
    try:
        user_id = int(input('\nEnter an ID'))

        if user_id < 0 or user_id > 3: 
            print("\n Invalid ID... Terminating \n")
            sys.exit(0)
        return user_id
    except ValueError: 
        
         print("\nInvalid ID... Terminating.\n")
         sys.exit(0)

def show_account_menu():

try:
    print("\n -- Account Menus --")
    print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
    account_option = int(input('                   <Select an Option>:'))

    return account_option
except ValueError: 
    print("Selection Invalid - Terminating \n")


def show_wishlist(_cursor,_user_id):
        
        _cursor.execute("SELECT user.user_id, user.last_name, user.first_name book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

        wishlist = _cursor.fetchall()

        print("\n -- Displaying Wishlist --")

        for book in wishlist:
            print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    
    query = ("SELECT book_id, book_name, author, details"
            "FROM book"
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
   
    print(query)

    _cursor.execute(query)
    
    books_to_add = _cursor.fetchall()

    print("\n Displaying Available Books ")

    for book in books_to_add:
         print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({})".format(_user_id, _book_id))

try: 
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    print("\n Welcome to WhatABook!")

    user_selection = show_menu()

    while user_selection !=4:

        if user_selection == 1: 
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)
        
        if user_selection == 3: 
            my_user_id = validate_user
            account_option = show_account_menu

            while account_option !=3:

                if account_option ==1: 
                    show_wishlist(cursor, my_user_id)

if account_option == 2:

    show_books_to_add(cursor, my_user_id)

    book_id - int(input("\n Enter the ID of Desired Book"))

    add_book_to_wishlist(cursor, my_user_id, book_id)

    db.commit()

    print("\n        Book id: {} was added to your wishlist".format(book_id))

if account_option < 0 or account_option > 3: 
    print("\n Selection Invalid - Try Again...")

account_option = show_account_menu()

if user selection < 0 or user_selection > 4: 
    print("\n Selection Invalid - Try again...")

    user_selection = show_menu()

print("\n\n Terminating...")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" Username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR
        print(" Database does not exist")
    
    else:
        print(error)
finally: 
    db.close()