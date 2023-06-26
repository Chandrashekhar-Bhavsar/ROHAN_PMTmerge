from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
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
        print(data)
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
        query = "SELECT status FROM Task WHERE task_id = 1001"
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
                    query = "UPDATE Task SET status = %s WHERE task_id = %s"
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
    
### new workflow added ###
def AssignWorkflow():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for AssignWorkflow module api")
        logging.debug(dt_string+" Inside the AssignWorkflow module api ")       
        data = request.get_json()
        logging.debug(dt_string+" payload recived from frontend is ",data)
        Project_ID = data["Project_ID"]
        task = data["task"]
        defect = data["defect"]
        cursor = mydb.cursor()
        query1 = "INSERT INTO workflowconnection (Project_ID, workflow_name,issue_type) VALUES (%s, %s,%s)"
        values1 = (Project_ID, task,"task")
        cursor.execute(query1, values1)
        query2 = "INSERT INTO workflowconnection (Project_ID, workflow_name,issue_type) VALUES (%s, %s,%s)"
        values2 = (Project_ID, defect,"defect")
        cursor.execute(query2, values2)
        mydb.commit()
        
        logging.debug(dt_string+" querry executed successfully" )
        return jsonify({"message": "Workflow assigned to project successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    
def ProjectwiseWorkflow():
    try:
        cursor = mydb.cursor()
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for ProjectwiseWorkflow module api")
        logging.debug(dt_string+" Inside theProjectwiseWorkflow module api ")       
        data = request.get_json()
        logging.debug(dt_string+" payload recived from frontend is ",data)
        print(data)
        Project_ID = data["Project_ID"]
        query = "select p.issue_type, p.workflow_name, w.workflow from workflowconnection p join workflow w on w.workflow_name=p.workflow_name where p.Project_ID=%s;"
        values = (Project_ID,)
        cursor.execute(query, values)
        out=cursor.fetchall()
        array_list=[]   
        for i in out:
            dis={"issue_type":i[0],"workflow_name":i[1],"workflow":i[2]}
            array_list.append(dis)
        logging.debug(dt_string+" querry executed successfully" )
        
        return jsonify(array_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

def CreateWorkflow():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for CreateWorkflow module api")
        logging.debug(dt_string+" Inside the CreateWorkflow module api ")       
        data = request.get_json()
        logging.debug(dt_string+" payload recived from frontend is ",data)
        Project_ID = data["Project_ID"]
        type = str(data["type"])
        print(type)
        workflowname=data["wfn"]
        array=str(data["array"])
        cursor = mydb.cursor()
        query1 = "INSERT INTO workflowconnection (Project_ID,workflow_name,issue_type) values(%s,%s,%s) ;"
        values1 = (Project_ID, workflowname,type)
        cursor.execute(query1, values1)
       
        query2 = "INSERT INTO workflow (workflow_name,workflow) VALUES (%s, %s)"
        values2 = (workflowname,array)
        cursor.execute(query2, values2)
        mydb.commit()
        
        logging.debug(dt_string+" querry executed successfully" )
        return jsonify({"message": "workflow added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
def Delete_Workflow():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for Delete_Workflow module api")
        logging.debug(dt_string+" Inside the Delete_Workflow module api ")       
        data = request.get_json()
        logging.debug(dt_string+" payload recived from frontend is ",data)
        Project_ID = data["Project_ID"]
        workflow_name = data["workflow_name"]
        cursor = mydb.cursor()
        query1 = "delete from workflowconnection where Workflow_name=%s and Project_ID=%s"
        values1 = (Project_ID, workflow_name)
        cursor.execute(query1, values1)
       
        query2 = "delete from workflow where workflow_name= %s"
        values2 = (workflow_name,)
        cursor.execute(query2, values2)
        mydb.commit()
        
        logging.debug(dt_string+" querry executed successfully" )
        return jsonify({"message": "workflow deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    

    

    
    
    