from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
import smtplib
import random
import logging
from datetime import datetime
from flask_bcrypt import Bcrypt

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')
bcrypt = Bcrypt(app)

def add_status():

    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside add_project_status api....")
        data = request.get_json()
        print(data)
        logging.debug(dt_string + " Accepting values for add project status.....")
        if "id" not in data:
            return jsonify({"error": "Missing 'Project_ID' in request data"}), 400
        if "status" not in data:
            return jsonify({"error": "Missing 'status' in request data"}), 400 
        id=data['id']
        status=data["status"]
        if(type(id) is not int):
            return jsonify({"error":"id must be integer"}),400
        logging.debug(dt_string + ' calling project_statusadd function.....')
        return statusadd(id,status)

    except KeyError as e:
        # Handle missing key in the request data
        #print("Missing key in request data: " + str(e))
        return jsonify({"error": " Missing key " + str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        print("Database error: " + str(err))
        
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    
#########################################################################################################


def display_status():
    
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside display_status....")
        data = request.get_json()
        logging.debug(dt_string + ' Accepting id to display status.....')
        if "id" not in data:
            return jsonify({"error": "Missing 'id' in request data"}), 400
        id=data["id"]
        if(type(id) is not int):
            return jsonify({"error":"id must be integer"}),400
        logging.debug(dt_string + " calling displaystatus function......")

        return displaystatus(id)

    except KeyError as e:
        # Handle missing key in the request data
        #print("Missing key in request data: " + str(e))
        return jsonify({"error": str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        print("Database error: " + str(err))
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    


    ######################################################################################################
    ###############################################################################################################



def update_status():
    
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside update_status api....")
        data = request.get_json()

        if "id" not in data:
            return jsonify({"error": "Missing 'id' in request data"}), 400
        if "status" not in data:
            return jsonify({"error": "Missing 'status' in request data"}), 400
        logging.debug(dt_string + " Accepting values to update ")
        id=data["id"]
        status=data["status"]
        if(type(id) is not int):
            return jsonify({"error":"id must be integer"}),400

        logging.debug(dt_string + " inside updatestatus function to update the database.....")
        return updatestatus(id,status)
        

    except KeyError as e:
        # Handle missing key in the request data
        return jsonify({"error":  + str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        print("Database error: " + str(err))
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    