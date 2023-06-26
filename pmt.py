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

def ShowEmails():
    try:
        mydb.cursor()
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside  ShowEmails api....")
        data = request.get_json()
        if "Project_ID" not in data:
            return jsonify({"error": "Missing 'Project_ID' in request data"}), 400
        logging.debug(dt_string + " Accepting values... ")
        Project_ID=data["Project_ID"]
        logging.debug(dt_string + " payload recivied from frontend is... ")
        print(data)
        if(type(Project_ID) is not int):
            return jsonify({"error":"Project_ID must be integer"}),400
        query="Select Email_ID from Users where user_ID not in (select user_ID from project_member where Project_ID = %s);"
        values=(Project_ID,)
        cursor.execute(query,values)
        id=cursor.fetchall()
        
        
        logging.debug(dt_string + " returning a list of Email_ID that are not associated with project...")
        return jsonify(id),200
        
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
        
def ShowEmailsTeams():
    try:
        cursor = mydb.cursor()
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside  ShowEmailsTeams api....")
        data = request.get_json()
        if "Project_ID" not in data:
            return jsonify({"error": "Missing 'Project_ID' in request data"}), 400
        logging.debug(dt_string + " Accepting values... ")
        Project_ID=data["Project_ID"]
        logging.debug(dt_string + " payload recivied from frontend is... ")
        print(data)
        if(type(Project_ID) is not int):
            return jsonify({"error":"Project_ID must be integer"}),400
        query="Select Email_ID from Users where user_ID in (select user_ID from project_member where Project_ID = %s);"
        values=(Project_ID,)
        cursor.execute(query,values)
        id=cursor.fetchall()
        print(id)
        l = []
        for i in range(len(id)):
            l.append(id[i][0])
        
        logging.debug(dt_string + " returning a list of Email_ID that are associated with project...")
        return jsonify(l),200
        
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


def pm_loginn():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call for login api")
        logging.debug(dt_string + " Inside the Login api ")
        data = request.get_json()
        Email_ID = data['Email_ID']
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
        user_ID=data['user_ID']
        user_name=data['user_name']
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
        return create_project_query(user_ID,user_name,project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                                    planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation)

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500
    
