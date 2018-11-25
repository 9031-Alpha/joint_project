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
        ''' name,nationality (string) : input the name of the book or nationality of the author
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
            age1 = age2 = age
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
    def __add__(self,other):
        self.first_name=other.first_name
        self.last_name=other.last_name
        self.address=other.address
        self.phone=other.phone
        return "First Name:" +other.first_name+" "+"Last Name:" +other.last_name+" "+"Street:" +str(other.address[0])+" "+"City:" +other.address[1]+" "+"Country:" +other.address[2]+" "+"Phone:" +other(self.phone)
    def load_users(self):
        with open(userlist,'r+') as f:
            new_f=f.readlines()
            temp=[]
            for line in new_f:
                if self.first_name:
                    temp=self.first_name+" "+self.last_name
            return temp
            f.close()
    def read_user(self):
        outFile=open(userlist, 'a+')
        outFile.write(self.first_name+','+self.last_name+','+str(self.birth_year)+','+'('+str(self.address[0])+','+self.address[1]+','+self.address[2]+')'+','+str(self.phone)+'\n')
        outFile.close()
    def delete_user(first_name):
        with open(userlist,'r+') as f:
            new_f=f.readlines()
            f.seek(0)
            for line in new_f:
                if first_name not in line:
                    f.write(line)
            f.truncate()
    def search_by_name(first_name):
        with open(userlist,'r') as f:
            new_f=f.readlines()
            #f.seek(0)
            for line in new_f:
                if first_name in line:
                    return line
            f.close()    

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
    
    def del_transaction(self):
        inFile = open(transactionList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        inFile = open(transactionList, 'w')
        for line in doc:
            if self.bookname not in line and self.username not in line and str(self.date_time) not in line:
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





#class Library(Author,Book):
#    def __init__(self):
        




             
# author1 = Author('segun','1992/10/25','Nigerian')            
author = Author.search_author('segun')
#print(type(author))
print(author)























