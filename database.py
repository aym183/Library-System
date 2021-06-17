#database.py
#these are the separate functions packaged in each file 
#the functions used are below


#function used for searching books
from searchpackage import booksearch
booksearch.search_for_books()

#function used for checking out books

from checkoutpackage import bookcheckout
bookcheckout.book_checkout()

#function used for returning books

from returnpackage import bookreturn
bookreturn.book_return()

#function used for weeding criteria

from weedingpackage import bookweed
bookweed.book_weed()


