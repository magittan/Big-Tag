import pyrebase
import json

config = {
"apiKey": "AIzaSyB3UTG878t8nyfUiw8zIhfyqb5Pqwp7S2I",
"authDomain": "thebigtag-135f2.firebaseapp.com",
"databaseURL": "https://thebigtag-135f2.firebaseio.com/",
"storageBucket": "thebigtag-135f2.appspot.com",
"serviceAccount": "thebigtag-135f2-firebase-adminsdk-f3yzd-32e7052d24.json"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

db = firebase.database()

all_users = db.child("users").child("-KeUKJXPSKGNeKqxH8QY").get()
#print(all_users.val()[0])

for user in all_users.each():
   print(user.val())


