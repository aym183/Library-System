import csv
from tkinter import *
from collections import Counter
from matplotlib import pyplot as plt    
mylist = []
for i in range(1000,10000):
    mylist.append(i)
mynewlist = mylist
mylist2 = ['Book_1', 'Book_2', 'Book_1', 'Book_2', 'Book_2', 'Book_3', 'Book_1', 'Book_3', 'Book_4', 'Book_4']
mylist3 = ['1','2','3','4','5','6','7','8','9','10']
data = open('database.txt', encoding = 'utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
root = Tk()
root.title("Library Management System")
my_listbox = Listbox(root, bg = 'lawn green', height = 10, width = 60)
my_listbox.grid(row = 20, column = 1)

#Above are all the global variables and value, a listbox is used to display all the ouputs


#below is the first entry widget where you should enter the Book title you want to search up

Booksearchinput = Label(root, text = 'Please enter Book Title:')
Booksearchinput.grid(row = 0,column = 0) 
                        
BookTitle = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5) #Book Title
BookTitle.grid(row = 1 , column=0 ) 


# below is the function used to search for books

def search_for_books():
    with open('database.txt', 'r') as big_file:
        big_reader = csv.reader(big_file)
        for line in big_reader:
            if BookTitle.get() in line:
                global output
                my_listbox.insert(END, line)
                
                
        if BookTitle.get() not in mylist2:
            my_listbox.insert(END, "Invalid")

SearchButton = Button(root, text = "Search", padx = 5, pady = 5,command = search_for_books,fg='red')


SearchButton.grid(row = 2, column = 0) 

#after input is put, press the search button to get back the books with that title



# BEFORE CHECKING OUT A BOOK, ALWAYS SEARCH FOR THE BOOK WITH THE SEARCH BUTTON AS THE DETAILS ARE IMPORTANT TO FILL IN AND CHECK THE AVAILABILITY OF THE BOOK  


#below, are the entries required for a book checkout. First enter Book title, Serial no of book, do you want to checkout(Yes or No), ISBN, MEMBER ID, today's date
#All the boxes have specification above them about what to do.
#please fill in  all the boxes  then press the checkout button

BookCheckoutBooktitle = Label(root, text = 'Please enter Book Title: ')
BookCheckoutBooktitle.grid(row = 0, column = 1)

Booktitle2 = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5) #Book Title
Booktitle2.grid(row = 1, column = 1)

BookCheckoutSerialNumber = Label(root, text = 'Please enter Serial number of book: ')
BookCheckoutSerialNumber.grid(row = 2, column = 1)


BookSerial = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #Please enter serial number of book which has 0 under ID column
BookSerial.grid(row = 3, column = 1)

BookCheckoutDoyouCheckout= Label(root, text = 'Do you want to checkout? (Yes or No): ')
BookCheckoutDoyouCheckout.grid(row = 4, column = 1)


Checkoutresponse = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #Do you want to checkout?
Checkoutresponse.grid(row = 5, column = 1)

BookCheckoutISBN = Label(root, text = "Please enter ISBN: ")
BookCheckoutISBN.grid(row = 6, column = 1)

ISBN = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #ISBN
ISBN.grid(row = 7, column = 1)

BookCheckoutMemberID = Label(root, text = "Please enter Member's ID: ")
BookCheckoutMemberID.grid(row = 8, column = 1)                             

MemberID = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #Member ID
MemberID.grid(row = 9, column = 1)

BookCheckoutDate = Label(root, text = "Please enter present Date: ")
BookCheckoutDate.grid(row = 10, column = 1)  


CheckoutDate = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #Checkout Date
CheckoutDate.grid(row = 11, column = 1)

#below is the book checkout function as explained in the bookcheckout.py file
         

