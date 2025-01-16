import pymysql


def connect():
    return pymysql.connect(host="localhost",user="root",password="",database="cirebonan",cursorclass=pymysql.cursors.DictCursor)

def secret_key():
    return "your_secret_key"