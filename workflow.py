from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
from workflow import *
import datetime
from datetime import datetime
import logging
import ast
import json
mydb=connect_db()
cursor=mydb.cursor()

logging.basicConfig(level=logging.DEBUG)



def addwf():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for addworkflow api")
        logging.debug(dt_string+" Inside the addworkflow api ")
        data = request.get_json()
        logging.debug(dt_string+" payload received from frontend is ")
        print(data)
        arrays=str(data["array"])
        print("recived array is ",arrays)
        wf = str(data["wf"])
        query = "INSERT INTO workflow(workflow_name,workflow) VALUES (%s, %s)"
        values = (wf, arrays)
        cursor.execute(query, values)
        mydb.commit()
        logging.debug(dt_string+" Query Exectued successfully ")
        logging.debug(dt_string+" GetWorkFlow API is executed successfully")
        return jsonify({"msg": "inserted"}), 200 
    except Exception as e:
        return jsonify({"error": "bad values"}), 400

    
def getworkflow():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for GetWorkFlow api")
        logging.debug(dt_string+" Inside the GetWorkFlow api ")
        logging.debug(dt_string+" payload received from frontend is ")
        query = "Select * from workflow"
        #values=(wfn,)
        cursor.execute(query,)
        out=cursor.fetchall()
       
        print("sql query output",out)
        print(out[0])
        array_list=[]   
        for i in out:
            dis={"array_name":i[0],"array":i[1]}
            array_list.append(dis)


        return jsonify(array_list)
    except Exception as e:
        return jsonify({"error": "bad values"}), 400
    
def GetWorkFloByName():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for GetWorkfloByName api")
        logging.debug(dt_string+" Inside the GetWorkfloByName api ")
        logging.debug(dt_string+" payload received from frontend is ")
        data = request.get_json()
        wfn=data["wfn"]
        query = "Select workflow from workflow where workflow_name=%s"
        values=(wfn,)
        cursor.execute(query,values)
        out=cursor.fetchall()
        
        print("sql query output",out[0][0])
        input_string = out[0][0]
        input_list = ast.literal_eval(input_string)
        output = json.dumps(input_list)
        print(output)
        return jsonify(out[0][0])
    except Exception as e:
        return jsonify({"error": "bad values"}), 400



def statusupdate():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call for StatusUpdate api")
        logging.debug(dt_string+" Inside the StatusUpdate api ")
        data = request.get_json()
        status = data["status"]
        logging.debug(dt_string+" payload received from frontend is ", data)
        cursor = mydb.cursor()
        query = "SELECT status FROM task WHERE task_id = 1001"
        cursor.execute(query)
        current_state = cursor.fetchone()[0]
        print("current state =", current_state)
        print("state inserted by user =", status)
        
        query = "SELECT prev_state, next_state FROM workflow WHERE current_state = %s"
        values = (current_state,)
        cursor.execute(query, values)
        succ_state = cursor.fetchall()
        logging.debug(dt_string + " Querry is executed successfully ")
        logging.debug(dt_string + " result of query ",succ_state)
        print(succ_state)
        print(type(succ_state))
        
        for k in succ_state:
            for j in k:
                if j.lower() == status.lower():
                    logging.debug(dt_string + " checking for enter workflow is match with previous or next state ")
                    print("match")
                    print(status)
                    query = "UPDATE task SET status = %s WHERE task_id = %s"
                    values = (status, 1001)
                    cursor.execute(query, values)
                    logging.debug(dt_string + " Update status Querry is executed successfully ")
                    mydb.commit()
                    return jsonify({"message": "Update successful"})
        
        print("not present")
        return jsonify({"message": "Violating workflow"})
    except Exception as e:
        return jsonify({"error": str(e)})

def getworkflowussue():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for get workfflow module api")
        logging.debug(dt_string+" Inside the get workfflow api ")       
        data = request.get_json()
        logging.debug(dt_string+" payload recived from frontend is ",data)
        issue = data["issueid"]
        wfn = data["wfn"]
        if (type(issue) is not int) or (type(wfn) is not str):
            return jsonify({"message": "data format is not right "}), 400
        cursor = mydb.cursor()
        query = "INSERT INTO issueworkflow_connection (issue_id, workflow_name) VALUES (%s, %s)"
        values = (issue, wfn)
        cursor.execute(query, values)
        mydb.commit()
        logging.debug(dt_string+" querry executed successfully" )
        return jsonify({"message": "Workflow assigned to task successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400