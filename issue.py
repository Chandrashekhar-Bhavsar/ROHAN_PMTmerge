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
        issue_name = data['issue_name']
        description = data['description']
        type = data['type']
        status = data['status']


        return createissues(issue_name, description, type, status)

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
            query = "SELECT COUNT(*) FROM issue_details WHERE issue_id=%s"
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
        query = "SELECT COUNT(*) FROM task WHERE task_id=%s"
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