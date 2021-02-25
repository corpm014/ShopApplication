# Class that helps with stuff
import bcrypt

class User:
    # Constructor
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.salt = None
    
    # Generates a salt for the user
    def hashPassword(self) -> None:
        # Gen salt
        salt = bcrypt.gensalt()

        # Hashing the password
        self.password = bcrypt.hashpassword(password=self.password, salt=salt)