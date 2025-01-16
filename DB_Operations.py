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

def fetch_all_messages():
    """Ambil semua pesan dari tabel messages."""
    try:
        connection = connect()
        cursor = connection.cursor()

        # Query untuk mendapatkan semua pesan
        cursor.execute('SELECT * FROM messages')
        messages = cursor.fetchall()

        connection.close()
        return messages
    except Exception as e:
        print(f"Error: {e}")
        return []


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

def save_message(name, contact, message):
    """Simpan pesan ke database."""
    try:
        connection = connect()
        cursor = connection.cursor()

        # Simpan data pesan menggunakan placeholder `%s`
        cursor.execute('''
            INSERT INTO messages (name, contact, message)
            VALUES (%s, %s, %s)
        ''', (name, contact, message))

        connection.commit()
        connection.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


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