def Assign_User():
    try:
        data = request.get_json()
        Email_ID = data['Email_ID']
        Project_ID = data['Project_ID']
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside user_add function.....")
        logging.debug(dt_string + " Adding the users details into the database...")
        query1 = "select user_ID from Users where Email_ID=%s;" 
        values1 = (Email_ID,)
        cursor.execute(query1, values1)
        u_id=cursor.fetchone()
        print(u_id)
        if not u_id:
            return jsonify({"Error":"No user found"}), 400
        else:
            query2 = "INSERT INTO project_member(user_ID,Project_ID) VALUES (%s, %s);" #add role after test
            values2 = ( u_id[0],Project_ID)#add role after test
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
        Project_ID = data['Project_ID']
        cursor = mydb.cursor()
        query = "SELECT Users.user_ID, Users.roles, Users.Name, Users.Email_ID FROM Users JOIN project_member ON Users.user_ID = project_member.user_ID WHERE project_member.Project_ID = %s;"
        values = (Project_ID,)
        cursor.execute(query, values)
        users = cursor.fetchall()

        if not users:
            return jsonify({'error': 'No users found for the project'}), 400
        
        user_list = []
        for user in users:
            user_info = {
                'user_ID': user[0],
                'role': user[1],
                'Name': user[2],
                'Email_ID': user[3]
            }
            user_list.append(user_info)

        logging.debug(dt_string + " Users retrieved successfully")
        
        
        return jsonify({'users': user_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
#######################################################

def get_cardprojectdetails():
    try:
        data = request.get_json()
        user_ID = data['user_ID']
        print("inside the function")
        cursor = mydb.cursor()
        query = "SELECT * FROM Project_Details p join project_member m on m.Project_ID=p.Project_ID  where p.ownby_id= m.user_ID and m.user_ID=%s  ;"
        value=(user_ID,)
        cursor.execute(query,value)
        projects = cursor.fetchall()
        project_list = []
        for project in projects:
            project_dict = {
                    'Project_ID': project[0],
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
                    "mitigation":project[13],
                    "ownby_id":project[14],
                    "ownby_name":project[15]
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
        if "Email_ID" not in data:
            return jsonify({"error": "Missing 'Email_ID' in request data"}), 400
        if "Contact" not in data:
            return jsonify({"error": "Missing 'Contact' in request data"}), 400
        if "user_ID" not in data:
            return jsonify({"error":"Missing 'user_ID' in the data."}),400
        name = data['name']
        
        Email_ID = data['Email_ID']
        
        Contact = data['Contact']

        user_ID = data['user_ID']
        
        if(type(user_ID) is not int):
            return jsonify({"error":"user_ID must be integer"}),400
        if  not is_valid_name(name):
            return jsonify({"error":"Invalid Name....Name can't start from Number,Can be a alphanumeric,special characters are not allowed"}),400
        if  not is_valid_phone_number(Contact):
            return jsonify({"error":"Invalid Contact Number."}),400
        if  not is_valid_email(Email_ID):
            return jsonify({"error":"Invalid Email"}),400

        return user_update(user_ID,name,Email_ID,Contact)  #add role 

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
        Project_ID = data['Project_ID']
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
        
        if not isinstance(Project_ID, int):
            return jsonify({'error': 'Invalid data type for Project_ID'}), 400
        if not isinstance(planned_hours, str):
            return jsonify({'error': 'Invalid data type for planned_hours'}), 400
        if not isinstance(actual_hours, str):
            return jsonify({'error': 'Invalid data type for actual_hours'}), 400
        
        
        return update_project_details(project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                                      planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation, Project_ID)

    except KeyError:
        # Handle missing key error
        return jsonify({'error': 'Missing key in the request'}), 400

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500



def ProjectDetails():
    try:
        data = request.get_json()
        pm_id = data['Project_ID']
        cursor = mydb.cursor()
        query = "SELECT * FROM Project_Details where Project_ID=%s; "
        values=(pm_id,)
        cursor.execute(query,values)
        projects = cursor.fetchall()
        project_list = []
        for project in projects:
            project_dict = {
                    'Project_ID': project[0],
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
        Project_ID = data['Project_ID']
        cursor = mydb.cursor()
        query = "SELECT Users.user_ID, Users.roles, Users.Name, Users.Email_ID FROM Users JOIN project_member ON Users.user_ID = project_member.user_ID WHERE project_member.Project_ID = %s;"
        values = (Project_ID,)
        cursor.execute(query, values)
        users = cursor.fetchall()

        if not users:
            return jsonify({'error': 'No users found for the project'}), 400
        
        user_list = []
        for user in users:
            user_info = {
                'user_ID': user[0],
                'role': user[1],
                'name': user[2],
                'Email_ID': user[3]
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
        Project_ID = data['Project_ID']
        cursor = mydb.cursor()

        query = """
        SELECT Issue_Details.issue.id, Issue_Details.issue_name, Issue_Details.description, Issue_Details.type, Issue_Details.status FROM Issue_Details
        JOIN Issue_Member ON Issue_Details.issue_id = Issue_Member.issue_id
        WHERE Issue_Member.Project_ID = %s
        """
        values = (Project_ID,)
        cursor.execute(query, values)
        result = cursor.fetchall()

        Issue_Details = []
        for row in result:
            issue = {
                'issue_id': row[0],
                'issue_name': row[1],
                'description': row[2],
                'type': row[3],
                'status': row[4]
            }
            Issue_Details.append(issue)
        
        
        return jsonify(Issue_Details), 200

    except Exception as e:
        # Handle any errors that occur during the execution
        logging.error("An error occurred: {}".format(str(e)))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    



def issues_explore():
    try:
        cursor = mydb.cursor()
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call to retrieve users from a project")
        data = request.get_json()
        issue_id = data['issue_id']
        print(data)
        query_task = """ SELECT * FROM Task t join Issue_Details i on t.issue_id = i.issue_id WHERE t.issue_id = %s """
        values = (issue_id,)
        cursor.execute(query_task, values)
        task_result = cursor.fetchall()

        query_defect = """SELECT * FROM Defect d join Issue_Details i on d.issue_id = i.issue_id WHERE d.issue_id = %s """
        values = (issue_id,)
        cursor.execute(query_defect, values)
        defect_result = cursor.fetchall()

        if not task_result and not defect_result:
            return jsonify({'error': 'No issue details found for the provided issue_id'}), 400
        
        print("task data",task_result)
        print("defect data",task_result)

        Issue_Details = []

        if task_result:
            for task_row in task_result:
                task = {
                    'task_id': task_row[0],
                    'issue_id': task_row[1],
                    'title': task_row[2],
                    'task_sd': task_row[3],
                    'task_ed': task_row[4],
                    'estimated_time': task_row[5],
                    'priority': task_row[6],
                    'file_attachment': task_row[7],
                    'issue_id':task_row[8],
                    'issue_name':task_row[9],
                    'description':task_row[10],
                    'type':task_row[11],
                    'status':task_row[12],
                }
                Issue_Details.append(task)

        if defect_result:
            for defect_row in defect_result:
                defect = {
                    'defect_id': defect_row[0],
                    'issue_id': defect_row[1],
                    'title': defect_row[2], 
                    'product' : defect_row[3],
                    'component' : defect_row[4],
                    'component_description' : defect_row[5],
                    'version' : defect_row[6],
                    'severity': defect_row[7],
                    'os' : defect_row[8],
                    'summary' : defect_row[9],
                    'defect_sd': defect_row[10],
                    'defect_ed': defect_row[11],
                    'priority': defect_row[12],
                    'estimated_time': defect_row[13],
                    'file_attachment': defect_row[14],
                    'issue_id':defect_row[15],
                    'issue_name':defect_row[16],
                    'description':defect_row[17],
                    'type':defect_row[18],
                    'status':defect_row[19]
                }
                    
                
                Issue_Details.append(defect)
        
        
        return jsonify({'issue_details': Issue_Details}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400




def get_task_count():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call to retrieve task count")
        data = request.get_json()
        Project_ID = data['Project_ID']
        cursor = mydb.cursor()

        query = """
        SELECT COUNT(Task.task_id) AS task_count
        FROM Task
        JOIN Issue_Member ON Task.issue_id = Issue_Member.issue_id
        WHERE Issue_Member.Project_ID = %s
        """
        values = (Project_ID,)
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
        Project_ID = data['Project_ID']
        cursor = mydb.cursor()

        query = """
        SELECT COUNT(Defect.defect_id) AS defect_count
        FROM Defect
        JOIN Issue_Member ON Defect.issue_id = Issue_Member.issue_id
        WHERE Issue_Member.Project_ID = %s
        """
        values = (Project_ID,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        defect_count = result[0]
        
        
        return jsonify({"defect_count": defect_count}), 200

    except Exception as e:
        # Handle any errors that occur during the execution
        logging.error("An error occurred: {}".format(str(e)))
        return jsonify({"error": "An error occurred: " + str(e)}), 500



    ######################################################################################################


def add_comment():
    """
    API endpoint for adding a comment to a project.

    Returns:
        If successful, returns the result of the 'project_commentadd' function.
        If any errors occur during execution, returns a JSON response with an error message and an appropriate status code.

    Raises:
        KeyError: If any of the required fields ('Project_ID', 'user_ID', 'description') are missing in the request data.
        mysql.connector.Error: If there is an error related to the MySQL database.
        Exception: If any other unexpected exception occurs.

    Usage:
        - Send a POST request to the 'add_projectcomment' endpoint.
        - The request data must be in JSON format and include the following fields:
            - 'Project_ID' (integer): The ID of the project to add the comment to.
            - 'user_ID' (integer): The ID of the user adding the comment.
            - 'description' (string): The content of the comment to be added.
"""


    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside add_project_comment api....")
        data = request.get_json()
        print(data)
        logging.debug(dt_string + " Accepting values for add project comment.....")

        if "ID" not in data:
            return jsonify({"error": "Missing 'Project_ID' in request data"}), 400
        if "user_ID" not in data:
            return jsonify({"error": "Missing 'user_ID' in request data"}), 400
        if "description" not in data:
            return jsonify({"error": "Missing 'description' in request data"}), 400
        
        ID=data['ID']
        
        user_ID =data["user_ID"]
        
        description=data["description"]

        if(type(user_ID) is not int):
            return jsonify({"error":"user_ID must be integer"}),400
        if(type(ID) is not int):
            return jsonify({"error":"ID must be integer"}),400
        
        logging.debug(dt_string + ' calling project_commentadd function.....')

        return commentadd(ID,description,user_ID)

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


def display_comments():
    """
    API endpoint for displaying comments for a specific issue.

    Returns:
        If successful, returns the result of the 'displaycomments_issuewise' function.
        If any errors occur during execution, returns a JSON response with an error message and an appropriate status code.

    Raises:
        KeyError: If the required field 'issue_id' is missing in the request data.
        mysql.connector.Error: If there is an error related to the MySQL database.
        Exception: If any other unexpected exception occurs.

    Usage:
        - Send a POST request to the 'display_issuewisecomments' endpoint.
        - The request data must be in JSON format and include the following field:
            - 'issue_id' (integer): The ID of the issue for which to retrieve the comments.
    """
    
    try:
        
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside display_issuewise_comments....")
        data = request.get_json()
        logging.debug(dt_string + ' Accepting issue_id to display issue wise comments.....')
        #Project_ID= data["Project_ID"]

        if "ID" not in data:
            return jsonify({"error": "Missing 'ID' in request data"}), 400
        ID=data["ID"]
       
        if(type(ID) is not int):
            return jsonify({"error":"ID must be integer"}),400
        
        
        logging.debug(dt_string + " calling displaycomments function......")

        return displaycomments(ID)

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



def delete_comment():
    """
    API endpoint for deleting a comment.

    Returns:
        If successful, returns the result of the 'delete_comments' function.
        If any errors occur during execution, returns a JSON response with an error message and an appropriate status code.

    Raises:
        KeyError: If the required field 'comment_ID' is missing in the request data.
        mysql.connector.Error: If there is an error related to the MySQL database.
        Exception: If any other unexpected exception occurs.

    Usage:
        - Send a POST request to the 'delete_comment' endpoint.
        - The request data must be in JSON format and include the following field:
            - 'comment_ID' (integer): The ID of the comment to be deleted.
    """
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside update_issuewise_comments api....")
        data = request.get_json()

        if "comment_ID" not in data:
            return jsonify({"error": "Missing 'comment_ID' in request data"}), 400
    

        logging.debug(dt_string + " Accepting values to update ")

        
        comment_ID=data["comment_ID"]
     
        if(type(comment_ID) is not int):
            return jsonify({"error":"comment_ID must be integer"}),400

        logging.debug(dt_string + " Calling updateissuewise_comments function to update the database.....")
        return delete_comments(comment_ID)
        

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
    
def deleteprojects():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside deleteprojects....")
        data = request.get_json()
        logging.debug(dt_string + ' Accepting Project_ID to delete project.....')
        logging.debug(" Entered in deleteprojects function")
        Project_ID=data["Project_ID"]
        print(Project_ID)
        project_mem = "DELETE FROM project_member WHERE Project_ID = %s;"
        values = (Project_ID,)
        cursor.execute(project_mem, values)
        logging.debug(dt_string + ' query1 executed .....')
        project = "select issue_id from project_issue where Project_ID=%s"
        values = (Project_ID,)
        cursor.execute(project, values)
        issue_ids=cursor.fetchall()
        logging.debug(dt_string + ' query2 executed .....')
        query ="delete from project_status where ID = %s;"
        values = (Project_ID,)
        cursor.execute(query,values)
        logging.debug(dt_string + ' query3 executed .....')
        query ="delete from Issue_Member where Project_ID = %s;"
        values = (Project_ID,)
        cursor.execute(query,values)
        logging.debug(dt_string + ' query4 executed .....')
        print("issue_ids are ",issue_ids)
        # Delete related records from projectworkflow_connection table
        projectwf_query = "DELETE FROM workflowconnection WHERE Project_ID = %s;"
        values = (Project_ID,)
        cursor.execute(projectwf_query, values)
        logging.debug(dt_string + ' query5 executed .....')
        # delete project from comments table.
        Query = "delete from comments where ID=%s;"
        values = (Project_ID,)
        cursor.execute(Query,values)
        logging.debug(dt_string + ' query5 executed .....')
        
        for i in issue_ids:
            print (i[0])
            query1 = "delete from comments where ID = %s;"
            values = (i[0],)
            cursor.execute(query1,values)
            
            query1 = "delete from Task where issue_id  = %s;"
            values = (i[0],)
            cursor.execute(query1,values)
            
            query1 = "delete from Defect where issue_id  = %s;"
            values = (i[0],)
            cursor.execute(query1,values)
            
            query ="delete from Issue_Details where issue_id= %s;"
            values = (i[0],)
            cursor.execute(query,values)
                
        query ="delete from project_issue where Project_ID = %s;"
        values = (Project_ID,)
        cursor.execute(query,values)
            
        # Delete project details from project_details table
        query = "DELETE FROM Project_Details WHERE Project_ID = %s;"
        values = (Project_ID,)
        cursor.execute(query, values)
        
        
        mydb.commit()
        
        
        return jsonify("Done"), 200


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
        
def update_comment():
    """
    API endpoint for updating a comment.

    Returns:
        If successful, returns the result of the 'delete_comments' function.
        If any errors occur during execution, returns a JSON response with an error message and an appropriate status code.

    Raises:
        KeyError: If the required field 'comment_ID' is missing in the request data.
        mysql.connector.Error: If there is an error related to the MySQL database.
        Exception: If any other unexpected exception occurs.

    Usage:
        - Send a POST request to the 'delete_comment' endpoint.
        - The request data must be in JSON format and include the following field:
            - 'comment_ID' (integer): The ID of the comment to be deleted.
    """
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside update comments api....")
        data = request.get_json()
        if "comment_ID" not in data:
            return jsonify({"error": "Missing 'comment_ID' in request data"}), 400
        if "description" not in data:
            return jsonify({"error": "Missing 'description' in request data"}), 400
        logging.debug(dt_string + " Accepting values to update ")
        comment_ID=data["comment_ID"]
        description = data["description"]
        if(type(comment_ID) is not int):
            return jsonify({"error":"comment_ID must be integer"}),400
        logging.debug(dt_string + " Calling updateissuewise_comments function to update the database.....")
        return updatecomments(description,comment_ID)
        
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
    
    
    
def issuestate_projectwise():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside issuestate_projectwise api....")
        data = request.get_json()
        if "Project_ID" not in data:
            return jsonify({"error": "Missing 'project_id' in request data"}), 400
        logging.debug(dt_string + " Accepting values to update ")
        Project_ID=data["Project_ID"]
        query = "Select issue_id from project_issue where Project_ID  = %s;"
        values = (Project_ID,)
        cursor.execute(query,values)
        issue_id = cursor.fetchall()
        if not issue_id:
            return jsonify({"msg":"No Issues associated with the project."}),200
        status_list = []
        for issue in issue_id:
            issue = issue[0]  # Extract the issue_id from the tuple
            query1 = "SELECT DISTINCT status FROM issue_details WHERE issue_id = %s;"
            values1 = (issue,)
            cursor.execute(query1, values1)
            status = cursor.fetchall()
            if status:
                status_list.extend(status)
        print(status_list)
        a=status_list[0][0]
        b=status_list[1][0]

        return jsonify(a,b), 200
        
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
    