#Booksearch.py


import csv
mylist = ['Book_1', 'Book_2', 'Book_1', 'Book_2', 'Book_2', 'Book_3', 'Book_1', 'Book_3', 'Book_4', 'Book_4']
def search_for_books():
    '''
    This function is used to help the librarian search for books
    To search for a book by entering a valid Book title.
    If valid, it will return all the respective copies of that book with it's availability status
    If Book title is unavailable, will return an error message
    if a book has 0 under last column(Member's ID column), it is available. If not, it is unavailable.
    '''
    books_search = input("Please enter Title: ")
    with open('database.txt', 'r') as big_file:
        big_reader = csv.reader(big_file)
        for line in big_reader:
            if books_search in line:
                print(line)
        if books_search not in mylist:
            print("Invalid!")
            
            # if the title is invalid, it prints out error message

#Below is the test code for this function          
if __name__ == '__main__':
    search_for_books()
                    
           
        
