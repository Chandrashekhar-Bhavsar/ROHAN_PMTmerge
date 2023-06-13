from flask import jsonify
from flask import Flask, jsonify, request
import mysql.connector
from urllib.parse import quote_plus as urlquote



def connect_db():
    filename = "db.config"
    content = open(filename).read()
    config = eval(content)

    try:
        mydb = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"])
        #cursor = mydb.cursor()
        print(mydb)
        return mydb

    except Exception as e:
        error = {"error" : "Connection with database is failed","config":config}
        print(error)

if __name__=='__main__':
    connect_db()











