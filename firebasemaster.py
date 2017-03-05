import pyrebase

class database:
    def __init__(self):
        config = {
          "apiKey": "AIzaSyB3UTG878t8nyfUiw8zIhfyqb5Pqwp7S2I",
          "authDomain": "thebigtag-135f2.firebaseapp.com",
          "databaseURL": "https://thebigtag-135f2.firebaseio.com/",
          "storageBucket": "thebigtag-135f2.appspot.com"
        }

        self.firebase = pyrebase.initialize_app(config)
        self.auth = self.firebase.auth()
    
    def initialize_logger(self):
        '''
        Initializes our logger
        '''

        FILE_NAME = "kosmos_store.log"

        # setting up our logger to write to a log file
        logger = logging.getLogger(FILE_NAME)
        logger.setLevel(logging.DEBUG) # Process all levels of logging messages

        # create file handler
        file_handler = logging.FileHandler(FILE_NAME, mode='w')
        file_handler.setLevel(logging.DEBUG)

        # create stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        logger.debug("logger initialized")

        return logger


    def register(self,name,email,password):        
        register = self.auth.create_user_with_email_and_password(email, password)

        if "'registered': True" in register.text:
            self.logger.info("Registration suceeded!")
        else:
            self.logger.info("Registration failed.")

        # Get a reference to the database service
        db = firebase.database()

        # data to save
        data = {
            "name":name
        }

        # Pass the user's idToken to the push method
        results = db.child("users").push(data, user['idToken'])

        
    def login(self,email,password):    
        user = self.auth.sign_in_with_email_and_password(email, password)
    
    def refreshtoken(self):
        # Refreshes the user's idToken in order to keep their session alive
        user = self.auth.refresh(user['refreshToken'])

if __name__ == "__main__":
    app.run()    



