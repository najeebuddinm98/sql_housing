import View
import Insert

HOST = 'localhost'
USER = 'root'
PASSWD = 'lunaluna'

def viewListings():
    """viewing the listings in the database with filters"""
    print()
    View.process(HOST, USER, PASSWD)

def insertListing():
    """adding a listing to the database"""
    print()
    Insert.process(HOST, USER, PASSWD)


if __name__ == "__main__":
    print("Welcome to our application for advertising and viewing properties for sale.")
    while(True):
        print()
        print("""You can perform the following 2 actions:
1. View listings based on various filters
2. Add your own listing to the database
0. Exit the application\n""")

        opt = input("Enter your preferred option number: ")
        
        if opt == '0':
            break
        elif opt == '1':
            viewListings()
        elif opt == '2':
            insertListing()
        else:
            print("You have entered an invalid option number. Please try again\n")

        
    print("Thank you.")
            
    
    
