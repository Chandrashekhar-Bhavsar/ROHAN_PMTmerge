from itertools import count
from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
from connection import *
from queries import *
import datetime
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)


############################ CREATE ISSUE DETAILS #################################


def createIssue():
    try:
        data = request.get_json()
        logging.debug("Inside the createIssue ")
        logging.debug("payload recived is ")
        print(data)
        Project_ID = data['Project_ID']
        issue_name = data['issue_name']
        description = data['description']
        type = data['type']
        status = data['status']
        query3="select * from Project_Details where Project_ID=%s"
        values3=(Project_ID,)
        cursor.execute(query3, values3)
        result=cursor.fetchall()
        if not result:
            return jsonify({"message": "no project exist "}), 400
        else:
            query = "INSERT INTO Issue_Details (issue_name, description, type, status) VALUES (%s, %s, %s, %s)"
            values = (issue_name, description, type, status)
            cursor.execute(query, values)
            mydb.commit()
            logging.debug("data inserted into the issue_detail table ")
            issue_id = cursor.lastrowid
            query2 = "INSERT INTO project_issue (issue_id,Project_ID) VALUES (%s, %s)"
            values2 = (issue_id,Project_ID)
            cursor.execute(query2, values2)
            mydb.commit()
            logging.debug("data inserted into the project_issue table ")
            return jsonify({"message": "Issue Created Successfully", "issue_id": issue_id}), 200


    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: {}".format(str(e)))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400
    

############################ UPDATE ISSUE DETAILS #################################

def updateIssue():
    try:
            logging.debug("Entered the values")
            data = request.get_json()
            issue_id = data['issue_id']
            status = data['status']
            logging.debug("Values Accepted")
            cursor = mydb.cursor()
            query = "SELECT COUNT(*) FROM Issue_Details WHERE issue_id=%s"
            cursor.execute(query, (issue_id,))
            count = cursor.fetchone()[0]

            if count == 0:
                return jsonify({"error": "Issue not found"}), 400
        
            return updateissues(status, issue_id)
   

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: {}".format(str(e)))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400
    

############################ UPDATE ISSUE DESCRIPTION #################################

def updateIssueDesc():
    try:
            logging.debug("Entered the values")
            data = request.get_json()
            issue_id = data['issue_id']
            description = data['description']
            logging.debug("Values Accepted")
            cursor = mydb.cursor()
            query = "SELECT COUNT(*) FROM Issue_Details WHERE issue_id=%s"
            cursor.execute(query, (issue_id,))
            count = cursor.fetchone()[0]

            if count == 0:
                return jsonify({"error": "Issue not found"}), 400
        
            return updateissuesdesc(description, issue_id)
   

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: {}".format(str(e)))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

############################ DELETE ISSUE DETAILS #################################

def deleteissue():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside deleteissues....")
        data = request.get_json()
        logging.debug(dt_string + ' Accepting issue_id to delete issue.....')
        logging.debug(" Entered in deleteissues function")
        issue_id=data["issue_id"]
        print(issue_id)
        project = "select issue_id from Issue_Details where issue_id=%s"
        values = (issue_id,)
        cursor.execute(project, values)
        issue_ids=cursor.fetchall()
        if not issue_ids:
            return jsonify({"Message":"No issue found"}), 200
         
        logging.debug(dt_string + ' query1 executed .....')     
        
        for i in issue_ids:
            print (i[0])
            query1 = "delete from comments where ID = %s;"
            values = (i[0],)
            cursor.execute(query1,values)

            query2 ="delete from Issue_Member where issue_id = %s;"
            values = (i[0],)
            cursor.execute(query2,values)
            
            query2 ="delete from project_issue where issue_id = %s;"
            values = (i[0],)
            cursor.execute(query2,values)
                

        t_query = "delete from Task where issue_id = %s;"
        values = (issue_id,)
        cursor.execute(t_query,values)

        d_query = "delete from Defect where issue_id = %s;"
        values = (issue_id,)
        cursor.execute(d_query,values)

        # Delete issue details from issue_details table
        query = "DELETE FROM Issue_Details WHERE issue_id = %s;"
        values = (issue_id,)
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
    


############################ CREATE TASK #################################

