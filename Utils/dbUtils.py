import mysql.connector
from mysql.connector import Error
import datetime


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='local'
        )
        print("Подключение к MySQL успешно")
    except Error as e:
        print(f"Ошибка '{e}' при подключении к MySQL")

    return connection
