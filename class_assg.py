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

class user():
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
    def load_users(self):
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
    
    def del_transaction(bookname=None,username=None,tr_date=None):
        if username == bookname == tr_date == None:
            return 'You MUST include ONE crieteria'
        inFile = open(transactionList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        inFile = open(transactionList, 'w')
        for line in doc:
            if tr_date == username == None and bookname !=None:
                if bookname not in line:
                    inFile.write(line)
            elif tr_date == bookname == None and username !=None:
                if username not in line:
                    inFile.write(line)
            elif bookname == username == None and tr_date !=None:
                if str(tr_date) not in line:
                    inFile.write(line)
            else:
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
       
t1 = Transaction('Advanced Physics','Abhinav',1)
t2=Transaction('FACTs','Bhavin',1)
t3 = Transaction('PS modelling','Gurjeet',0)
t4 = Transaction('Networking principles','Karanbir',1)

t1.add_transaction()
t2.add_transaction()
t3.add_transaction()
t4.add_transaction()



             
# author1 = Author('segun','1992/10/25','Nigerian')            
author = Author.search_author('segun')
#print(type(author))
print(author)























