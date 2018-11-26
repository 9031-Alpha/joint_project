# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:19:16 2018

@author: Mohamed Omer Airaj
"""

authorlist='Authors.txt'
userlist='User.txt'
#def load_words():
#    """
 #   Returns a list of valid words. Words are strings of lowercase letters.
    
  #  Depending on the size of the word list, this function may
   # take a while to finish.
    #"""
 #   print("Loading word list from file...")
    # inFile: file
  #  inFile = open(Wordlist_filename, 'r+')
    # line: string
   # line = inFile.read()
    # wordlist: list of strings
    #wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    #return wordlist

#wordlist=load_words()

from datetime import date
class author:
    def __init__(self,name=None,date_of_birth=None,nationality=None):
        self.name=name
        self.date_of_birth=date_of_birth
        self.nationality=nationality
    def age(self):
        return date.today().year-self.date_of_birth[0]
    def __str__(self):
        return "Author Name:" +self.name+" "+ "Nationality:" +self.nationality+" "+"Age:" +str(self.age())
    def __add__(self,other):
        self.name=other.name
        self.nationality=other.nationality
        self.date_of_birth=other.date_of_birth
        return "Author Name:" +other.name+" "+ "Nationality:" +other.nationality+" "+"Date of Birth:" +str(other.date_of_birth)
    def get_info(self):
        outFile=open(authorlist, 'a+')
        outFile.write('\n'+self.name+','+str(self.date_of_birth)+','+self.nationality)
        outFile.close()
    def del_info(self):
        with open(authorlist,'r+') as f:
            new_f=f.readlines()
            f.seek(0)
            for line in new_f:
                if self.name not in line:
                    f.write(line)
            f.truncate()
    def search_authname(name):
        with open(authorlist,'r') as f:
            new_f=f.readlines()
            #f.seek(0)
            for line in new_f:
                if name in line:
                    return line
            f.close()
    def search_authnation(nationality):
        with open(authorlist,'r') as f:
            new_f=f.readlines()
            temp=[]
            for line in new_f:
                if nationality in line:
                    pos=line.find(',')
                    temp.append(line[:pos])
            return temp
            f.close()
                    

#author1=author("Zara",(1975,12,11),"Indian")
#author2=author("Tara",(1988,11,11),"Italian")

class book(author):
    def __init__(self,name,author,publisher):
        self.name=name
        self.author=author
        self.publisher=publisher
    def __str__(self):
        return "Book Name:" +self.name+" "+"Publisher:" +self.publisher+" "+"Author Name:" +self.author+" "+"Nationality:" +self.country()
    def country(self):
        return str()
    def __add__(self,other):
        self.name=other.name
        self.author=other.author
        self.publisher=other.publisher
        return "Book Name:" +other.name+" "+"Publisher:" +other.publisher+" "+"Author Name:" +other.name

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