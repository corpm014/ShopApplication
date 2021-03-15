import bcrypt


# Manager class
class Manager:
    # Function that logins in a user (after database has fetched)
    @staticmethod
    def login(password, databasePassword) -> bool:
        """
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
    @staticmethod
    def signUp(password) -> (str, str):
        """
        :param username:
        :param email:
        :param password:
        :return None:
        """
        salt = bcrypt.gensalt()
        hashedPw = bcrypt.hashpw(password=password.encode('utf-8'), salt=salt)
        salt = salt.decode('utf-8')
        hashedPw = hashedPw.decode('utf-8')

        return str(hashedPw), str(salt)
