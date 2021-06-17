#this is the function used for the checkout process
import csv
mylist = []
mylist2 = ['Book_1', 'Book_2', 'Book_3', 'Book_4']
mylist3 = ['1','2','3','4','5','6','7','8','9','10']
data = open('database.txt', encoding = 'utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)           
for i in range(1000,10000):
    mylist.append(i)
def book_checkout():
    '''
    This is the function used to help  the librarian checkout a book.
    First they need to enter the book title, and see if it is available
    If there is a 0 under Member's ID, it indicates that it is available.
    If librarian selects unavailable book, appropriate message will show up and then to start over the Librarian will have to enter "No" in the "Do you want to checkout?" section
    if librarian selects available book,
    then please enter the serial number of that book
    If all entries are valid, please enter "Yes" in the "Do you want to checkout?" section
    then enter appropriate values for ISBN and Member's ID
    If valid, Please enter the date which will be the checkout date that the user should remember when returning
    And after this, the book will be checked out successfully
    '''
    books_search = input("Please enter Title: ") 
          
    if books_search not in mylist2:
        print("Not valid")
    
    with open('database.txt', 'r') as big_file:
        big_reader = csv.reader(big_file)
        for line in big_reader:
            if books_search in line:
                print(line)
                
             #Please select the serial number of the book selected which has 0 under the Member's ID column which indicates that it is available
        
        ID = input("Please select your book which has 0 under the ID column: ")
    
        if ID in mylist3:
            
            if books_search == 'Book_1' and ID == mylist3[0]:
                
                
                if data_lines[1][5] == '0':
                        print("Book is available")
                            
                else:
                        print("Book is not available at this time")
                            
                        
            if books_search =='Book_2' and ID ==mylist3[1]:
                   
                if data_lines[2][5] == '0':
                        print("Book is available")
                            
                else:
                        print("Book is not available at this time")
                            
                        
            if books_search == 'Book_1' and ID ==mylist3[2]:
                    
                if data_lines[3][5] == '0':
                        print("Book is available")
                           
                else:
                        print("Book is not available at this time")
                            
                        
            if books_search =='Book_2' and ID ==mylist3[3]:
                    
                    if data_lines[4][5] == '0':
                        print("Book is available")
                            
                    else:
                        print("Book is not available at this time")
                            
                        
            if books_search =='Book_2' and ID ==mylist3[4]:
                   
                    if data_lines[5][5] == '0':
                        print("Book is available")
                            
                    else:
                        print("Book is not available at this time")
                            
                        
            if books_search =='Book_3' and ID ==mylist3[5]:
                   
                    if data_lines[6][5] == '0':
                        print("Book is available")
                            
                    else:
                        print("Book is not available at this time")
                           
                        
            if books_search == 'Book_1' and ID ==mylist3[6]:
                    
                    if data_lines[7][5] == '0':
                        print("Book is available")
                            
                        
                    else:
                        print("Book is not available at this time")
                            
                        
            if books_search =='Book_3' and ID ==mylist3[7]:
                  
                    if data_lines[8][5] == '0':
                        print("Book is available")
                            
                    else:
                        print("Book is not available at this time")
                            
                        
            if books_search =='Book_4' and ID ==mylist3[8]:
                    
                    if data_lines[9][5] == '0':
                        print("Book is available")
                            
                    else:
                        print("Book is not available at this time")
                            
                         
            if books_search =='Book_4' and ID ==mylist3[9]:
                    
                    if data_lines[10][5] == '0':
                        print("Book is available")
                            
                    else:
                        print("Book is not available at this time")
                           
                        
                        
            else:
                print("")
                
                    
        if ID not in mylist3:
            print("Entry not valid")
            
        # If all the entries are valid, it then asks the user if they want to checkout
        # If the entries are returned as not valid, Please enter 'No' in the do you want to checkout section
                        
    #Yes or No
    CheckoutResponse = input("Do you want to checkout? ")
         #Please check from the valid title outputs and enter the designated ISBN number for that book
    if CheckoutResponse == 'Yes':
        Book_ISBN = input("Please enter ISBN for that book: ")
        Members_ID = int(input("Please enter Members ID (only integers): "))
       
        with open('database.txt', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if Book_ISBN in line and Members_ID in mylist:
                    print("Book Withdrawn successfully!")
                   #Below is the code to change the member'ID column from 0 to the member's ID to show that particular book has been checked out
                    
                    if Book_ISBN == '9783161484100' and ID == '1':
                        data_lines[1][5]= ('%d'%(Members_ID))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows([data_lines])
                                csv2_FILE.close
                            
                    if Book_ISBN == '9783161484105' and ID == '2':
                        data_lines[2][5]= ('%d'%(Members_ID))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                                
                    if Book_ISBN == '9783161484100' and ID == '3':
                        data_lines[3][5]= ('%d'%(Members_ID))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if Book_ISBN == '9783161484105' and ID == '4':
                        data_lines[4][5]= ('%d'%(Members_ID))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if Book_ISBN == '9783161484105' and ID == '5':
                        data_lines[5][5]= ('%d'%(Members_ID))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if Book_ISBN == '9783161484110' and ID == '6':
                        data_lines[6][5]= ('%d'%(Members_ID))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if Book_ISBN == '9783161484100' and ID == '7':
                        data_lines[7][5]= ('%d'%(Members_ID))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if Book_ISBN == '9783161484110' and ID == '8':
                        data_lines[8][5]= ('%d'%(Members_ID))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if Book_ISBN == '9783161484200' and ID == '9':
                        data_lines[9][5]= ('%d'%(Members_ID))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                    if Book_ISBN == '9783161484200' and ID == '10':
                        data_lines[10][5]= ('%d'%(Members_ID))
                        
                        with open('database.txt',mode = 'w') as csv2_FILE:
                                writerow = csv.writer(csv2_FILE, delimiter =',')
                                writerow.writerows(data_lines)
                                csv2_FILE.close
                        
                        
                    Checkout_Date = input("Please enter the date(dd/mm/yyyy): ")
                    print("Thank You")
                    print("ID : %s , Book Title : %s, Member ID : %s, ISBN : %s, Checkout Date : %s" %(ID,books_search,Members_ID,Book_ISBN,Checkout_Date))
                    print("Please remember this information while returning your book")
                    
                    break
    
                   #If all the entries are valid, Book has successfully been checked out and that particular book's assigned Member's ID is the one of the user
                   
                    
                    
                elif Book_ISBN not in line and Members_ID not in mylist:
                    print("Invalid!")
                    break
    elif CheckoutResponse == 'No':
        print("Bye")
    else:
        print("Not a valid response!")
        
        

    
 # below is the test code                   
    
if __name__ == '__main__':
    book_checkout()


    #as the ID number is changed from 0 to some 4 digit value, it indicates that the book unavailable
