from flask import Flask, jsonify, request
import jwt
from functools import wraps

import mysql.connector
from flask_cors import CORS,cross_origin
from connection import *
from queries import *
import datetime
from datetime import datetime
import logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')

import hashlib
file = open("myfile.txt","w")





##############################################################################################################
                                        # login
###############################################################################################################

def pm_loginn():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call for login api")
        logging.debug(dt_string + " Inside the Login api ")
        data = request.get_json()
        Email_ID = data['email_id']
        Password = data['password']
        cursor = mydb.cursor()
        logging.debug(dt_string + " Checking for valid email")
        query1 = "SELECT * FROM Users WHERE Email_ID=%s"
        values1 = (Email_ID,)
        cursor.execute(query1, values1)
        users1 = cursor.fetchone()
        logging.debug(dt_string + " Email Checking Query executed successfully")
        logging.debug(dt_string + " Query result is ", users1)
        if not users1:
            logging.debug(dt_string + " Email id is not valid")
            return jsonify({'error': "Email is invalid"}), 400
        else:
            flag = True
            logging.debug(dt_string + " Checking for valid password")
            print("original password is",Password)
            hashed_password =hashlib.sha256(Password.encode('utf-8')).hexdigest()
            print("password is :", hashed_password)
            query2 = "SELECT * FROM Users WHERE Password=%s"
            values2 = (hashed_password,)
            cursor.execute(query2, values2)
            users2 = cursor.fetchone()
            logging.debug(dt_string + " Password Checking Query executed successfully")
            logging.debug(dt_string + " Query result is ", users2)
            if not users2:
                logging.debug(dt_string + " Password is not valid")
                return jsonify({'error': 'Password is invalid'}), 400
            else:
                flag2 = True
        if flag and flag2:
            query3 = "SELECT * FROM Users WHERE Password=%s and Email_ID=%s"
            values3 = (hashed_password,Email_ID)
            cursor.execute(query3, values3)
            users3 = cursor.fetchall()
            logging.debug(dt_string + " Email id and password are valid")
            logging.debug(dt_string + " Login api execution completed without errors")
            token = jwt.encode({'username': "Email_ID"}, 'your_secret_key', algorithm='HS256')
            return jsonify({'msg': "login successful","user_detail":users3,'token': token}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400




##############################################################################################################
                                        # CREATE PROJECT
###############################################################################################################


def create_projects():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for create roject api")
        logging.debug(dt_string+"Inside the create project api ")
        data = request.get_json()
        logging.debug(dt_string+"payload comming from frontend ")
        print(data)
        User_id=data['user_id']
        project_name = data['project_name']
        project_description = data['project_description']
        planned_sd = data['planned_sd']
        planned_ed = data['planned_ed']
        actual_sd = '2020-01-01'#data['actual_sd']
        actual_ed = '2020-01-01'#data['actual_ed']
        planned_hours = "0" #data['planned_hours']
        actual_hours = "0"#data['actual_hours']""
        status = "To_Do"#data['status']
        project_lead = data['project_lead']
        client_name = data['client_name']
        risk = data['risk']
        mitigation = data['mitigation']
        logging.debug(dt_string+"Calling create project query function ")
        return create_project_query(User_id,project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                                    planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation)

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500
    
def Assign_User():
    try:
        data = request.get_json()
        Email_id = data['email_id']
        Project_id = data['project_id']
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside user_add function.....")
        logging.debug(dt_string + " Adding the users details into the database...")
        query1 = "select user_ID from Users where email_id=%s;" 
        values1 = (Email_id,)
        cursor.execute(query1, values1)
        u_id=cursor.fetchone()
        print(u_id)
        if not u_id:
            return jsonify({"Error":"No user found"}), 400
        else:
            query2 = "INSERT INTO project_member(user_ID,Project_ID) VALUES (%s, %s);" #add role after test
            values2 = ( u_id[0],Project_id)#add role after test
            cursor.execute(query2, values2)
            mydb.commit()
            logging.debug(dt_string + " Details successfully updated into the database....")
            return jsonify({'msg':"Data Inserted"}), 200
    except Exception as e:
        print("An error occurred:", str(e))
        return jsonify({'error': 'An error occurred while fetching project details'}), 400


def get_users_from_project():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call to retrieve users from a project")
        data = request.get_json()
        project_id = data['project_id']
        cursor = mydb.cursor()
        query = "SELECT Users.user_ID, Users.roles, Users.Name, Users.Email_ID FROM Users JOIN project_member ON Users.user_ID = project_member.user_ID WHERE project_member.Project_ID = %s;"
        values = (project_id,)
        cursor.execute(query, values)
        users = cursor.fetchall()

        if not users:
            return jsonify({'error': 'No users found for the project'}), 400
        
        user_list = []
        for user in users:
            user_info = {
                'user_id': user[0],
                'role': user[1],
                'name': user[2],
                'email_id': user[3]
            }
            user_list.append(user_info)

        logging.debug(dt_string + " Users retrieved successfully")
        return jsonify({'users': user_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

def get_cardprojectdetails():
    try:
        data = request.get_json()
        User_id = data['user_id']
        print("inside the function")
        cursor = mydb.cursor()
        query = "SELECT * FROM Project_Details p join project_member m on m.Project_ID=p.Project_ID  where m.user_id=%s;"
        value=(User_id,)
        cursor.execute(query,value)
        projects = cursor.fetchall()
        project_list = []
        for project in projects:
            project_dict = {
                    'Project_id': project[0],
                    'Project_name': project[1],
                    'description': project[2],
                    'planned_sd':project[3],
                    'planned_ed':project[4],
                    'Actual_sd' : project[5],
                    'Actual_ed' : project[6],
                    'planned_hours':project[7],
                    "actual_hours":project[8],
                    "Status":project[9],
                    "project_lead":project[10],
                    "client_name":project[11],
                    "risk":project[12],
                    "mitigation":project[13]
                }
            project_list.append(project_dict)
        return jsonify(project_list),200
    except Exception as e:
        print("An error occurred:", str(e))
        return jsonify({'error': 'An error occurred while fetching project details'}), 400

def update_users():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside update usder API.....")
        data = request.get_json()
        
        logging.debug(dt_string + " Taking Some inputs.....")
        
        if "name" not in data:
            return jsonify({"error": "Missing 'name' in request data"}), 400
        if "email_id" not in data:
            return jsonify({"error": "Missing 'email_id' in request data"}), 400
        if "contact" not in data:
            return jsonify({"error": "Missing 'contact' in request data"}), 400
        if "user_id" not in data:
            return jsonify({"error":"Missing 'user_id' in the data."}),400
        name = data['name']
        
        email_id = data['email_id']
        
        contact = data['contact']

        user_id = data['user_id']
        
        if(type(user_id) is not int):
            return jsonify({"error":"user_id must be integer"}),400
        if  not is_valid_name(name):
            return jsonify({"error":"Invalid Name....Name can't start from Number,Can be a alphanumeric,special characters are not allowed"}),400
        if  not is_valid_phone_number(contact):
            return jsonify({"error":"Invalid Contact Number."}),400
        if  not is_valid_email(email_id):
            return jsonify({"error":"Invalid Email"}),400

        return user_update(user_id,name,email_id,contact)  #add role 

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



################################################################################################################    
                                   # UPDATE PROJECT DETAILS
############################################################################################################### 


def update_projects():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for Update project api")
        logging.debug(dt_string,"Inside the update project api ")
        data = request.get_json()
        logging.debug(dt_string,"payload received from frontend is ", data)
        project_id = data['project_id']
        project_name = data['project_name']
        project_description = data['project_description']
        planned_sd = data['planned_sd']
        planned_ed = data['planned_ed']
        actual_sd = data['actual_sd']
        actual_ed = data['actual_ed']
        planned_hours ="30 minute" #data['planned_hours']
        actual_hours = "40 minute" #data['actual_hours']
        status = data['status']
        project_lead = data['project_lead']
        client_name = data['client_name']
        risk = "xyz" #data['risk']
        mitigation = "xyz" #data['mitigation']
        logging.debug(dt_string,"Calling update project query function ")
        
        if not isinstance(project_id, int):
            return jsonify({'error': 'Invalid data type for project_id'}), 400
        if not isinstance(planned_hours, str):
            return jsonify({'error': 'Invalid data type for planned_hours'}), 400
        if not isinstance(actual_hours, str):
            return jsonify({'error': 'Invalid data type for actual_hours'}), 400
        
        
        return update_project_details(project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                                      planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation, project_id)

    except KeyError:
        # Handle missing key error
        return jsonify({'error': 'Missing key in the request'}), 400

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500



def ProjectDetails():
    try:
        data = request.get_json()
        pm_id = data['project_id']
        cursor = mydb.cursor()
        query = "SELECT * FROM Project_Details where project_id=%s; "
        values=(pm_id,)
        cursor.execute(query,values)
        projects = cursor.fetchall()
        project_list = []
        for project in projects:
            project_dict = {
                    'Project_id': project[0],
                    'Project_name': project[1],
                    'description': project[2],
                    'planned_sd':project[3],
                    'planned_ed':project[4],
                    'Actual_sd' : project[5],
                    'Actual_ed' : project[6],
                    'planned_hours':project[7],
                    "actual_hours":project[8],
                    "Status":project[9],
                    "project_lead":project[10],
                    "client_name":project[11],
                    "risk":project[12],
                    "mitigation":project[13]
                }
            project_list.append(project_dict)
        return jsonify(project_dict)

    except KeyError as e:
        # Handle missing key in the request data
        print("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400



###################################### GET ALL PROJECT DETAILS ###################################



def create_task():
    try:
        data = request.get_json()
        issue_id = data['issue_id']
        description = data['description']
        status = data['status']
        task_sd = data['task_sd']
        task_ed = data['task_ed']
        planned_hours = data['planned_hours']
        actual_hours = data['actual_hours']
        priority = data['priority']
       

       

        
        return createtask(issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours,priority)

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500



def update_task():
    try:
        data = request.get_json()
        task_id = data['task_id']
        issue_id = data['issue_id']
        description = data['description']
        status = data['status']
        task_sd = data['task_sd']
        task_ed = data['task_ed']
        planned_hours = data['planned_hours']
        actual_hours = data['actual_hours']
        priority = str(data['priority'])
        
        

        return updatetask(description, status, task_sd, task_ed, planned_hours, actual_hours,priority,task_id, issue_id)
    

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    


############################ DELETE TASK #################################

def delete_task():
    try:
        data = request.get_json()
        task_id = data['task_id']
        cursor = mydb.cursor()


      

        return deletetask(task_id)
        

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    



def get_users_from_project():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call to retrieve users from a project")
        data = request.get_json()
        project_id = data['project_id']
        cursor = mydb.cursor()
        query = "SELECT Users.user_ID, Users.role, Users.Name, Users.Email_ID FROM Users JOIN project_member ON Users.user_ID = project_member.user_ID WHERE project_member.Project_ID = %s;"
        values = (project_id,)
        cursor.execute(query, values)
        users = cursor.fetchall()

        if not users:
            return jsonify({'error': 'No users found for the project'}), 400
        
        user_list = []
        for user in users:
            user_info = {
                'user_id': user[0],
                'role': user[1],
                'name': user[2],
                'email_id': user[3]
            }
            user_list.append(user_info)

        logging.debug(dt_string + " Users retrieved successfully")
        return jsonify({'users': user_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400



def get_issue_details():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call to retrieve issue_details")
        data = request.get_json()
        project_id = data['project_id']
        cursor = mydb.cursor()

        query = """
        SELECT Issue_Details.Issue_Id, Issue_Details.Issue_name, Issue_Details.Description, Issue_Details.Type, Issue_Details.Status FROM Issue_Details
        JOIN issue_member ON Issue_Details.Issue_Id = issue_member.issue_ID
        WHERE issue_member.project_ID = %s
        """
        values = (project_id,)
        cursor.execute(query, values)
        result = cursor.fetchall()

        issue_details = []
        for row in result:
            issue = {
                'Issue_Id': row[0],
                'Issue_name': row[1],
                'Description': row[2],
                'Type': row[3],
                'Status': row[4]
            }
            issue_details.append(issue)

        return jsonify(issue_details), 200

    except Exception as e:
        # Handle any errors that occur during the execution
        logging.error("An error occurred: {}".format(str(e)))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    



def issues_explore():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call to retrieve users from a project")
        data = request.get_json()
        issue_id = data['issue_id']
        cursor = mydb.cursor()

        query_task = """ SELECT * FROM Task WHERE Issue_ID = %s """
        values = (issue_id,)
        cursor.execute(query_task, values)
        task_result = cursor.fetchall()

        query_defect = """SELECT * FROM defect WHERE Issue_ID = %s """
        values = (issue_id,)
        cursor.execute(query_defect, values)
        defect_result = cursor.fetchall()

        if not task_result and not defect_result:
            return jsonify({'error': 'No issue details found for the provided issue_id'}), 400

        issue_details = []

        if task_result:
            for task_row in task_result:
                task = {
                    'Task_ID': task_row[0],
                    'Issue_ID': task_row[1],
                    'Description': task_row[2],
                    'Status': task_row[3],
                    'task_SD': task_row[4],
                    'task_ED': task_row[5],
                    'Planned_Hours': task_row[6],
                    'Actual_Hours': task_row[7],
                    'Priority': task_row[8]
                }
                issue_details.append(task)

        if defect_result:
            for defect_row in defect_result:
                defect = {
                    'Defect_ID': defect_row[0],
                    'Issue_ID': defect_row[1],
                    'Description': defect_row[2],
                    'Status': defect_row[3],
                    'defect_SD': defect_row[4],
                    'defect_ED': defect_row[5],
                    'Planned_Hours': defect_row[6],
                    'Actual_Hours': defect_row[7]
                }
                issue_details.append(defect)

        return jsonify({'issue_details': issue_details}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400




def get_task_count():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call to retrieve task count")
        data = request.get_json()
        project_id = data['project_id']
        cursor = mydb.cursor()

        query = """
        SELECT COUNT(Task.Task_ID) AS task_count
        FROM Task
        JOIN issue_member ON Task.Issue_ID = issue_member.issue_ID
        WHERE issue_member.project_ID = %s
        """
        values = (project_id,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        task_count = result[0]

        return jsonify({"task_count": task_count}), 200

    except Exception as e:
        # Handle any errors that occur during the execution
        logging.error("An error occurred: {}".format(str(e)))
        return jsonify({"error": "An error occurred: " + str(e)}), 500


def get_defect_count():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call to retrieve defect count")
        data = request.get_json()
        project_id = data['project_id']
        cursor = mydb.cursor()

        query = """
        SELECT COUNT(defect.defect_ID) AS defect_count
        FROM defect
        JOIN issue_member ON defect.Issue_ID = issue_member.issue_ID
        WHERE issue_member.project_ID = %s
        """
        values = (project_id,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        defect_count = result[0]

        return jsonify({"defect_count": defect_count}), 200

    except Exception as e:
        # Handle any errors that occur during the execution
        logging.error("An error occurred: {}".format(str(e)))
        return jsonify({"error": "An error occurred: " + str(e)}), 500



    

