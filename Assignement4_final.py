from datetime import date,datetime

authorList = 'author.txt'
bookList = 'books.txt'
userlist='User.txt'
transactionList = 'transactions.txt'

''' Assumptions for this assignment
    The text file containing authors must have the following:
        Each authors name must be unique
        Each authors details must be inputted in the order - name,dob(YYYY/MM/DD),nationality
        Each author's details must be in a new line
'''

class Author():
    def __init__(self,name=None,dob=None,nationality=None):
        self.name = name
        self.dob = str(dob)
        self.nationality = nationality
    
    def get_age(self):
        today = date.today()
        datee = self.dob
        datee= datee.split('/')
        year = int(datee[0])
        return today.year - year 
    
    def __str__(self):
        return 'Author info- Name:'+ self.name +' Nationality:'+ self.nationality + ' Age:'+str(self.get_age())
    
    def __add__(self,other):
        ''' other(tuple): updates the atrtibute of the instance of a class 
        '''
        
        Author.__init__(self,name=None,dob=None,nationality=None)
        self.name = other[0]
        self.dob = other[1] 
        self.nationality = other[2]
        
    def load_authors():
        inFile = open(authorList, 'r')    
        doc = inFile.readlines()
        author_list = [x.strip() for x in doc]
        return author_list
    
    def author_to_text(self):
        ''' adds the details of an author to the text file
        the code is run as a method of the instance '''
        
        file = open('author.txt','a')
        file.write(self.name+','+self.dob+','+self.nationality +'\n')
          
    def del_author(name):
        inFile = open(authorList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        inFile = open(authorList, 'w')
        for line in doc:
            if name not in line:
                inFile.write(line)
        inFile.close()
        
    def search_author(name):
        ''' name(string) of the author to be searched. This function returns 
        an object of the author. This function has to be called as a method of 
        the class when used outside the class '''
        
        inFile = open(authorList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        for line in doc:
            if name in line:
                break
        #return Author(name=line[:-1])
        line=line.split(',')
        return Author(name=line[0],dob=line[1],nationality=line[2])
    
    def search_by_nationality(nationality):
        inFile = open(authorList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        temp = []
        for line in doc:
            if nationality in line:
                pos = line.find(',')
                temp.append(line[:pos])
        return temp

    def search_by_age(age1,age2):
        '''age1,age2(integers): the upper and lower limit of age to search for.
        The function returns a list of all authors in the range ''' 
        if age1 > age2:
            (age1,age2) = (age2,age1) # this condition allows the user to search by inputting either the upper or lower limit first
            
        inFile = open(authorList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        temp = []
        for line in doc:
            line=line.split(',')
            author = Author(name=line[0],dob=line[1],nationality=line[2])
            age = author.get_age()
            if age >= age1 and age <= age2:
                temp.append(line[0])
        if temp == []:
            return 'No Author available in this age range'
        else:
            return temp

    
class Book():               # MUST input all attributes unlike author class
    def __init__(self,book_name=None,author_name=None,publisher_name=None):
        self.book_name = book_name
        self.author_name = author_name
        self.publisher_name = publisher_name
        self.profile = Author.search_author(author_name)
    
    def __str__(self):
        return 'Book Info- Book Name:'+ self.book_name +' Publisher:'+ self.publisher_name + ' Author Name:'+ self.author_name + ' Author Nationality:'+ self.profile.nationality
     
    def __add__(self,other):      
        self.book_name = other[0]
        self.author_name = other[1]
        self.publisher_name = other[2]     
        self.profile = Author.search_author(other[1])
        
    def load_books():
        inFile = open(bookList, 'r')    
        doc = inFile.readlines()
        book_list = [x.strip() for x in doc]
        return book_list
    
    def book_to_text(self):
        file = open('books.txt','a')
        file.write(self.book_name+','+self.author_name+','+self.publisher_name +'\n')
        
    def del_book(name):
        inFile = open(bookList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        inFile = open(bookList, 'w')
        for line in doc:
            if name not in line:
                inFile.write(line)
        inFile.close()
        
    def search_book(name):
        ''' name(string) of the book to be searched. This function returns 
        the details of the book. This function has to be called as a method of 
        the class when used outside the class '''
        
        inFile = open(bookList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        for line in doc:
            if name in line:
                break
        line=line.split(',')
        return Book(book_name=line[0],author_name=line[1],publisher_name=line[2])
    
    def search_by_author(name=None, nationality=None, age=None):
        ''' name,nationality (string) : input the name of the author or nationality of the author
            age (int): input the age of the author
            function returns a list of books that fit the crieteria '''
            
        inFile = open(bookList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        temp = []
        if name != None:
            for line in doc:   # Review the search conditions 
                if name in line:
                    pos = line.find(',')
                    temp.append(line[:pos])
        if nationality != None:
            name = Author.search_by_nationality(nationality)
            for line in doc:
                for line2 in name:
                    if line2 in line:
                        pos = line.find(',')
                        if line[:pos] not in temp:
                            temp.append(line[:pos])
        if age != None:
            age1 = age2 = int(age)
            name = Author.search_by_age(age1,age2)
            for line in doc:
                for line2 in name:
                    if line2 in line:
                        pos = line.find(',')
                        if line[:pos] not in temp:
                            temp.append(line[:pos])

        return temp

class user:
    def __init__(self,first_name=None,last_name=None,birth_year=None,address=None,phone=None):
        self.first_name=first_name
        self.last_name=last_name
        self.birth_year=birth_year
        self.address=address
        self.phone=phone
    def age(self):
        return date.today().year-self.birth_year
    def __str__(self):
        return "First Name:" +self.first_name+" "+"Last Name:" +self.last_name+" "+"User Age:" +str(self.age())+" "+"City:" +self.address[1]+" "+"Country:" +self.address[2]+" "+"Phone:" +str(self.phone)
    # To test the above part of the code use the following example data:
    # user1=user('Abhinav','Nanda',1990,(140,'Whitby','Canada'),9051112222)
    #print(user1)
    def __add__(self,other):
        #user.__init__(self,first_name=None,last_name=None,birth_year=None,address=None,phone=None)
        self.first_name=other.first_name
        self.last_name=other.last_name
        self.address=other.address
        self.phone=other.phone
        return "First Name:" +other.first_name+" "+"Last Name:" +other.last_name+" "+"Street:" +str(other.address[0])+" "+"City:" +other.address[1]+" "+"Country:" +other.address[2]+" "+"Phone:" +str(other.phone)
    # To test the above part of the code use the following example data:
    # user1=user('Abhinav','Nanda',1990,(140,'Whitby','Canada'),9051112222)
    #other=user('Pandu','Nand',1980,(40,'Whillyby','Canada'),9051111111)
    #user1+other
    def load_users():
        inFile = open(userlist, 'r')    
        doc = inFile.readlines()
        user_list = [x.strip() for x in doc] # Removes the next line characters from each line
        return user_list
    # To test the above part of the code use the following code:
    # user().load_users()
    def read_user(self):
        outFile=open(userlist, 'a+')
        outFile.write(self.first_name+','+self.last_name+','+str(self.birth_year)+','+'('+str(self.address[0])+','+self.address[1]+','+self.address[2]+')'+','+str(self.phone)+'\n')
        outFile.close()
    # To test the above part of the code use the following example data:
    #add=user('Pandu','Nand',1980,(40,'Whillyby','Canada'),9051111111)
    #user.read_user(add)
    def delete_user(first_name):
        with open(userlist,'r+') as f:
            new_f=f.readlines()
            f.seek(0)
            for line in new_f:
                if first_name not in line:
                    f.write(line)
            f.truncate()
    #user.delete_user('Pandu')
    def search_by_name(first_name):
        with open(userlist,'r') as f:
            new_f=f.readlines()
            f.seek(0)
            for line in new_f:
                if first_name in line:
                    return line[:-1]
            f.close()
    def search_by_info(city=None,phone=None,last_name=None): #input phone number as string
        with open(userlist,'r') as f:
            new_f=f.readlines()
            temp=[]
            f.seek(0)
            if city!=None:
                for line in new_f:
                    if city in line:
                        pos = line.find(',')
                        if line[:pos] not in temp:
                            temp.append(line[:pos])
                return temp
            if str(phone)!=None:
                    for line in new_f:
                        if str(phone) in line:
                            pos=line.find(',')
                            if line[:pos] not in temp:
                                temp.append(line[:pos])
                        return temp
            if last_name!=None:
                    for line in new_f:
                        if last_name in line:
                            pos=line.find(',')
                            if line[:pos] not in temp:
                                temp.append(line[:pos])
                        return temp
            if city and str(phone)!=None:
                for line in new_f:
                    for line in new_f:
                        if city and str(phone) in line:
                            pos=line.find(',')
                            if line[:pos] not in temp:
                                temp.append(line[:pos])
                return temp
            if city and last_name!=None:
                for line in new_f:
                    for line in new_f:
                        if city and str(phone) in line:
                            pos=line.find(',')
                            if line[:pos] not in temp:
                                temp.append(line[:pos])

                return temp  


class Transaction():
    def __init__(self,bookname=None,username=None,t_type=None):
        self.bookname = str(bookname)
        self.username = username
        self.date_time = datetime.now()
        self.t_type = int(t_type)
    
    def load_transactions():
        inFile = open(transactionList, 'r')    
        doc = inFile.readlines()
        transaction_list = [x.strip() for x in doc]
        return transaction_list
    
    def add_transaction(self):
        file = open(transactionList,'a+')
        file.write(self.bookname+','+self.username+','+str(self.date_time) +','+str(self.t_type)+'\n')
    
    def del_transaction(bookname = None,username = None, timedate= None):
        inFile = open(transactionList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        inFile = open(transactionList, 'w')
        for line in doc:
            if bookname not in line and username not in line and str(timedate) not in line:
                inFile.write(line)
        inFile.close()
        
    def search_transaction(tr_date=None, username=None, bookname=None):
        inFile = open(transactionList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        temp = []
        if tr_date != None:
            for line in doc:
                if str(tr_date) in line:
                    temp.append(line[:-1])
        if username != None:
            for line in doc:
                if username in line and line[:-1] not in temp:
                    temp.append(line[:-1])
        if bookname != None:
            for line in doc:
                if bookname in line and line[:-1] not in temp:
                    temp.append(line[:-1])
        return temp





class Library(Author,Book,user,Transaction):
    def __init__(self,name):
        self.name = name
        self.userlist= user.load_users()
        self.authorlist = Author.load_authors()
        self.booklist = Book.load_books()
        self.tranlist = Transaction.load_transactions()
        self.dictn = Library.show_book_name()
    
   
        
    def show_book_name():
        dictn= {}
        books= Book.load_books()
        for item in books:
            item_list = item.split(',')
            dictn[item_list[0]] = 4
        transac = Transaction.load_transactions()
        for item in transac:
            item_list = item.split(',')
            t_type = item_list[-1]
            if t_type == '1':
               dictn[item_list[0]] -= 1
            elif t_type == '0':
                dictn[item_list[0]] += 1
            
        return dictn
        

    def borrow_book(bookname = None, username=None):
        transac= Transaction(bookname,username,1)
        transac.add_transaction()

    def return_book(bookname=None, username=None):
        transac=Transaction(bookname,username,0)
        transac.add_transaction()
    
    def show_book_authorname(author_name):
        bookname = Book.search_by_author(name = author_name)[0]
        lib = Library.show_book_name()
        if bookname in lib:
            available = lib[bookname]
        return bookname + ': ' + str(available)
    
    def show_book_nationality(author_nationality):
        bookname = Book.search_by_author(nationality = author_nationality)
        lib = Library.show_book_name()
        available ={}
        for i in bookname:
            if i in lib:
                available[i] = lib[i]
        return available
    
    def borrowed_book(username):
        transac = Transaction.load_transactions() #transList
        book=[]
        for item in transac:
            item_list = item.split(',')
            if item_list[1] == username:
                book.append(item_list[0])
        return book      
        
    def borrowed_book_phone(phone):     #phone number has to be entered as a string
        name = user.search_by_info(phone)
        transac = Transaction.load_transactions() #transList
        book=[]
        for item in transac:
            item_list = item.split(',')
            if item_list[1] == name[0]:
                book.append(item_list[0])
        return book

    
    def main_menu():
        '''
        This function creates an interactive interface with menus and submenus
        '''
        while(1):
            
            menu ={}
            menu['i'] = 'AUTHORS'
            menu['ii']=  'BOOKS'
            menu['iii'] = 'USERS'
            menu['iv']='LIBRARY'
            menu['v'] = 'EXIT'
            print(menu)
            access = input('Make a selection from above list: ')
            if access == 'i':
                print('AUTHOR FUNCTIONS')
                submenu={}
                submenu[1] = 'ADD'
                submenu[2] = 'UPDATE'
                submenu[3] = 'DELETE'
                submenu[4] = 'SEARCH BY NAME'
                submenu[5] = 'SEARCH BY AGE'
                submenu[6] = 'SEARCH BY NATIONALITY'
                print(submenu)
                acc = int(input('Make a selection from above list: '))
                if acc == 1:
                    name= input('Enter name of author: ')
                    dob=input('Enter dob of author: ')
                    nationality=input('Enter nationality of author: ')
                    C = Author(name,dob,nationality)
                    C.author_to_text()
                if acc == 2:        # not yet
                    name= input('Enter name of author: ')
                    dob=input('Enter dob of author: ')
                    nationality=input('Enter nationality of author: ')
                    other = (name,dob,nationality)
                    Author.__add__(other)
                if acc == 3:
                    name = input('Enter name of author you want to delete: ')
                    Author.del_author(name)
                if acc == 4:
                    name =input('Enter name of author you want to search: ')
                    print(Author.search_author(name))
                if acc == 5:
                    age1 =int(input('Enter lower age limit of author you want to search: '))
                    age2 =int(input('Enter upper age limit of author you want to search: '))
                    print(Author.search_by_age(age1,age2))
                if acc == 6:
                    nationality = input('Enter nationality of author you want to search: ')
                    print(Author.search_by_nationality(nationality))
                    
            if access == 'ii':
                print('BOOK FUNCTIONS')
                submenu={}
                submenu[1] = 'ADD'
                submenu[2] = 'UPDATE'
                submenu[3] = 'DELETE'
                submenu[4] = 'SEARCH BY NAME'
                submenu[5] = 'SEARCH BY AUTHOR NAME OR NATIONALITY'
                print(submenu)
                acc = int(input('Make a selection from above list: '))
                if acc == 1:
                    bookname= input('Enter name of book: ')
                    authorname=input('Enter name of author: ')
                    publishername=input('Enter name of publisher: ')
                    C = Book(bookname,authorname,publishername)
                    C.book_to_text()
                if acc == 2:        # not yet
                    bookname= input('Enter name of book: ')
                    authorname=input('Enter name of author: ')
                    publishername=input('Enter name of publisher: ')
                    other = (bookname,authorname,publishername)
                    Book.__add__(other)
                if acc == 3:
                    name = input('Enter name of book you want to delete: ')
                    Book.del_book(name)
                if acc == 4:
                    name =input('Enter name of book you want to search: ')
                    b=Book.search_book(name)
                    print(b)
                if acc == 5:
                    a_name =input('Enter name of author: ')
                    a_nationality = input('Enter nationality of author: ')
                    a_age = input('Enter age of author: ')
                    if a_name == '':
                        a_name = None
                        #print(Book.search_by_author(name = a_name)) 
                    if a_nationality == '':
                        a_nationality = None
                        print(Book.search_by_author(nationality = a_nationality))
                    if a_age == '':
                        a_age = None
                    print(Book.search_by_author(a_name,a_nationality,a_age))
                   
            if access == 'iii':
                print('USER FUNCTIONS')
                submenu={}
                submenu[1] = 'ADD'
                submenu[2] = 'UPDATE'
                submenu[3] = 'DELETE'
                submenu[4] = 'SEARCH BY NAME'
                submenu[5] = 'SEARCH BY CITY'
                print(submenu)
                acc = int(input('Make a selection from above list: '))
                if acc == 1:
                    first_name= input('Enter user first name: ')
                    last_name=input('Enter user last name: ')
                    birth_year = int(input('Enter your birth year: '))
                    temp = input('Enter your address in format- number city country: ')
                    temp1= temp.split(' ')
                    address = (int(temp1[0]),temp1[1],temp1[2])
                    phone = input('Enter phone number: ')
                    c = user(first_name,last_name,birth_year,address,phone)
                    c.read_user()
                if acc == 2:        # not yet
                    first_name= input('Enter user first name: ')
                    last_name=input('Enter user last name: ')
                    birth_year=int(input('Enter user last name: '))
                    (address)=input('Enter user address: ')
                    phone=input('Enter user phone number: ')
                    other = user(first_name,last_name,birth_year,address,phone)
                    other.read_user()
                if acc == 3:
                    first_name = input ('Enter first name of user you want to delete: ')
                    user.delete_user(first_name)
                if acc == 4:
                    first_name = input('Enter first name of user you want to search: ')
                    print(user.search_by_name(first_name))
                if acc == 5:
                    u_city = input('Enter city of user you want to search: ')
                    print(user.search_by_info(u_city))
            
            
        
            if access == 'iv':
                print('LIBRARY EXCHANGE')
                submenu={}
                submenu[1] = 'BORROW BOOK'
                submenu[2] = 'RETURN BOOK'
                submenu[3] = 'SHOW BOOK AVAILABILITY BY NAME'
                submenu[4] = 'SHOW BOOK AVAILABILITY BY AUTHOR NAME'
                submenu[5] = 'SHOW BOOK AVAILABILITY BY AUTHOR NATIONALITY'
                submenu[6] = 'SHOW BORROWED BOOK BY USERNAME'
                submenu[7] = 'SHOW BORROWED BOOK BY PHONE'
                print(submenu)
                acc = int(input('Make a selection from above list: '))
                if acc == 1:
                    user1 = input('Enter your username: ')
                    book = input('Enter book name you want to borrow: ')
                    Library.borrow_book(bookname=book, username=user1)
                if acc == 2:
                    user1 = input('Enter user name: ')
                    book = input('Enter name of book being returned: ')
                    Library.return_book(bookname=book,username=user1)
                if acc == 3:
                    print( 'Books available and the quantities are: ')
                    print(Library.show_book_name())
                if acc == 4:
                    author_name = input ('Enter author of the book to check for availability: ')
                    print(Library.show_book_authorname(author_name))
                if acc == 5:
                    author_nationality = input ('Enter nationality of the author of the book you want: ')
                    print(Library.show_book_nationality(author_nationality))
                if acc == 6:
                    user1 = input('Enter the username: ')
                    print(Library.borrowed_book(user1))
                if acc == 7:
                    phone = input('Enter phone number of user: ')
                    print(Library.borrowed_book_phone(phone))
            if access == 'v':
                print('THANK YOU!!!')
                break
           
        
            
            


Library.main_menu()
#t1 = Transaction('Advanced Physics','Abhinav',1)
#t2=Transaction('FACTs','Bhavin',1)
#t3 = Transaction('PS modelling','Gurjeet',0)
#t4 = Transaction('Networking principles','Karanbir',1)

#t1.add_transaction()
#t2.add_transaction()
#t3.add_transaction()
#t4.add_transaction()



             
# author1 = Author('segun','1992/10/25','Nigerian')            
#author = Author.search_author('segun')
#print(type(author))
#print(author)























