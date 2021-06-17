import csv

data = open('database.txt',encoding = 'utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
mylist2 = ['Book_1', 'Book_2', 'Book_1', 'Book_2', 'Book_2', 'Book_3', 'Book_1', 'Book_3', 'Book_4', 'Book_4']
mylist3 = ['1','2','3','4','5','6','7','8','9','10']


def book_return():
    '''
    This function is used to help the librarian to complete the process of returning a book
    First, will ask the user if they want to return a book (Reply with "Yes" or "No")
    any other response will be invalid.
    If user inputs Yes, will next ask for the Member ID of the user, and then the program will check which Book has assigned that Member ID
    Then will ask user to input the present date, Serial number of the book, Cheeckout date, Book title and ISBN.
    After all are valid, the return process will be completed.
    '''
    
    # asks user if they want to return a book
    ReturnResponse = input("Do you want to return a book? ")
    
    #takes MemberID then checks if valid
    if ReturnResponse == 'Yes':
        MemberID = input("Please enter Member's ID: ")
        for i in range(0,11):
                
            if MemberID in data_lines[i][5]:
                print(data_lines[i])
                print("Valid")
                
                
                Return_date = input("Please enter today's date (dd/mm/yyyy): ")
                Book_SerialNo = input("Please enter Serial number of the book: ")
                Checkout_date = input("Please enter the date you checked out: ")
                Book_Title = input("Please enter Book title: ")
                ISBN_Book = input("Please enter ISBN: ")
                if Book_Title in mylist2:
                    print("Valid response")
                    
                # Below is the code that changes the Members ID of the respective book back to 0 to indicate that that respective Book copy is available again
                if Book_SerialNo in mylist3 and ISBN_Book in data_lines[i][1]:
                    if Book_SerialNo =='1':
                        data_lines[1][5]= '0'
                        with open('database.txt',mode = 'w') as csvmy_FILE:
                            writerow = csv.writer(csvmy_FILE, delimiter =',')
                            writerow.writerows(data_lines)
                            csvmy_FILE.close
                                
                    if Book_SerialNo =='2':
                        data_lines[2][5]= '0'
                        with open('database.txt',mode = 'w') as csvmy_FILE:
                            writerow = csv.writer(csvmy_FILE, delimiter =',')
                            writerow.writerows(data_lines)
                            csvmy_FILE.close
                                
                    if Book_SerialNo =='3':
                        data_lines[3][5]= '0'
                        with open('database.txt',mode = 'w') as csvmy_FILE:
                            writerow = csv.writer(csvmy_FILE, delimiter =',')
                            writerow.writerows(data_lines)
                            csvmy_FILE.close
                            
                    if Book_SerialNo =='4':
                        data_lines[4][5]= '0'
                        with open('database.txt',mode = 'w') as csvmy_FILE:
                            writerow = csv.writer(csvmy_FILE, delimiter =',')
                            writerow.writerows(data_lines)
                            csvmy_FILE.close
                                
                    if Book_SerialNo =='5':
                        data_lines[5][5]= '0'
                        with open('database.txt',mode = 'w') as csvmy_FILE:
                            writerow = csv.writer(csvmy_FILE, delimiter =',')
                            writerow.writerows(data_lines)
                            csvmy_FILE.close
                                
                    if Book_SerialNo =='6':
                        data_lines[6][5]= '0'
                        with open('database.txt',mode = 'w') as csvmy_FILE:
                            writerow = csv.writer(csvmy_FILE, delimiter =',')
                            writerow.writerows(data_lines)
                            csvmy_FILE.close
                                
                    if Book_SerialNo =='7':
                        data_lines[7][5]= '0'
                        with open('database.txt',mode = 'w') as csvmy_FILE:
                            writerow = csv.writer(csvmy_FILE, delimiter =',')
                            writerow.writerows(data_lines)
                            csvmy_FILE.close
                                
                    if Book_SerialNo =='8':
                        data_lines[8][5]= '0'
                        with open('database.txt',mode = 'w') as csvmy_FILE:
                            writerow = csv.writer(csvmy_FILE, delimiter =',')
                            writerow.writerows(data_lines)
                            csvmy_FILE.close
                                
                    if Book_SerialNo =='9':
                        data_lines[9][5]= '0'
                        with open('database.txt',mode = 'w') as csvmy_FILE:
                            writerow = csv.writer(csvmy_FILE, delimiter =',')
                            writerow.writerows(data_lines)
                            csvmy_FILE.close
                                
                    if Book_SerialNo =='10':
                        data_lines[10][5]= '0'
                        with open('database.txt',mode = 'w') as csvmy_FILE:
                            writerow = csv.writer(csvmy_FILE, delimiter =',')
                            writerow.writerows(data_lines)
                            csvmy_FILE.close
                                
                    print( "Book returned successfully")
                        
                elif Book_SerialNo not in mylist3:
                    print("Invalid")
                    break
               #Below is the code that adds the details of the loan to the logfile.txt which shows the loan history of the book
                with open(r'logfile.txt', 'a') as csvfile:    
                    newfile = csv.writer(csvfile)
                    newfile.writerow([Book_SerialNo,Book_Title,MemberID,ISBN_Book,Checkout_date,Return_date])
                    print("Thank You!")
                    break
        else:
            print("Not valid")
    elif ReturnResponse == 'No':
        print("Have a good day!")
    else:
        print("Not a valid response")

        # Below is the test code
if __name__ == '__main__':
    book_return()
