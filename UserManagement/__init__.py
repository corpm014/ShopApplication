import bcrypt
from UserManagement.userClass import User

# Manager class
class Manager:
    # Constructor
    def __init__(self, app):
        self.app = app
    

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
    def signUp(self, username, email, password):
        """
        :param username:
        :param email:
        :param password:
        """
        pass

        

