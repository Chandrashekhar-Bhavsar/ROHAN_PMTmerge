from itertools import count
from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
import datetime
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)


############################ CREATE ISSUE DETAILS #################################



def createissue():
    try:
        data = request.get_json()
        Issue_name = data['Issue_name']
        Description = data['Description']

        #cursor = mydb.cursor()

        #query = "INSERT INTO issue_details (issue_name, description) VALUES (%s, %s)"
        #values = (issue_name, description)
        #cursor.execute(query, values)
        #mydb.commit()
        return create_issue(Issue_name, Description)
        
    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: {}".format(str(e)))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400
    

############################ UPDATE ISSUE DETAILS #################################

def updateissue():
    try:
        data = request.get_json()
        issue_id = data['issue_id']
        issue_name = data['issue_name']
        description = data['description']
        cursor = mydb.cursor()
        query = "SELECT COUNT(*) FROM issue_details WHERE issue_id=%s"
        cursor.execute(query, (issue_id,))
        count = cursor.fetchone()[0]

        if count == 0:
            return jsonify({"error": "Issue not found"}), 400
        
        query = "UPDATE issue_details SET issue_name = %s,description = %s WHERE issue_id=%s"
        values = (issue_name, description, issue_id)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "Issue Updated Successfully"}), 200
   

    except KeyError as e:
        # Handle missing required parameter
        return jsonify({"error": "Missing required parameter: {}".format(str(e))}), 400

    

############################ DELETE ISSUE DETAILS #################################

def deleteissue():
    try:
        data = request.get_json()
        issue_id = data['issue_id']
        cursor = mydb.cursor()

        # Delete related records from issue_member table
        #member_query = "DELETE FROM issue_member WHERE issue_id = %s"
        #values = (issue_id,)
        #cursor.execute(member_query, values)

        # Delete related records from defect table
        #defect_query = "DELETE FROM defect WHERE issue_id = %s"
        #cursor.execute(defect_query, values)

        # Delete related records from Task table
        #task_query = "DELETE FROM task WHERE issue_id = %s"
        #cursor.execute(task_query, values)

        # Delete related records from file table
        #file_query = "DELETE FROM file WHERE issue_id = %s"
        #cursor.execute(file_query, values)

        # Delete related records from issue_workflow table
        #issuewf_query = "DELETE FROM issueworkflow_connection WHERE issue_id = %s"
        #cursor.execute(issuewf_query, values)

        # Delete project details from issue_details table
        #query = "DELETE FROM issue_details WHERE issue_id = %s"
        #cursor.execute(query, values)
        #mydb.commit()

        
        return deleteissue(issue_id)

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    

############################ CREATE TASK #################################

def createtask():
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
       

        cursor = mydb.cursor()
        #query = "INSERT INTO task (issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        #values = (issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours,priority)
        #cursor.execute(query, values)
        #mydb.commit()

        
        return createtask(issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours,priority)

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    
############################ UPDATE TASK #################################

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
        
        cursor = mydb.cursor()
       #query = "UPDATE task SET description = %s,status = %s,task_sd=%s, task_ed=%s, planned_hours=%s, actual_hours=%s, priority=%s WHERE task_id=%s and issue_id=%s"
        #values = ( description, status, task_sd, task_ed, planned_hours, actual_hours,priority,task_id, issue_id)
        #cursor.execute(query, values)
        #mydb.commit()

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


        # Delete Task from Task table
        '''query = "DELETE FROM task WHERE task_id = %s"
        values = (task_id,)
        cursor.execute(query, values)

        mydb.commit()

        logging.debug("Task deleted: task_id={}".format(task_id))
        return jsonify({"message": "Task Deleted successfully"}), 200'''

        return deletetask(task_id)
        

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    

############################ CREATE DEFECT #################################

def createdefect():
    try:
        data = request.get_json()
        issue_id = data['issue_id']
        description = data['description']
        status = data['status']
        severity =data['severity']
        defect_sd = data['defect_sd']
        defect_ed = data['defect_ed']
        planned_hours = data['planned_hours']
        actual_hours = data['actual_hours']

        cursor = mydb.cursor()

        '''query = "INSERT INTO defect (issue_id, description, status, severity, defect_sd, defect_ed, planned_hours, actual_hours) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (issue_id, description, status,severity, defect_sd, defect_ed, planned_hours, actual_hours)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "Defect created successfully"}), 200'''

        return createdefect(issue_id, description, status,severity, defect_sd, defect_ed, planned_hours, actual_hours)

    except KeyError as e:
        # Handle missing key in the request data
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    
############################ UPDATE DEFECT #################################

def updatedefect():
    try:
        data = request.get_json()
        defect_id = data['defect_id']
        issue_id = data['issue_id']
        description = data['description']
        status = data['status']
        severity =data['severity']
        defect_sd = data['defect_sd']
        defect_ed = data[ 'defect_ed']
        planned_hours = data['planned_hours']
        actual_hours = data['actual_hours']
        
        cursor = mydb.cursor()
        '''query = "UPDATE defect SET description = %s,status = %s,severity=%s,defect_sd=%s, defect_ed=%s, planned_hours=%s, actual_hours=%s WHERE defect_id=%s and issue_id=%s"
        values = ( description, status, severity, defect_sd, defect_ed, planned_hours, actual_hours,defect_id, issue_id)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Defect updated: defect_id={}".format(defect_id))
        return jsonify({"message": "Defect updated successfully"}), 200'''

        return updatedefect(description, status, severity, defect_sd, defect_ed, planned_hours, actual_hours,defect_id, issue_id)

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400


    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500


############################ DELETE DEFECT #################################

def deletedefect():
    try:
        data = request.get_json()
        defect_id = data['defect_id']
        cursor = mydb.cursor()


        # Delete Task from Task table
        '''query = "DELETE FROM defect WHERE defect_id = %s"
        values = (defect_id,)
        cursor.execute(query, values)

        mydb.commit()

        logging.debug("Defect deleted: defect_id={}".format(defect_id))
        return jsonify({"message": "Defect Deleted successfully"}), 200'''

        return deletedefect(defect_id)
        

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
