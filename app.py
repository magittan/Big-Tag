#######################################
# Imports
#######################################
#from flask import Flask
#from flask import render_template
#from flask import request
#from operator import itemgetter
from random import randint
#import json

######################################
# App initialization
#####################################
#app = Flask("Big-Tag")

####################################
# Leaderboard
####################################
class User:
    
    def __init__(self,name,email,code):
        self.name = name
        self.email = email
        self.code = code
        self.taggedUsers= []
        
    def get_code(self): # gets the unique code from the player
        return self.code
    
    def get_name(self): # gets the name from the player
        return self.name
        
    def get_email(self): #gets the email from the player
        return self.email
    
    def get_taggedUsers(self): # gets the tagged Users from the players
        return self.taggedUsers
        
    def update_taggedUsers(self,User): # adds a tag into the list
        self.taggerUsers.add(User)
        

class Game:
    def __init__(self):
        self.inUsers = [] # Game is intialized with inUsers and outUsers
        self.outUsers = []
        
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
    
    def remove_user(self,User,code): #user requests to remove a person
        for user in self.users:
            if (user.get_code()==code):
                self.user
        
    def start_seq(self): # shuffles the array in order to begin playing the game
        self.users.shuffle()
    
    def getTarget(self,User):
        if (User in self.inUsers):
            return self.inUsers[(self.inUsers.index(User)+1)%len(self.inUsers)].get_name()
        else: 
            return "You are Dead"
            
    def get_inUsers(self):
        return self.inUsers
            
g = Game()
g.add_user("jim", "jim.com")
for i in g.get_inUsers():
    print(i.get_name()+" "+i.get_email()+" "+str(i.get_code())
