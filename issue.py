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
        project_id = data['project_id']
        issue_name = data['issue_name']
        description = data['description']
        type = data['type']
        status = data['status']
        query3="select * from Project_Details where project_id=%s"
        values3=(project_id,)
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
            query2 = "INSERT INTO project_issue (issue_id,project_id) VALUES (%s, %s)"
            values2 = (issue_id,project_id)
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
    

############################ DELETE ISSUE DETAILS #################################

def deleteIssue():
    try:
        logging.debug("Entered the values")
        data = request.get_json()
        issue_id = data['issue_id']
        logging.debug("Values Accepted")


        return deleteissues(issue_id)
    
    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: {}".format(str(e)))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400
    


############################ CREATE TASK #################################

def createTask():
    try:
        logging.debug("Entered the values")
        data = request.get_json()
        issue_id = data['issue_id']
        title = data['title']
        description = data['description']
        task_sd = data['task_sd']
        task_ed = data['task_ed']
        estimated_time = data['estimated_time']
        priority = data['priority']
        logging.debug("Values Accepted")

        return createtask(issue_id, title, description, task_sd, task_ed, estimated_time, priority)

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: {}".format(str(e)))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400


############################ UPDATE TASK #################################

def updateTask():
    try:
        logging.debug("Entered the values")
        data = request.get_json()
        task_id = data['task_id']
        issue_id = data['issue_id']
        title = data['title']
        description = data['description']
        task_sd = data['task_sd']
        task_ed = data['task_ed']
        estimated_time = data['estimated_time']
        priority = data['priority']
        file_attachment = data['file_attachment']
        logging.debug("Values Accepted")

        cursor = mydb.cursor()
        query = "SELECT COUNT(*) FROM Task WHERE task_id=%s"
        cursor.execute(query, (task_id,))
        count = cursor.fetchone()[0]

        if count == 0:
            return jsonify({"error": "Task not found"}), 400

        
        
        return updatetask(title, description, task_sd, task_ed, estimated_time, priority, file_attachment, task_id, issue_id)

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
        logging.debug("entered into create defect" )
        data = request.get_json()
        issue_id = data['issue_id']
        title = data['title']
        description = data['description']
        severity = data['severity']
        defect_sd = data['defect_sd']
        defect_ed = data['defect_ed']
        priority = data['priority']
        estimated_time = data['estimated_time']
        logging.debug("Values Accepted")
        

        return createdefects(issue_id, title, description, severity, defect_sd, defect_ed, priority, estimated_time)

    except KeyError as e:
        # Handle missing key in the request data
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400
    
############################ UPDATE DEFECT #################################

def updateDefect():
    try:
        logging.debug('Enter the values')
        data = request.get_json()
        defect_id = data['defect_id']
        issue_id = data['issue_id']
        title = data['title']
        description = data['description']
        severity = data['severity']
        defect_sd = data['defect_sd']
        defect_ed = data['defect_ed']
        priority = data['priority']
        estimated_time = data['estimated_time']
        file_attachment = data['file_attachment']
        logging.debug('Values Accepted')

        cursor = mydb.cursor()
        query = "SELECT COUNT(*) FROM defect WHERE defect_id=%s"
        cursor.execute(query, (defect_id,))
        count = cursor.fetchone()[0]

        if count == 0:
            return jsonify({"error": "Defect not found"}), 400
        
        return updatedefects(title, description, severity, defect_sd, defect_ed, priority, estimated_time, file_attachment, defect_id, issue_id)

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
            user_id = data['user_id']
            project_id =data['project_id']
            logging.debug("accepted values")

            if not isinstance(issue_id, int):
                return jsonify({'error': 'Invalid data type for issue_id'}), 400
            if not isinstance(user_id, int):
                return jsonify({'error': 'Invalid data type for user_id'}), 400
            if not isinstance(project_id, int):
                return jsonify({'error': 'Invalid data type for project_id'}), 400
 
            return issue_member(issue_id, user_id,project_id)

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
        user_id = data['user_id']
        project_id =data['project_id']
        logging.debug("accepted values")

        if type(project_id)==str:
             return jsonify({"Error": "String value inserted"}), 400

        logging.debug("calling issuemember_update function.")
        return issuemembers_update(issue_id, user_id, project_id,issueMember_id)

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
        project_id = data['project_id']
        cursor = mydb.cursor()
        query = "select * from Issue_Details i join project_issue m on i.issue_id = m.issue_id where project_id=%s"
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
    
    
def Assign_Issue():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call to Assign_Issue api")
        data = request.get_json()
        email_id = data['email_id']
        issue_id = data['issue_id']
        project_id=data['project_id']
        cursor = mydb.cursor()
        query1 = "select user_id from Users where email_id=%s"
        values1 = (email_id,)
        cursor.execute(query1, values1)
        userId = cursor.fetchone()[0]
        print("type of cursor is ",type(userId)," and "," value is ",userId)
        print("Select query executed succesfully")
        query2 = "insert into issue_member(issue_id,user_id,project_id) values (%s,%s,%s);"
        values2 = (issue_id,userId,project_id)
        cursor.execute(query2, values2)
        mydb.commit()
        print("Data is inserted to issue_member table")
        return jsonify({"msg":"Data is inserted to issue_member table"}), 200
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
        