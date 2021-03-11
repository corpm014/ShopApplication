import sqlite3

# Database
class Database:
    # Constructor
    def __init__(self, database):
        # Database
        self.database = database
        
        # Connection and cursor
        self.conn = sqlite3.connect(self.database)
        self.cusror = self.conn.cursor()
    
    def addUser(self, username, email, password):
        with self.conn:
            query = "INSERT INTO users VALUES (?, ?, ?)"
            params = (username, email, password)
            self.cursor.execute(query, params)
        

    def deleteUser(self, username):
        with self.conn:
            query = "DELETE * FROM users WHERE username=?"
            params = (username,)
            self.cusror.execute(query, params)
    
    def updateUsername(self, email, newUsername):
        with self.conn:
            query = "UPDATE users SET username=? WHERE email=?"
            params = (newUsername, email)
            self.cursor.execute(query, params)
    
    def updateEmail(self, username, newEmail):
        with self.conn:
            query = "UPDATE users SET email=? WHERE username=?"
            params = (newEmail, username)
            self.cursor.execute(query, params)
    
    def updatePassword(self, email, newPassword):
        with self.conn:
            query = "UPDATE users SET password=? WHERE email=?"
            params = (newPassword, email)
            self.cursor.execute(query, params)
    
    def getProductFromName(self, productName):
        with self.conn:
            query = "SELECT product_name FROM products WHERE product_id=?"
            params = (productName,)
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
    
    def getProductFromID(self, productID):
        with self.conn:
            query = "SELECT product_id FROM products WHERE product_name=?"
            params = (productID)
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
    

    def setUp(self):
        with self.conn:
            query = "CREATE TABLE IF NOT EXISTS users(username text, email text, password text)"
            self.cursor.execute(query)

            productsQuery = "CREAET TABLE IF NOT EXISTS products(product_name text, product_id text, price int)"
            self.cursor.execute(productsQuery)

