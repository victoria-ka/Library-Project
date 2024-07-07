#Library menu
#Importing the library into the program
#Create an array with all the information in the CSV file
#Title,Author,Genre,Height,Publisher

import csv

inventory = []

with open('books.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        inventory.append(row)
    
#print(inventory)



def library_menu():
    print("Welcome to the Library!")
    print("Here we have a wide selection of books. Select a number from our menu items and press enter.\n")

    print("1: Return or donate a book.")
    print("2: Search our selection and check out.")
    print("3: See what you have checked out.")
    print("4: Quit.\n")

    selection = input("Your selection: \n")

    if (selection == 1):
        add_book()
    elif (selection == 2):
        search_books()
    elif (selection == 3):
        checked_out_books()4
    else:
        print('')
 

library_menu()

#Function for searching through books in the array
#Search by: Title, author, genre, or publisher

def search_books():

    #define variable for search result
    #

    query = input('\n')
    search_result = ''


    #for each result in the array

def add_book():
    variable = 0 #define array for new book 

def checked_out_books():
    variable = 0 #show books user has checked out already