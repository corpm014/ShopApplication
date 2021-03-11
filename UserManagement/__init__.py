import bcrypt
import smtplib
from UserManagement.userClass import User

# Manager class
class Manager:
    # Constructor
    def __init__(self, app, email, password):
        self.app = app
        self.email = email
        self.password = password
    

    # Function that logins in a user (after database has fetched)
    def login(self, username, password, databasePassword) -> bool:
        """
        :param username:
        :param password:
        :param databasePassword:
        :return bool:
        """

        # Password encoding
        password = password.encode('utf-8')
        databasePassword = databasePassword.encode('utf-8')

        # Comparing
        if bcrypt.checkpw(password, databasePassword):
            return True
        return False
    
    # Function that signups a user (before database)
    def signUp(self, username, email, password) -> None:
        """
        :param username:
        :param email:
        :param password:
        :return None:
        """

        # Creating instance of user and hashing the password
        user = User(username=username, email=email, password=password)
        user.hashPassword()

        subject = "Sign Up"
        body = '''
        Hi this is a test email manager
               '''  

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login(self.email, self.password)
        except Exception as E:
            print(f"[EMAIL MANAGER ERROR] {E}")
