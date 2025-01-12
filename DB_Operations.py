import pymysql
import pymysql.cursors
from config import connect

def fetch_all_items():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM items")
            rows = cursor.fetchall()
        return rows
    finally:
        connection.close()

def insert_item(name,description):
    connection=connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO items (name, description) VALUES (%s,%s)",(name,description))
            connection.commit()
        return 1
    finally:
        connection.close()

def fetch_item_by_id(item_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM items WHERE id = %s",(item_id))
            rows = cursor.fetchone()
        return rows
    finally:
        connection.close()

def update_item(item_id, name, description):
    connection=connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE items SET name = %s, description = %s WHERE id = %s", (name,description,item_id))
            connection.commit()
            return 1
    finally:
        connection.close()

def delete_item(item_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM items WHERE id = %s",(item_id))
            connection.commit()
        return 1
    finally:
        connection.close()

def validate_user(username, password):
    """Validasi username dan password dari database."""
    connection = connect()  # Ganti dengan fungsi untuk membuat koneksi ke database
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()  # Mengambil user pertama yang ditemukan
            return user  # Mengembalikan user jika ditemukan
    finally:
        connection.close()
