import csv
import pymysql

class DatabaseManager:
    def __init__(self, host, username, password, database, port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = pymysql.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            db=self.database,
            port=self.port,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def create_tables(self):
        create_sentiments_table = """
            CREATE TABLE IF NOT EXISTS sentiments (
                sentiment_id INT PRIMARY KEY,
                sentiment_label VARCHAR(20) UNIQUE
            )
        """
        create_tweets_table = """
            CREATE TABLE IF NOT EXISTS tweets (
                id INT AUTO_INCREMENT PRIMARY KEY,
                text VARCHAR(280),
                sentiment_id INT,
                FOREIGN KEY(sentiment_id) REFERENCES sentiments(sentiment_id)
            )
        """
        self.cursor.execute(create_sentiments_table)
        self.cursor.execute(create_tweets_table)

    def insert_from_csv(self, csv_file):
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                text = row['tweets']
                label = row['labels']
                
                if label == 'good':
                    sentiment_id = 2
                elif label == 'bad':
                    sentiment_id = 3
                else:
                    sentiment_id = 1  

                insert_sentiment_query = """
                    INSERT IGNORE INTO sentiments (sentiment_id, sentiment_label) 
                    VALUES (%s, %s)
                """
                self.cursor.execute(insert_sentiment_query, (sentiment_id, label))
                self.connection.commit()

                insert_tweet_query = """
                    INSERT INTO tweets (text, sentiment_id) 
                    VALUES (%s, %s)
                """
                self.cursor.execute(insert_tweet_query, (text, sentiment_id))
                self.connection.commit()

    def close_connection(self):
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    DB_HOST = '127.0.0.1'
    DB_USERNAME = 'root'
    DB_PASSWORD = ''
    DB_NAME = 'db_sentiment'
    DB_PORT = 3306
    
    db_manager = DatabaseManager(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME, DB_PORT)
    db_manager.connect()
    db_manager.create_tables()
    db_manager.insert_from_csv('data_source/file.csv')
    db_manager.close_connection()
