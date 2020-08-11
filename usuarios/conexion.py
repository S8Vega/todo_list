import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="localhost", user="root", password="0000", database="todo_list", port=3306
    )
    cursor = database.cursor(buffered=True)
    return [database, cursor]