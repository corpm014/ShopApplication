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

