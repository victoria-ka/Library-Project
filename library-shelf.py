
#Library menu
def library_menu():
    print("Welcome to the Library!")
    print("Here we have a wide selection of books. Select a number from our menu items and press enter.\n")

    print("1: Return a book.")
    print("2: Search our selection and check out.")
    print("3: See what you have checked out.")
    print("4: Check your existing fees.")
    print("5: Quit.\n4")

    selection = input("Your selection: \n")


library_menu()

#Importing the library into the program
#Create an array with all the information in the CSV file
#Title,Author,Genre,Height,Publisher

def import_csv():
    import csv

    inventory = []

    with open('books.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            inventory.append(row)
    
    print(inventory)

#Function for searching through books in the array
#Search by: Title, author, genre, or publisher

def search_books():
    #define variable for search result

    search_result = ''