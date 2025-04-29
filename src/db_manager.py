import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Database connection successful")

        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
    
    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            self.connection.commit()
            cursor.close()
            return True
        
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return False
        
    def fetch_all(self, query, params=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            print(f"Error fetching data: {err}")
            return None
        
    def fetch_one(self, query, params=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            result = cursor.fetchone()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            print(f"Error fetching data: {err}")
            return None
        
    def get_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            cursor.close()
            return tables
        except mysql.connector.Error as e:
            print("Error fetching tables:", e)
            return []

'''
    def close_connections(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")
'''