
from flask import Flask, jsonify, request
import jwt
from functools import wraps
import mysql.connector
from flask_cors import CORS,cross_origin
from flask_bcrypt import bcrypt
from connection import *
from queries import *
from workflow import *
from Filter import *
from connection import *
from issue import *
from pmt import *
from UserManagement_module import *
import logging
import datetime
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

file = open("myfile.txt","w")

app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')
app.config['SECRET_KEY'] = 'your-secret-key'



@app.route('/')
def home():
    return '<h1>Welcome Team :To the POC YJB</h1>'


############################################################
#                       workflow module                    #
############################################################

app.secret_key = 'your_secret_key'  # Set a secret key for session management

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            # Verify and decode the token
            data = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            # Add the decoded token data to the request context if needed

        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return f(*args, **kwargs)

    return decorated

@app.route('/AddWorkFlow', methods=['POST'])
#@token_required
def AddWorkFlow():
    return addwf()


@app.route('/GetWorkflow', methods=['GET'])
def GetWorkflow():
    return getworkflow()


@app.route('/GetWorkflowByName', methods=['POST'])
def GetWorkflowByName():
    return GetWorkFloByName()


@app.route('/StatusUpdate', methods=['POST'])
def StatusUpdate():
    return statusupdate()


@app.route('/AssignUser', methods=['POST'])
def AssignUser():
    return Assign_User()


@app.route('/GetWorkflowIssue', methods=['POST'])
def GetWorkflowIssue():
    return getworkflowussue()




############################################################
#                       Issue module                       #
############################################################


@app.route('/IssueByMonth', methods=['POST'])
def IssueByMonth():
    return IssueFilterationMonth()

@app.route('/IssueByWeek', methods=['POST'])
def IssueByWeek():
    return IssueFilterationWeek()

@app.route('/IssueByQuarter', methods=['POST'])
def IssueByQuarterly():
    return IssueFilterationQuarterly()

@app.route('/DetailedIssue', methods=['GET'])
def DetailedIssue():
    return DetailedIssueFilteration()
    
    
############################################################
#                       authentication module              #
############################################################



@app.route('/login', methods=['POST'])
def pm_login():
        
    return pm_loginn()


@app.route('/create_project', methods=['POST'])
#@token_required
def create_project():
    return create_projects()

@app.route('/ProjectList', methods=['POST'])
#@token_required
def ProjectList():
    return get_cardprojectdetails()


@app.route('/updateProject', methods=['PUT'])
def update_project():
    return update_projects() 

@app.route('/deleteProject', methods=['POST'])
def delete_project():
    return deleteprojects()



@app.route('/add_user', methods=['POST'])
def add_user():
    return adduser()
    

@app.route('/assign_user', methods=['POST'])
def assign_user():
   return Assign_User()
   

@app.route('/userdetails_project', methods=['POST'])
def user_details_project():
    return get_users_from_project()





@app.route('/get_issue_detailsss', methods=['POST'])
def get_issuedetails():
    return get_issue_details()


@app.route('/issue_explore', methods=['POST'])
def issuess_explore():
    return issues_explore()


@app.route('/tasks_count', methods=['POST'])
def count_tasks():
    return get_task_count()


@app.route('/defects_count', methods=['POST'])
def count_defects():
    return get_defect_count()
   




    


        



   


    
@app.route('/show_user', methods=['GET'])
def show_user():
    return showuser()


@app.route('/deletecomment', methods=['POST'])
def deletecomment():
    return delete_comment()

@app.route('/comment_add', methods=['POST'])
def comment_add():
    return add_comment()


@app.route('/display_comment', methods=['POST'])
def display_comment():
    return display_comments()
    

############################ CREATE ISSUE DETAILS #################################

# Defining an API endpoint (/create_issue) for creating a new issue. This endpoint expects a POST request.
@app.route('/create_issue', methods=['POST'])
def create_issue():
    # Call the create_issue function from the queries module with the required arguments
    return createIssue()  
    

############################ UPDATE ISSUE DETAILS #################################

# Defining an API endpoint (/update_issue) for updating an existing issue. This endpoint expects a POST request.
@app.route('/update_issue', methods=['POST'])
def update_issue():
    # Call the update_issue function from the queries module with the required arguments
    return updateIssue()  # Pass the necessary arguments
    

############################ DELETE ISSUE DETAILS #################################

# Defining an API endpoint (/delete_issue) for deleting an issue. This endpoint expects a POST request.
@app.route('/delete_issue', methods=['POST'])
def delete_issue():
    # Call the delete_issue function from the queries module with the required arguments
    return deleteissue()  # Pass the necessary arguments
    

############################ CREATE TASK #################################

@app.route('/create_task', methods=['POST'])
def create_task():
    # Call the create_task function from the queries module with the required arguments
    return createtask()  # Pass the necessary arguments
    

############################ UPDATE TASK #################################

@app.route('/update_task', methods=['POST'])
def update_task():
    # Call the update_task function from the queries module with the required arguments
    return updatetask()  # Pass the necessary arguments
    

############################ DELETE TASK #################################

@app.route('/delete_task', methods=['POST'])
def delete_task():
    # Call the delete_task function from the queries module with the required arguments
    return deletetask()  # Pass the necessary arguments
 
############################ CREATE DEFECT#################################

@app.route('/create_defect', methods=['POST'])
def create_defect():

    return createdefect()

############################ UPDATE DEFECT#################################

@app.route('/update_defect', methods=['POST'])
def update_defect():

    return updatedefect()

############################ DELETE DEFECT #################################

@app.route('/delete_defect', methods=['POST'])
def delete_defect():
    return deletedefect()

@app.route('/completeProjectdetails', methods=['POST'])
def completeProjectdetails():
    return ProjectDetails()

@app.route('/update_user', methods=['POST'])
def update_user():
    return update_users()

@app.route('/delete_user', methods=['POST'])
def delete_user():
    return delete_users()

@app.route('/useridwise_user', methods=['POST'])
def useridwise_user():
    return user_useridwise()

############################################################
#                       workflow module 2                  #
############################################################

@app.route('/Assign_Workflow', methods=['POST'])
def Assign_Workflow():
    return AssignWorkflow()

@app.route('/Projectwise_Workflow', methods=['POST'])
def Projectwise_Workflow():
    return ProjectwiseWorkflow()

@app.route('/Create_Workflow', methods=['POST'])
def Create_Workflow():
    return CreateWorkflow()

@app.route('/DeleteWorkflow', methods=['POST'])
def DeleteWorkflow():
    return Delete_Workflow()

    
if __name__ == "__main__":
    app.run(debug=True,port=5000)
