# from flask import jsonify
# from flask import Flask, jsonify, request
# import mysql.connector
# from urllib.parse import quote_plus as urlquote



# def connect_db():
#     filename = "db.config"
#     content = open(filename).read()
#     config = eval(content)

#     try:
#         mydb = mysql.connector.connect(
#         host=config["host"],
#         user=config["user"],
#         password=config["password"],
#         database=config["database"])
#         #cursor = mydb.cursor()
#         print(mydb)
#         return mydb

#     except Exception as e:
#         error = {"error" : "Connection with database is failed","config":config}
#         print(error)

# if __name__=='__main__':
#     connect_db()








from flask import Flask
from flask import jsonify
from flask import request
import pymysql
from urllib.parse import quote_plus as urlquote
from dbutils.pooled_db import PooledDB

app = Flask(__name__)
connection_pool = None

def create_connection_pool():
    global connection_pool
    if connection_pool is None:
        filename = "db.config"
        content = open(filename).read()
        config = eval(content)
        pool = PooledDB(
            creator=pymysql,
            host=config["host"],
            port=config.get("port", 3306),
            user=config["user"],
            password=config["password"],
            database=config["database"],
            autocommit=True,
            charset='utf8mb4',
            mincached=1,
            maxcached=10,
            maxconnections=10
        )
        connection_pool = pool

def get_connection():
    global connection_pool
    if connection_pool is None:
        create_connection_pool()
    return connection_pool.connection()

def connect_db():
    connection = get_connection()
    return connection

if __name__ == '__main__':
    app.run()