from datetime import date,datetime

authorList = 'author.txt'
bookList = 'books.txt'
transactionList = 'transactions.txt'


class Author():
    def __init__(self,name=None,dob=None,nationality=None):
        self.name = str(name)
        self.dob = str(dob)
        self.nationality = str(nationality)
    
    def get_age(self):
        today = date.today()
        datee = self.dob
        datee= datee.split('/')
        year = int(datee[0])
        
        return today.year - year 
    
    def __str__(self):
        return 'Author info- Name:'+ self.name +' Nationality:'+ self.nationality + ' Age:'+str(self.get_age())
    def __add__(self,other):
        self.name = other.name
        self.dob = other.dob
        self.nationality = other.nationality
        return Author(self.name,self.dob,self.nationality)
        
    def load_authors():
        inFile = open(authorList, 'r')    
        doc = inFile.readlines()
        author_list = [x.strip() for x in doc]
        return author_list
    
    def author_to_text(self):
        file = open('author.txt','a')
        file.write(self.name+','+self.dob+','+self.nationality +'\n')
          
    def del_author(name):
        inFile = open(authorList, 'r')    
        doc = inFile.readlines()
        print (doc)
        inFile.close()
        inFile = open(authorList, 'w')
        for line in doc:
            if name not in line:
                inFile.write(line)
        inFile.close()
        
    def search_author(name):
        ''' name(string) of the author to be searched. This function returns 
        the details of the author. This function has to be called as a method of 
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
        return Author(temp)
    
a = Author('mohamed','1993/1/1','egyptian')
b = Author('fahmy','1993/1/1','canadian')
c=a+b
print(a)
print(c)
c.author_to_text()


    
class Book():
    def __init__(self,book_name=None,author_name=None,publisher_name=None):
        self.book_name = str(book_name)
        self.author_name = str(author_name)
        self.publisher_name = str(publisher_name)
        self.author = Author.search_author(author_name)
    
    def __str__(self):
        return 'Book Info- Book Name:'+ self.book_name +' Publisher:'+ self.publisher_name + '\n'+ self.author.__str__()+'\n'
    
    def __add__(self,other):
        self.book_name = other.book_name
        self.author_name = other.author_name
        self.publisher_name = other.publisher_name
        return Book(self.book_name,self.author_name,self.publisher_name)
        
    def load_books():
        inFile = open(bookList, 'r')    
        doc = inFile.readlines()
        book_list = [x.strip() for x in doc]
        return book_list
    
    def book_to_text(self):
        file = open('books.txt','w+')
        file.write(self.book_name+','+self.author_name+','+self.publisher_name +'\n')
        
    def del_book(name):
        inFile = open(bookList, 'r')    
        doc = inFile.readlines()
        print (doc)
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
        inFile = open(bookList, 'r')    
        doc = inFile.readlines()
        inFile.close()
        temp = []
        if name != None:
            for line in doc:
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
            name = Author.search_by_age(age)
            for line in doc:
                for line2 in name:
                    if line2 in line:
                        pos = line.find(',')
                        if line[:pos] not in temp:
                            temp.append(line[:pos])
        return temp
    

a = Book('circuits','mohamed','company1')
b = Book('circuits','fahmy','company2')
c=a+b
print(a)
print(c)

author = Author.search_author('segun')
print(type(author))
print(author)


class Transaction():
    def __init__(self,bookname=None,username=None,t_type=None):
        self.bookname = str(bookname)
        self.username = str(username)
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
    
x1 = Transaction('physics','mohamed',1)
x2 = Transaction('chemistry','ahmed',0)
x3 = Transaction('english','omar',1)
x4 = Transaction('math','youssef',0)
print(x1)
print(x2)
x1.add_transaction()
x2.add_transaction()
x3.add_transaction()
x4.add_transaction()
print(Transaction.load_transactions())
y = Transaction.search_transaction(username='mohamed')
print(y)
x1.del_transaction()
print(Transaction.load_transactions())

















