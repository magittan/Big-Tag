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
import json
import requests

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

class Database:
    def __init__(self):
        config = {
          "apiKey": "AIzaSyB3UTG878t8nyfUiw8zIhfyqb5Pqwp7S2I",
          "authDomain": "thebigtag-135f2.firebaseapp.com",
          "databaseURL": "https://thebigtag-135f2.firebaseio.com/",
          "storageBucket": "thebigtag-135f2.appspot.com"
        }

        self.firebase = pyrebase.initialize_app(config)
        self.auth = self.firebase.auth()
        
    def register(self,name,email,password):        
        register = self.auth.create_user_with_email_and_password(email, password)
        #if "'registered': True" in register.text:
        #    self.logger.info("Registration suceeded!")
        #else:
        #    self.logger.info("Registration failed.")

        # Get a reference to the database service
        db = firebase.database()
        # data to save
        data = {
            "name":name, "email":email, "password": password
        }
        # Pass the user's idToken to the push method
        results = db.child("users").push(data)

    def pull_username(self,key):
        return db.child("users").child(key).get()["name"]
    
    def pull_password(self,key):
        return db.child("users").child(key).get()["password"]

    def pull_email(self,key):
        return db.child("users").child(key).get()["email"]
        
    def login(self,email,password):    
        user = self.auth.sign_in_with_email_and_password(email, password)
    
    def refreshtoken(self):
        # Refreshes the user's idToken in order to keep their session alive, kept open for 30 minutes
        user = self.auth.refresh(user['refreshToken'])
    
    def pullAllKeys(self): # we are going to intialized the game with everyone playing
        return db.child("users").get() #unsure if this works
    


##############################################################################
class User:
    
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.taggedUsers= []
        self.timeOfTag
        self.locOfTag

##############################################################################
#Eventually can be replaced with calls to a User in the Data base
    def get_code(self): # gets the unique code from the player
        return self.code
    
    def get_name(self): # gets the KEY from the player
        return self.name
        
##############################################################################

    def get_taggedUsers(self): # gets the tagged Users from the players
        return self.taggedUsers
        
    def update_taggedUsers(self,User): # adds a tag into the list
        self.taggedUsers.append(User)
    
    def update_TOD(self):
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        coords = [lat,lon]

        self.timeOfTag = datetime.datetime.now()
        self.locOfTag = coords
    
    def get_userinfo(self):
        # rewrite
        

class Game: # THE GAME WILL OPERATE ENTIRELY OFF OF KEYS, INFORMATION WILL BE GATHERED BASED ON KEYS
    def __init__(self, inKeys):
        self.inUsers = [] # Game is intialized with inUsers and outUsers
        self.outUsers = []
        for key in inKeys:
            self.add_user(key)
        
    def add_user(self,name): # new user is added
        tempCode = randint(1000000,9999999)
        check = True
        while (check):# used in order to check that all the codes are unique
            temp=0
            for user in self.inUsers: 
                if not (user.get_code() == tempCode):
                    temp+=1
            if (temp == len(self.inUsers)):
                check=False
        newUser = User(nametempCode)
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
            
    def get_inUsers(self):
        return self.inUsers
        
        
#got to create some people first
BigTag = Database()
BigTag.register("Jim","Jim@gmail.com","1999jm")
BigTag.register("Serena","Sim@gmail.com","1999Sm")
BigTag.register("Pip","puck@gmail.com","1999Pm")



g = Game([])
for i in range(50):
    print(g.add_user(str(i), str(i)+"@gmail.com").get_userinfo())
g.start_seq()
for user in g.get_inUsers():
    print(user.get_name()+" "+database.pull_username(g.get_targetName(user)))
for i in range(20):
    tagger = choice(g.get_inUsers())
    g.remove_user(tagger,g.get_target(tagger).get_code())
    print(len(g.get_inUsers()))
