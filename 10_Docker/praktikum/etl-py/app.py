import requests
import pymysql

#ambil data dari api
def get_data_from_api():
    url = "https://jsonplaceholder.typicode.com/posts?userId=1"
    response = requests.get(url)
    return response.json()

#menyimpan data ke database mysql
def save_data_to_database(data):
    connection = pymysql.connect(host='db', user='root', password='password', database='etl_db', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    
    for item in data:
        sql = "INSERT INTO posts (userId, id, title, body) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (item['userId'], item['id'], item['title'], item['body']))
    
    connection.commit()
    connection.close()

if __name__ == "__main__":
    data = get_data_from_api()
    save_data_to_database(data)
    print("Data berhasil dimasukkan ke database!")
