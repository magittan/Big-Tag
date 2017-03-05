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
        self.db = self.firebase.database()
        self.yourKey = 0
        
    def register(self,name,email,password,interest):        
        self.auth.create_user_with_email_and_password(email, password)
        #if "'registered': True" in register.text:
        #    self.logger.info("Registration suceeded!")
        #else:
        #    self.logger.info("Registration failed.")

        # Get a reference to the database service
        
        # data to save
        data = {
            "name":name, "email":email, "password": password, "interest": interest
        }
        # Pass the user's idToken to the push method
        self.db.child("users").push(data)
        
    def pull_username(self,key):
        return self.db.child("users").child(key).get().val()["name"]
    
    def pull_password(self,key):
        return self.db.child("users").child(key).get().val()["password"]

    def pull_email(self,key):
        return self.db.child("users").child(key).get().val()["email"]

    def pull_interest(self,key):
        return self.db.child("users").child(key).get().val()["interest"]
        
        
    def login(self,email,password): # no error check  
        for i in range(len(self.pullAllEmails())):
            if (email.lower()==self.pullAllEmails()[i].lower()):
                if (password==self.pullAllPasswords()[i]):
                    self.yourKey = str(self.pullAllKeys()[i])
                    return self.yourKey
                else:
                    return 0
                    #this is an error - error message/ wrong password
    
    def logout(self):
        self.yourKey=0 # no error check
        
    #def refreshtoken(self):
    #   # Refreshes the user's idToken in order to keep their session alive, kept open for 30 minutes
    #   self.auth.refresh(user['refreshToken'])
    
    def pullAllKeys(self): # we are going to intialized the game with everyone playing
        output = []
        for user in self.db.child("users").get().val().keys():
            output.append(str(user))
        return output
        
    def pullAllEmails(self):
        output = []
        for e in self.db.child("users").child().get().each():
            output.append(str(e.val()["email"]))
        return output
        
    def pullAllNames(self): # we are going to intialized the game with everyone playing
        output = []
        for e in self.db.child("users").child().get().each():
            output.append(str(e.val()["name"]))
        return output
        
    def pullAllPasswords(self):
        output = []
        for e in self.db.child("users").child().get().each():
            output.append(str(e.val()["password"]))
        return output
        
    def pullAllInterests(self):
        output = []
        for e in self.db.child("users").child().get().each():
            output.append(str(e.val()["interest"]))
        return output
        
    def get_userkey(self):
        print(self.yourKey)

##############################################################################
class User:
    
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.taggedUsers= []
        self.timeOfTag = str(datetime.datetime.now())
        self.locOfTag = [0,0]

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

        self.timeOfTag = str(datetime.datetime.now())
        self.locOfTag = coords
    
    def get_TOT(self):
        return self.timeOfTag
        
    def get_TOL(self):
        return self.locOfTag
        
    def get_userinfo(self,Database):
        return Database.pull_username(self.name)
        

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
        newUser = User(name, tempCode)
        self.inUsers.append(newUser)
        return newUser
    
    def remove_user(self,User,code): #user requests to remove a person
        for user in self.inUsers:
            if (user.get_code()==code):
                self.outUsers.append((self.inUsers.pop(self.inUsers.index(user))))
                user.update_TOD()
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
    
    def get_TOT(self): 
        output = []
        for user in self.outUsers:
            output.append(user.get_TOT())
    
    def get_TOL(self): 
        output = []
        for user in self.outUsers:
            output.append(user.get_TOL)

    def get_user(self,name):
        for user in self.inUsers:
            if (user.get_name==name):
                return user
        
personalKey = 0
#got to create some people first
BigTag = Database()
#BigTag.register("Jim","Jimdasd@lsajlkalgmail.com","1999jm","Boats")
#BigTag.register("Serena","Simasda@slkgmail.com","1999Sm","Ships")
#BigTag.register("Pip","puckaskjh@asdgmail.com","1999Pm","Planes")
#BigTag.register("Ben","bealdskj@asdgmail.com","1999Bm","Trees")
#BigTag.register("Leith","Ladiuwd@asdgmail.com","1999LEm","Math")
#BigTag.register("Lucas","Cssasdaijh@asdgmail.com","1999LAm","Bunnies")


#BigTag.register("Demi","Cssaw66qoiedoijh@asdgmail.com","1999aKSVHJ","Songs")
#BigTag.register("Beyonce","Cqw55owdioassdoijh@asdgmail.com","1999aSHBasdkm","Beyonce")
#BigTag.register("Kanye","Cssdo44ijh@asdgmail.com","1999ADIAUSVm","Kanye Kanye Kanye mememe")
#BigTag.register("John","Css33doijh@asdgmail.com","1999KSBm","CHESSE")
#BigTag.register("Uncle Same","Cssd22oijh@asdgmail.com","1999akjbdaAm","CHGSEESE")
#BigTag.register("The Spiciest Memelord","Css11doijh@asdgmail.com","1999asduiAm","SHEESCHE")
#BigTag.register("Pupper","Cssdo89ijh@asdgmail.com","1999asdkjacbm","CHEEESEEY")
#BigTag.register("Thelegend27","Css67doijh@asdgmail.com","1999asdms","CHEESYSS")
#BigTag.register("Harambe","Cssdo45ijh@asdgmail.com","1999Lasdibn","CHEEYSE")
#BigTag.register("Rick Astley","Cssdsd2oijh@asdgmail.com","1999asbao","CHEYSS")
#BigTag.register("Fermat","Cssddas233d@gmail.com","1999LASDAAA","CSHYES")
#BigTag.register("Hawking","Cssds777dijh@asdgmail.com","1999LAasaka","CCHYEEEs")
username = "Lucas"
email = "Cssdoijh@asdgmail.com"
password = "1999LAm"
interest = "Bunnies"
loginEmail = "Cssdoijh@asdgmail.com"
loginPassword = "1999LAm"
#BigTag.register(username,email,password,interest)

g = Game(BigTag.pullAllKeys())
print(BigTag.pullAllNames()) #database of names
print(BigTag.pullAllEmails())
print(BigTag.pullAllPasswords())
print(BigTag.pullAllInterests())
print(BigTag.pullAllKeys())
BigTag.login(loginEmail,loginPassword)
you = g.get_user(BigTag.get_userkey())
print(BigTag.get_userkey()) #player key
BigTag.pull_username(g.get_targetName(you)) #target name

#BigTag.pull_interests

#createPageOutput =[] # this should be what the create page needs to run
#for i in g.get_inUsers():
#    createPageOutput.append(BigTag.pull_username(i.get_name()))

g.start_seq()

#g.get_targetName()
#sending data to the google maps page
#g.get_TOT()
#g.get_TOL()
#this data depends on what time it is


#for i in range(50):
#    print(g.add_user(str(i)).get_userinfo(BigTag))

#for user in g.get_inUsers():
#    print(g.get_targetName(user.get_name()))
#    print(user.get_name()+" "+BigTag.pull_username(g.get_targetName(user.get_name())))

for i in range(5):
    tagger = choice(g.get_inUsers())
    g.remove_user(tagger,g.get_target(tagger).get_code())
    print(len(g.get_inUsers()))
