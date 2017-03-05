#######################################
# Imports
#######################################
from flask import Flask
from flask import render_template
from flask import request
#from operator import itemgetter
from random import randint
from random import shuffle
from random import choice
import datetime
import pyrebase
#import json

######################################
# App initialization
#####################################
#app = Flask("Big-Tag")

####################################
# Leaderboard
####################################

####################################
# DATABASE
####################################



##############################################################################
class User:
    
    def __init__(self,name,email,code):
        self.name = name
        self.code = code
        self.taggedUsers= []
        self.timeOfTag
        self.locOfTag

##############################################################################
#Eventually can be replaced with calls to a User in the Data base
    def get_code(self): # gets the unique code from the player
        return self.code
    
    def get_name(self): # gets the name from the player
        return self.name
        
    def get_email(self): #gets the email from the player
        return self.email
##############################################################################

    def get_taggedUsers(self): # gets the tagged Users from the players
        return self.taggedUsers
        
    def update_taggedUsers(self,User): # adds a tag into the list
        self.taggedUsers.append(User)
    
    def update_TOD(self):
        self.timeOfTag = datetime.datetime.now()
        self.locOfTag = 
    
    def get_userinfo(self):
        return self.name + " " + self.email + " " + str(self.code)
        

class Game:
    def __init__(self):
        self.inUsers = [] # Game is intialized with inUsers and outUsers
        self.outUsers = []
        self.data = Data()
        
    def add_user(self,name,email): # new user is added
        tempCode = randint(1000000,9999999)
        check = True
        while (check):# used in order to check that all the codes are unique
            temp=0
            for user in self.inUsers: 
                if not (user.get_code() == tempCode):
                    temp+=1
            if (temp == len(self.inUsers)):
                check=False
        newUser = User(name,email,tempCode)
        self.inUsers.append(newUser)
        return newUser
    
    def remove_user(self,User,code): #user requests to remove a person
        for user in self.inUsers:
            if (user.get_code()==code):
                self.outUsers.append((self.inUsers.pop(self.inUsers.index(user))))
                user.
                User.update_taggedUsers(user)
                return True
        return False
        
    def start_seq(self): # shuffles the array in order to begin playing the game
        shuffle(self.inUsers)
    
    def get_targetName(self,user):
        if (user in self.inUsers):
            return self.inUsers[(self.inUsers.index(user)+1)%len(self.inUsers)].get_name()
        else: 
            return "You are Dead"
            
    def get_target(self,user):
        if (user in self.inUsers):
            return self.inUsers[(self.inUsers.index(user)+1)%len(self.inUsers)]
        else: 
            return "You are Dead"
            
    def get_inUsers(self):
        return self.inUsers
        
####################################################################     

class Data:
    def __init__(self):
        
        
        
        
g = Game()
for i in range(50):
    print(g.add_user(str(i), str(i)+"@gmail.com").get_userinfo())
g.start_seq()
for user in g.get_inUsers():
    print(user.get_name()+" "+g.get_targetName(user))
for i in range(20):
    tagger = choice(g.get_inUsers())
    g.remove_user(tagger,g.get_target(tagger).get_code())
    print(len(g.get_inUsers()))
