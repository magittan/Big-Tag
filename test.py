import pyrebase

config = {
"apiKey": "AIzaSyB3UTG878t8nyfUiw8zIhfyqb5Pqwp7S2I",
"authDomain": "thebigtag-135f2.firebaseapp.com",
"databaseURL": "https://thebigtag-135f2.firebaseio.com/",
"storageBucket": "thebigtag-135f2.appspot.com",
"serviceAccount": "thebigtag-135f2-firebase-adminsdk-f3yzd-32e7052d24.json"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'testingraggawgwegewGA@gmail.com'
password = 'testing11111'


user = auth.sign_in_with_email_and_password(email, password)

print(user)

db = firebase.database()

name = "Tester"

data = {
    "name":name,
    "email":email,
    "password":password
}

# Pass the user's idToken to the push method
results = db.child("users").push(data)
print(results)

all_users = db.child("users").get()
for user in all_users.each():
    print(user.key()) # Morty
    print(user.val())
