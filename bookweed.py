def book_weed():
    '''
    This function is used to show the criteria that I have decided to use
    to show which books should be removed
    The book which has been withdrawn the least amount of times should be removed
    It is represented in the form of a bar graph
    '''
    import csv
    from collections import Counter
    from matplotlib import pyplot as plt
    plt.style.use("fivethirtyeight")
    with open('logfile.txt') as my_file:
        book_reader = csv.DictReader(my_file)
        book_counter = Counter()
        for row in book_reader:
            book_counter.update(row['Book Title'].split(';'))
    books = []
    popularity = []
    for item in book_counter.most_common():
        books.append(item[0])
        popularity.append(item[1])
    books.reverse()
    popularity.reverse()
    plt.barh(books, popularity)
    plt.title("Book Weeding")
    plt.xlabel("Number of times withdrawn")
    plt.ylabel("BOOK TITLE")
    plt.tight_layout()
    plt.show()

    # Below is the test code for my function
if __name__ == '__main__':
    book_weed()