def createTask():
    try:
        logging.debug("Entered the values")
        data = request.get_json()
        issue_id = data['issue_id']
        title = data['title']
        task_sd = data['task_sd']
        task_ed = data['task_ed']
        estimated_time = data['estimated_time']
        priority = data['priority']
        logging.debug("Values Accepted")

        return createtask(issue_id, title, task_sd, task_ed, estimated_time, priority)
    

    except KeyError as e:
        # Handle missing key in the request data
        print("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400


############################ UPDATE TASK #################################

def updateTask():
    try:
        logging.debug("Enter the values")
        data = request.get_json()
        task_id = data['task_id']
        issue_id = data['issue_id']
        title = data['title']
        task_sd = data['task_sd']
        task_ed = data['task_ed']
        estimated_time = data['estimated_time']
        priority = data['priority']
        file_attachment = data['file_attachment']
        logging.debug("values Accepted")

        cursor = mydb.cursor()
        query = "SELECT COUNT(*) FROM Task WHERE task_id=%s"
        cursor.execute(query, (task_id,))
        count = cursor.fetchone()[0]

        if count == 0:
            return jsonify({"error": "Task not found"}), 400
        
        
        return updatetask(title, task_sd, task_ed, estimated_time, priority, file_attachment, task_id, issue_id)

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: {}".format(str(e)))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400


    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: ".format(str(e)))
        return jsonify({"error": "An error occurred: " + str(e)}), 500



############################ CREATE DEFECT #################################

def createDefect():
    try:
        logging.debug('Enter the values')
        # Retrieve data from the request
        data = request.json

        # Extract values from the request data
        issue_id = data['issue_id']
        title = data['title']
        product = data['product']
        component = data['component']
        component_description = data['component_description']
        version = data['version']
        severity = data['severity']
        os = data['os']
        summary = data['summary']
        defect_sd = data['defect_sd']
        defect_ed = data['defect_ed']
        priority = data['priority']
        estimated_time = data['estimated_time']
        logging.debug('Values Accepted')
        

        return createdefects(issue_id, title, product, component, component_description, version,severity, os, summary, defect_sd, defect_ed, priority,estimated_time)

    except KeyError as e:
        # Handle missing key in the request data
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400
    
############################ UPDATE DEFECT #################################

def updateDefect():
    try:
        data = request.json
        defect_id = data['defect_id']
        issue_id = data['issue_id']
        title = data['title']
        product = data['product']
        component = data['component']
        component_description = data['component_description']
        version = data['version']
        severity = data['severity']
        os = data['os']
        summary = data['summary']
        defect_sd = data['defect_sd']
        defect_ed = data['defect_ed']
        priority = data['priority']
        estimated_time = data['estimated_time']
        file_attachment = data['file_attachment']

        cursor = mydb.cursor()
        query = "SELECT COUNT(*) FROM defect WHERE defect_id=%s"
        cursor.execute(query, (defect_id,))
        count = cursor.fetchone()[0]

        if count == 0:
            return jsonify({"error": "Defect not found"}), 400
        
        return updatedefects(issue_id, title, product, component, component_description, version,severity, os, summary, defect_sd, defect_ed, priority,estimated_time, file_attachment, defect_id)

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    

############################ CREATE ISSUE MEMBER #################################


def createissuemember():
        try:
            logging.debug("entered into createissuemember" )
            data = request.get_json()
            issue_id = data['issue_id']
            user_ID = data['user_ID']
            Project_ID =data['Project_ID']
            logging.debug("accepted values")

            if not isinstance(issue_id, int):
                return jsonify({'error': 'Invalid data type for issue_id'}), 400
            if not isinstance(user_ID, int):
                return jsonify({'error': 'Invalid data type for user_ID'}), 400
            if not isinstance(Project_ID, int):
                return jsonify({'error': 'Invalid data type for Project_ID'}), 400
 
            return issue_member(issue_id, user_ID,Project_ID)

        except KeyError as e:
        # Handle missing key in the request data
            logging.error("Missing key in request data: {}".format(str(e)))
            return jsonify({"error": "Missing key in request data: " + str(e)}), 400
    
    
        except Exception as e:
        # Handle any other unexpected exceptions
            logging.error("An error occurred: " + str(e))
            return jsonify({"error": "An error occurred: " + str(e)}), 500
    


############################ UPDATE ISSUE MEMBER #################################

def updateissuemember():
    try:
        logging.debug("Entered into updateissuemember")
        data = request.get_json()
        issueMember_id = data['issueMember_id']
        issue_id = data['issue_id']
        user_ID = data['user_ID']
        Project_ID =data['Project_ID']
        logging.debug("accepted values")

        if type(Project_ID)==str:
             return jsonify({"Error": "String value inserted"}), 400

        logging.debug("calling issuemember_update function.")
        return issuemembers_update(issue_id, user_ID, Project_ID,issueMember_id)

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: {}".format(str(e)))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400



############################ DELETE ISSUE MEMBER #################################

def deleteissuemember():
    try:
        logging.debug("entered into deleteissuemember")
        data = request.get_json()
        issueMember_id = data['issueMember_id']
        logging.debug("accepted values")
        
        
        logging.debug("calling issuemembers function.")
        return issuemembers(issueMember_id)

    except KeyError as e:
        # Handle missing key in the request data
        print("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    
    ## added by rohan 
    
def ProjectwiseIssue():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call to ProjectwiseIssue")
        data = request.get_json()
        Project_ID = data['Project_ID']
        cursor = mydb.cursor()
        query = "select * from Issue_Details i join project_issue m on i.issue_id = m.issue_id where Project_ID=%s"
        values = (Project_ID,)
        cursor.execute(query, values)
        result = cursor.fetchall()
        issue_details = []
        for row in result:
            issue = {
                'issue_id': row[0],
                'issue_name': row[1],
                'description': row[2],
                'type': row[3],
                'status': row[4]
            }
            issue_details.append(issue)

        return jsonify(issue_details), 200

    except Exception as e:
        # Handle any errors that occur during the execution
        logging.error("An error occurred: {}".format(str(e)))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    
    
def Assign_Issue():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call to Assign_Issue api")
        data = request.get_json()
        Email_ID = data['Email_ID']
        issue_id = data['issue_id']
        Project_ID=data['Project_ID']
        cursor = mydb.cursor()
        query1 = "select user_ID from Users where Email_ID=%s"
        values1 = (Email_ID,)
        cursor.execute(query1, values1)
        userId = cursor.fetchone()[0]
        print("type of cursor is ",type(userId)," and "," value is ",userId)
        print("Select query executed succesfully")
        query3="select * from Issue_Member where issue_id=%s and user_ID=%s and Project_ID=%s;"
        values3 = (issue_id,userId,Project_ID)
        cursor.execute(query3, values3)
        present = cursor.fetchone()
        print("value of present is ", present)
        if not present :
            query2 = "insert into Issue_Member(issue_id,user_ID,Project_ID) values (%s,%s,%s);"
            values2 = (issue_id,userId,Project_ID)
            cursor.execute(query2, values2)
            mydb.commit()
            print("Data is inserted to issue_member table")
            return jsonify({"msg":"Data is inserted to issue_member table"}), 200
        else:
            return jsonify({"MSG":"issue is already assigned to user"}),200
    except Exception as e:
        logging.error("An error occurred: {}".format(str(e)))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    
    
def update_description_taskid():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside update_description_taskid....")
        data = request.get_json()
        logging.debug(dt_string + ' Accepting task_id to update description.....')
        if "task_id" not in data:
            return jsonify({"error": "Missing 'task_id' in request data"}), 400
        if "description" not in data:
            return jsonify({"error": "Missing 'description' in request data"}), 400
        task_id=data["task_id"]
        description = data["description"]
        if(type(task_id) is not int):
            return jsonify({"error":"task_id must be integer"}),400
        query = "update Task set description = %s where task_id=%s;"
        values = (description,task_id)
        cursor.execute(query,values)
        mydb.commit()
        logging.debug(dt_string + "Description updated successfully.")
        return jsonify({"msg" : "Description updated successfully."})

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
        
        
        
def update_description_defect():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside update_description_defect....")
        data = request.get_json()
        logging.debug(dt_string + ' Accepting defect_id to update description.....')
        if "defect_id" not in data:
            return jsonify({"error": "Missing 'defect_id' in request data"}), 400
        if "description" not in data:
            return jsonify({"error": "Missing 'description' in request data"}), 400
        defect_id=data["defect_id"]
        description = data["description"]
        if(type(defect_id) is not int):
            return jsonify({"error":"task_id must be integer"}),400
        query = "update defect set description = %s where defect_id=%s;"
        values = (description,defect_id)
        cursor.execute(query,values)
        mydb.commit()
        logging.debug(dt_string + "Description updated successfully.")
        return jsonify({"msg" : "Description updated successfully."})

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
    

        
        
def userwiseissue():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside userwiseissue....")
        data = request.get_json()
        user_ID=data["user_ID"]
        query ="""SELECT pd.Project_ID, pd.Project_Name, id.issue_id, id.issue_name, id.description, id.type, id.status
FROM Project_Details pd
JOIN Issue_Member im ON im.Project_ID = pd.Project_ID
JOIN Issue_Details id ON id.issue_id = im.issue_id
WHERE im.user_ID = %s;"""

        values = (user_ID,)
        cursor.execute(query,values)
        result = cursor.fetchall()
        print("id is ", result)
        issue_details = []
        for row in result:
            issue = {
                'Project_ID': row[0],
                'Project_Name': row[1],
                'issue_id': row[2],
                'issue_name': row[3],
                'description': row[4],
                'type': row[5],
                'status': row[6]
            }
            issue_details.append(issue)
        print("result of query is ",issue_details)
        return jsonify(issue_details)
        
    except KeyError as e:
        # Handle missing key in the request data
        #print("Missing key in request data: " + str(e))
        return jsonify({"error": str(e)}), 400

        
    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    

def issuewiseuser():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside userwiseissue....")
        data = request.get_json()
        issue_id=data["issue_id"]
        query1 ="""select user_ID from Issue_Member where issue_id=%s;"""
        values1 = (issue_id,)
        cursor.execute(query1,values1)
        result = cursor.fetchone()
        print("result is ", result)
        user_id=result[0]
        print("id is ", user_id)
        query2 ="""select * from Users where user_ID=%s;"""
        values2 = (user_id,)
        cursor.execute(query2,values2)
        User_details=cursor.fetchall()
        print(User_details)
        user_details = []
        for row in User_details:
            issue = {
                'user_ID': row[0],
                'role': row[1],
                'name': row[2],
                'email_id': row[3],
                'contact': row[5]

            }
            user_details.append(issue)
        print("result of query is ", user_details)

        return jsonify({"user to given issue are ":user_details})
        
    except KeyError as e:
        # Handle missing key in the request data
        #print("Missing key in request data: " + str(e))
        return jsonify({"error": str(e)}), 400

        
    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500