from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
from connection import *
from queries import *
import smtplib
import random
import logging
from datetime import datetime
import re

import hashlib

def generate_hashed_password(password):
         # Hash the password using SHA-256
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode('utf-8'))
        hashed_password = sha256_hash.hexdigest()
        return hashed_password


mydb=connect_db()
cursor=mydb.cursor()

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')


###########################################################################################################
                        #to add new user(authority of  alpha user)
###########################################################################################################

#import re
#to check valid name
def is_valid_name(name):
    pattern = r'^[a-zA-Z][a-zA-Z0-9]*$'
    return re.match(pattern, name) is not None and not name.isdigit()

#to check valid email
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

#To check valid phone_no.
def is_valid_phone_number(phone_number):
    # Remove any non-digit characters from the phone number
    cleaned_number = re.sub(r'\D', '', phone_number)

    # Check if the cleaned number matches the desired format
    pattern = r'^\d{10}$'  # Assumes a 10-digit phone number
    return re.match(pattern, cleaned_number) is not None

#to add new user
def adduser():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside add usder API.....")
        data = request.get_json()
        logging.debug(dt_string + " Taking Some inputs.....")
        if "Name" not in data:
            return jsonify({"error": "Missing 'Name' in request data"}), 400
        if "Email_ID" not in data:
            return jsonify({"error": "Missing 'Email_ID' in request data"}), 400
        if "Contact" not in data:
            return jsonify({"error": "Missing 'Contact' in request data"}), 400
        Name = data['Name']
        Email_ID = data['Email_ID']
        Contact = data['Contact']
        role = "User"
        if  not is_valid_name(Name):
            return jsonify({"error":"Invalid Name....Name can't start from Number,Can be a alphanumeric,special characters are not allowed"}),400
        if  not is_valid_email(Email_ID):
            return jsonify({"error":"Invalid Email"}),400
        if  not is_valid_phone_number(Contact):
            return jsonify({"error":"Invalid Contact Number."}),400
        query="select 1 from Users where Email_ID=%s;"
        values=(Email_ID,)
        cursor.execute(query,values)
        id=cursor.fetchone()
        if id:
               return jsonify({"error":"email already exists."}),400
        def send_otp_email(receiver_email, otp):
            logging.debug(dt_string + " Entered send_otp_email function....")
            sender_email = "pratik@infobellit.com"  # Replace with your email address
            password = "mzygirleuqcwzwtk"  # Replace with your email password
            message = f"Subject: login credentials for Project Management Tool\n\n Your Username is your email.\nYour password is: {otp}"
            logging.debug(dt_string + " Sending email....")
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
        def generate_otp(length=6):
            logging.debug(dt_string + " Entered into generate_otp function....")
            digits = "0123456789abcdefghijklmnopqrstuvwxyz"
            otp = ""
            for _ in range(length):
                otp += random.choice(digits)
            logging.debug(dt_string + " OTP generated sucessfully....")
            return otp
        # Example usage
        email = Email_ID  # Replace with the recipient's email address
        logging.debug(dt_string + " calling generate_otp function...")
        otp = generate_otp()
        logging.debug(dt_string + " calling send_otp_email function....")
        send_otp_email(email, otp)
        print("OTP sent successfully!")
        # Hash the password
        logging.debug(dt_string + " Encrypting the generated password....")
        hashed_password =hashlib.sha256(str(otp).encode('utf-8')).hexdigest()
        logging.debug(dt_string + " calling User_add function to update the database....")
        return user_add(Name, Email_ID,hashed_password, Contact,role)  #add role 
    except KeyError as e:
        # Handle missing key in the request data
        #print(dt_string + " Missing key in request data: " + str(e))
        return jsonify({"error": str(e)}), 400
    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        print(" Database error: " + str(err))
        return jsonify({"error": "Database error: " + str(err)}), 500
    except Exception as e:
        # Handle any other unexpected exceptions
        print(" An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500


############################################################################################################
                            # API to Assign a user to a particular project    
############################################################################################################



#to assign a user to new project
def assignuser():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside assign user api...")
        data = request.get_json()
        
        logging.debug(dt_string + " Accepting some values....")

        if "Project_ID" not in data:
            return jsonify({"error": "Missing 'Project_ID' in request data"}), 400
        if "user_ID" not in data:
            return jsonify({"error": "Missing 'user_ID' in request data"}), 400
        if "role_in_project" not in data:
            return jsonify({"error": "Missing 'role_in_project' in request data"}), 400
        

        Project_ID=data['Project_ID']
        
        user_ID =data["user_ID"]
        
        role_in_project = data["role_in_project"]
        

        if(type(Project_ID) is not int):
            return jsonify({"error":"Project_ID must be integer"}),400
        if(type(user_ID) is not int):
            return jsonify({"error":"user_ID must be integer"}),400
        

        logging.debug(dt_string + " checking if the project manager role already existing or not since tere can be only one project manager per project....")
        
        if(role_in_project=='Project manager'):
            
            return jsonify({"error":"Their can only be one Project manager per project"}),400
        
        else:
            
            logging.debug(dt_string + " calling user_assign function to update the databse....")
            
            return user_assign(Project_ID,user_ID,role_in_project)

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
    

############################################################################################################
                            # API to show all users to added     
############################################################################################################




def showuser():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside show user api...")

        return user_show()

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
    


def delete_users():
    try:    
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside show delete_user api...")
        data = request.get_json()
        
        logging.debug(dt_string + " Accepting some values....")
        if "user_ID" not in data:
            return jsonify({"error": "Missing 'user_ID' in request data"}), 400
        user_ID = data["user_ID"]
        
        if(type(user_ID) is not int):
            return jsonify({"error":"user_ID must be integer"}),400

        return user_delete(user_ID)
    
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


def user_useridwise():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside update_issuewise_comments api....")
        data = request.get_json()

        if "user_ID" not in data:
            return jsonify({"error": "Missing 'user_ID' in request data"}), 400
    

        logging.debug(dt_string + " Accepting values to update ")

        
        user_ID=data["user_ID"]
     
        if(type(user_ID) is not int):
            return jsonify({"error":"user_ID must be integer"}),400

        query="Select name, Email_ID , Contact from Users where user_ID = %s;"
        values=(user_ID,)
        cursor.execute(query,values)
        id=cursor.fetchall()
        user_list = []
        for project in id:
                    user_dict = {
                        'name': project[0],
                        'Email_ID' : project[1],
                        'Contact' : project[2]
                    }
                    user_list.append(user_dict)
        logging.debug(dt_string + " returning a list of user details for this user_ID...")
        return jsonify(user_list),200
        

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
    



    