def book_checkout(): 
    
   
    if Booktitle2.get() not in mylist2:
        error2 = "Not valid"
        print(error2)
        output3 = Label(root, text = error2)
        output3.pack()
    with open('database.txt', 'r') as big_file:
        big_reader = csv.reader(big_file)
        for line in big_reader:
            if Booktitle2.get() in line:
                my_listbox.insert(END, line)
          #(Please enter serial number of book which has 0 under ID column)

        

          
        if BookSerial.get() in mylist3:
                if Booktitle2.get() == 'Book_1' and BookSerial.get() == mylist3[0]:
                    if data_lines[1][5] == '0':
                        my_listbox.insert(END, "Book is available")
                        
                        
                    else:
                        my_listbox.insert(END, "Book is not available at this time")
                        
                elif Booktitle2.get() =='Book_2' and BookSerial.get() ==mylist3[1]:
                    if data_lines[2][5] == '0':
                        my_listbox.insert(END, "Book is available")
                        
                    else:
                        my_listbox.insert(END, "Book is not available at this time")
                        
                        
                elif Booktitle2.get() == 'Book_1' and BookSerial.get() ==mylist3[2]:
                    if data_lines[3][5] == '0':
                        my_listbox.insert(END, "Book is available")
                        
                    else:
                        my_listbox.insert(END, "Book is not available at this time")
                        
                        
                elif Booktitle2.get() =='Book_2' and BookSerial.get() ==mylist3[3]:
                    if data_lines[4][5] == '0':
                        my_listbox.insert(END, "Book is available")
                        
                    else:
                        my_listbox.insert(END, "Book is not available at this time")
                        
                        
                elif Booktitle2.get() =='Book_2' and BookSerial.get() ==mylist3[4]:
                    if data_lines[5][5] == '0':
                        my_listbox.insert(END, "Book is available")
                        
                    else:
                        my_listbox.insert(END, "Book is not available at this time")
                        
                elif Booktitle2.get() =='Book_3' and BookSerial.get() ==mylist3[5]:
                    if data_lines[6][5] == '0':
                        my_listbox.insert(END, "Book is available")
                        
                    else:
                        my_listbox.insert(END, "Book is not available at this time")
                        
                elif Booktitle2.get() == 'Book_1' and BookSerial.get() ==mylist3[6]:
                    if data_lines[7][5] == '0':
                        my_listbox.insert(END, "Book is available")
                        
                    else:
                        my_listbox.insert(END, "Book is not available at this time")
                        
                if Booktitle2.get() =='Book_3' and BookSerial.get() ==mylist3[7]:
                    if data_lines[8][5] == '0':
                        my_listbox.insert(END, "Book is available")
                        
                    else:
                        my_listbox.insert(END, "Book is not available at this time")
                        
                elif Booktitle2.get() =='Book_4' and BookSerial.get() ==mylist3[8]:
                    if data_lines[9][5] == '0':
                        my_listbox.insert(END, "Book is available")
                        
                        
                    else:
                        my_listbox.insert(END, "Book is not available at this time")
                        
                elif Booktitle2.get() =='Book_4' and BookSerial.get() ==mylist3[9]:
                    if data_lines[10][5] == '0':
                        my_listbox.insert(END, "Book is available")
                        
                    else:
                        my_listbox.insert(END, "Book is not available at this time")
                        
                else:
                    my_listbox.insert(END, "")
                    
                
        if BookSerial.get() not in mylist3:
            my_listbox.insert(END, "Entry not valid")                
                        
        if Booktitle2.get() not in mylist2 :
            my_listbox.insert(END, "Invalid!") 
            
            

    if Checkoutresponse.get() == 'Yes':
        my_listbox.insert(END, "ISBN Please")
        
        with open('database.txt', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if ISBN.get() in line and int(MemberID.get())in mynewlist:
                    my_listbox.insert(END, "Book Withdrawn successfully!")
                    
                   
                    if ISBN.get() == '9783161484100' and BookSerial.get() == '1':
                        data_lines[1][5]= ('%d'%(int(MemberID.get())))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                            
                    if ISBN.get() == '9783161484105' and BookSerial.get() == '2':
                        data_lines[2][5]= ('%d'%(int(MemberID.get())))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                                
                    if ISBN.get() == '9783161484100' and BookSerial.get() == '3':
                        data_lines[3][5]= ('%d'%(int(MemberID.get())))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if ISBN.get() == '9783161484105' and BookSerial.get() == '4':
                        data_lines[4][5]= ('%d'%(int(MemberID.get())))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if ISBN.get() == '9783161484105' and BookSerial.get() == '5':
                        data_lines[5][5]= ('%d'%(int(MemberID.get())))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if ISBN.get() == '9783161484110' and BookSerial.get() == '6':
                        data_lines[6][5]= ('%d'%(int(MemberID.get())))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if ISBN.get() == '9783161484100' and BookSerial.get() == '7':
                        data_lines[7][5]= ('%d'%(int(MemberID.get())))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if ISBN.get() == '9783161484110' and BookSerial.get() == '8':
                        data_lines[8][5]= ('%d'%(int(MemberID.get())))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if ISBN.get() == '9783161484200' and BookSerial.get() == '9':
                        data_lines[9][5]= ('%d'%(int(MemberID.get())))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if ISBN.get() == '9783161484200' and BookSerial.get() == '10':
                        data_lines[10][5]= ('%d'%(int(MemberID.get())))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                                
                        
                    my_listbox.insert(END, "Thank You")
                    my_listbox.insert(END, ("ID : %s , Book Title : %s, Member ID : %s, ISBN : %s, Checkout Date : %s" %(BookSerial.get(),Booktitle2.get(),MemberID.get(),ISBN.get(),CheckoutDate.get())))
                    my_listbox.insert(END, "Please remember this information while returning your book")
                    
        
                    break
    
                   
                   
                    
                    
                elif ISBN.get() not in line and int(MemberID.get()) not in mynewlist:
                    my_listbox.insert(END, "Invalid!")
                    
                    break
    elif Checkoutresponse.get() == 'No':
        my_listbox.insert(END, "Bye")
       

#After all the inputs are put in their respective boxes, only then click the checkout button
    
Checkout_button = Button(root, text = "Checkout", padx = 5, pady = 5, command = book_checkout,fg='red')

Checkout_button.grid(row = 12, column = 1)





#below, are the entries required for a book return. First enter Do you want to return a book(Yes or NO) , ISBN, MEMBER ID, today's date, Serial number of book, checkout date
#All the boxes have specification above them about what to do.
#please fill in  all the boxes  then press the return button

BookReturnDoyouwanttoreturn = Label(root, text = "Do you want to return a book?(Yes or No): ")
BookReturnDoyouwanttoreturn.grid(row = 4, column = 0)

Returnresponse = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #Do you wish to return a book?
Returnresponse.grid(row = 5, column = 0)

BookReturnMemberID = Label(root, text = "Please enter Member's ID: ")
BookReturnMemberID.grid(row = 6, column = 0)

MemberID2 = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #Member ID
MemberID2.grid(row = 7, column = 0)

BookReturnISBN = Label(root, text = "Please enter ISBN: ")
BookReturnISBN.grid(row = 8, column = 0)                      
                        

ISBN2  = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #ISBN
ISBN2.grid(row = 9, column = 0)

BookReturnBooktitle = Label(root, text = "Please enter Book Title: ")
BookReturnBooktitle.grid(row = 10, column = 0) 

Booktitle3 = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #Book Title
Booktitle3.grid(row = 11, column = 0)

BookReturnTodayDate = Label(root, text = "Please enter Today's Date: ")
BookReturnTodayDate.grid(row = 12, column = 0)

ReturnDate = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #Today's Date
ReturnDate.grid(row = 13, column = 0)

BookReturnSerialNo = Label(root, text = "Please enter Serial number of book: ")
BookReturnSerialNo.grid(row = 14, column = 0)

BookSerial2 = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #Serial number of book taken
BookSerial2.grid(row = 15, column = 0)

BookReturnCheckoutDate = Label(root, text = "Please enter checkout date: ")
BookReturnCheckoutDate.grid(row = 16, column = 0)

CheckoutDate2 = Entry(root,width = 50,bg = 'black', fg='white', borderwidth = 5)  #Checkout Date
CheckoutDate2.grid(row = 17, column = 0)


#below is the book return function as explained in the bookreturn.py file
def book_return():
    
    if Returnresponse.get() == 'Yes':
        for i in range(0,11):
                if MemberID2.get() in data_lines[i][5]:
                    
                    my_listbox.insert(END, data_lines[i])
                    
                    my_listbox.insert(END, "Valid")
                    
                    

                
            
                    if BookSerial2.get() in mylist3 and ISBN2.get() in data_lines[i][1]:
                        if BookSerial2.get() =='1':
                            data_lines[1][5]= '0'
                            with open('database.txt',mode = 'w') as csvmy_FILE:
                                writerow = csv.writer(csvmy_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csvmy_FILE.close
                                
                        if BookSerial2.get() =='2':
                            data_lines[2][5]= '0'
                            with open('database.txt',mode = 'w') as csvmy_FILE:
                                writerow = csv.writer(csvmy_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csvmy_FILE.close
                                
                        if BookSerial2.get() =='3':
                            data_lines[3][5]= '0'
                            with open('database.txt',mode = 'w') as csvmy_FILE:
                                writerow = csv.writer(csvmy_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csvmy_FILE.close
                            
                        if BookSerial2.get() =='4':
                            data_lines[4][5]= '0'
                            with open('database.txt',mode = 'w') as csvmy_FILE:
                                writerow = csv.writer(csvmy_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csvmy_FILE.close
                                
                        if BookSerial2.get() =='5':
                            data_lines[5][5]= '0'
                            with open('database.txt',mode = 'w') as csvmy_FILE:
                                writerow = csv.writer(csvmy_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csvmy_FILE.close
                                
                        if BookSerial2.get() =='6':
                            data_lines[6][5]= '0'
                            with open('database.txt',mode = 'w') as csvmy_FILE:
                                writerow = csv.writer(csvmy_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csvmy_FILE.close
                                
                        if BookSerial2.get() =='7':
                            data_lines[7][5]= '0'
                            with open('database.txt',mode = 'w') as csvmy_FILE:
                                writerow = csv.writer(csvmy_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csvmy_FILE.close
                                
                        if BookSerial2.get() =='8':
                            data_lines[8][5]= '0'
                            with open('database.txt',mode = 'w') as csvmy_FILE:
                                writerow = csv.writer(csvmy_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csvmy_FILE.close
                                
                        if BookSerial2.get() =='9':
                            data_lines[9][5]= '0'
                            with open('database.txt',mode = 'w') as csvmy_FILE:
                                writerow = csv.writer(csvmy_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csvmy_FILE.close
                                
                        if BookSerial2.get() =='10':
                            data_lines[10][5]= '0'
                            with open('database.txt',mode = 'w') as csvmy_FILE:
                                writerow = csv.writer(csvmy_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csvmy_FILE.close
                                
                        my_listbox.insert(END, "Book returned successfully")        
                        
                    elif BookSerial2.get() not in mylist3:
                        my_listbox.insert(END, "Invalid!")
                        
                        break
               
                    with open(r'logfile.txt', 'a') as csvfile:    
                        newfile = csv.writer(csvfile)
                        newfile.writerow([BookSerial2.get(),Booktitle3.get(),MemberID2.get(),ISBN2.get(),CheckoutDate2.get(),ReturnDate.get()])
                        my_listbox.insert(END, "Thank You! Have a great day.")
                        
                        break
        else:
            my_listbox.insert(END, "Not valid!")
            
    else:
        my_listbox.insert(END, "Have a good day")
        
        
        
        
#After all the inputs are put in the respective boxes, only then click the return button
     
Return_button = Button(root, text = "Return",padx = 5, pady = 5, command = book_return,fg='red')
Return_button.grid(row = 18, column = 0)


#Below is the function for my weeding criteria, there is an obvious error where the graph is not embedded in the tkinter window, Apologies.




    
def book_weeding():
    plt.style.use("fivethirtyeight")
with open('logfile.txt') as myoo_file:
    book_reader = csv.DictReader(myoo_file)
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



Weeding_button = Button(root, text = "Weeding",padx = 5, pady = 5, command = book_weeding,fg='red')
Weeding_button.grid(row = 20, column = 0)

root.configure(bg='cyan')

root.mainloop()


# TO USE THE WINDOW, PLEASE EXIT FROM THE GRAPH FIRST
