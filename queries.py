from connection import *
# MySQL configuration
import hashlib
import smtplib
import random
import logging
from datetime import datetime
import re

import logging
from datetime import datetime
mydb=connect_db()
cursor=mydb.cursor()
def is_valid_name(name):
    pattern = r'^[a-zA-Z]+(?: [a-zA-Z]+)?$'
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




###############################################################################

def user_add(Name, Email_ID,hashed_password, Contact,role):#add role after test3
        """This endpoint is used to add a new user to the system.
          It expects the user's name, email ID, Contact information,
        and generates an OTP (One-Time Password) to be sent to the user's email address. The user's information, along with the hashed OTP, is then stored in the database."""
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside user_add function.....")
        logging.debug(dt_string + " Adding the users details into the database...")
        query = "INSERT INTO Users ( Name, Email_ID, password ,Contact,roles) VALUES (%s, %s, %s,%s,%s);" #add role after test
        values = ( Name, Email_ID,hashed_password, Contact,role)#add role after test
        cursor.execute(query, values)
        mydb.commit()
        logging.debug(dt_string + " Details successfully updated into the database....")

        return jsonify({"message": "User created successfully."}), 200


##########################################################################################

def user_show():
            now = datetime.now()
            dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            logging.debug(dt_string + " Inside user_show function.....")
            logging.debug(dt_string+"showing all the users")
            query = "select user_ID,Name,Email_ID,Contact,roles from Users;"
            cursor.execute(query)
            id=cursor.fetchall()
            user_list = []
            for project in id:
                    user_dict = {
                        'user_ID': project[0],
                        'Name': project[1],
                        'Email_ID' : project[2],
                        'Contact' : project[3],
                        "role" : project[4]
                    }
                    user_list.append(user_dict)
            logging.debug(dt_string + " returning a list of all users...")
            return jsonify(user_list),200

#################################################################################################

def user_assign(Project_ID,user_ID,role_in_project):
            """This endpoint is used to assign a user to a particular project. 
            It expects the project ID, user ID, and the user's role in the project.
              If the role is "Project manager," it returns a message indicating that there can only be one project manager per project. Otherwise, it adds the user to the project and returns a list of all users assigned to that project."""
            
            now = datetime.now()
            dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            logging.debug(dt_string + " Inside user_assign function.....")

            query="select * from Project_Details where Project_ID=%s"
            values=(Project_ID,)
            cursor.execute(query,values)
            a=cursor.fetchall()
            if not a:
                return jsonify({"error": "Invalid Project_ID"}), 400
            logging.debug(dt_string + " Inside user_assign ")

            
            query="select * from Users where user_ID=%s"
            values=(user_ID,)
            cursor.execute(query,values)
            a=cursor.fetchall()
            if not a:
                return jsonify({"error": "Invalid user_ID"}), 400

            query = "select * from project_member where user_ID=%s and Project_ID=%s;"
            values=(user_ID,Project_ID)
            cursor.execute(query,values)
            id=cursor.fetchone()
            if id:
                   return jsonify({"error":"User already associated with the project."}),400
            
            logging.debug(dt_string + " Associating the user with the requisite project...")
            query = "INSERT INTO project_member(Project_ID,user_ID,role_in_project) VALUES(%s,%s,%s);"
            values = (Project_ID,user_ID,role_in_project)
            cursor.execute(query, values)
            mydb.commit()
            logging.debug(dt_string + " The user successfully associated with the project....")
            # to fetch id of newly added member and all user_IDs
            #query = "select user_ID, name ,roles,Email_ID,Contact from users where user_ID in (select user_ID from project_member where Project_ID=%s);"
            logging.debug(dt_string + " Getting a list of all users associated with the requisite project...")
            query = "select u.user_ID, name ,role_in_project , Email_ID,Contact from users u ,project_member m where u.user_ID=m.user_ID and Project_ID=%s"
            values = (Project_ID,)
            cursor.execute(query, values)
           
            id=cursor.fetchall()
            user_list = []
            for project in id:
                    user_dict = {
                        'user_ID': project[0],
                        'Name': project[1],
                        'roles_in_project': project[2],
                        'Email_ID' : project[3],
                        'Contact' : project[4]
                    }
                    user_list.append(user_dict)
            logging.debug(dt_string + " returning a list of all users...")
            return jsonify(user_list),200

############################################################################################

def project_commentadd(Project_ID,description,user_ID):
        """This endpoint is used to add a comment to a project.
          It expects the project ID, user ID, and the comment description. 
          The comment is then stored in the database, and the newly added comment, along with other comments for that project, is returned."""
        
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside project_commentadd function .....")
        logging.debug(dt_string +  " Adding comment to the project....")

        query = "select Name from Users where user_ID =%s"
        values = (user_ID,)
        cursor.execute(query,values)
        a_name=cursor.fetchone()
        if not a_name:
            return jsonify({"error": "Invalid user_ID"}), 400
        author_name=a_name[0]
        
        print(author_name)
        logging.debug(dt_string + "noted....")
        
        query = "INSERT INTO comments(ID, description, user_ID, author_name, date) VALUES (%s, %s, %s, %s, now())"
        values = (Project_ID, description, user_ID, author_name)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug(dt_string + " Comment successfully added....")
        # to fetch newly added member comments
        logging.debug(dt_string + " getting all the comments associated with this project....")
        query = "select * from comments where id=%s;"
        values = (Project_ID,)
        cursor.execute(query, values)
        id=cursor.fetchall()
        logging.debug(dt_string + " All comments fetched sucessfully....")
        comments_list = []
        for project in id:
                comments_dict = {
                    'comment_ID': project[0],
                    'ID': project[1],
                    'description': project[2],
                    'user_ID' : project[3],
                    'date' : project[4]
                }
                comments_list.append(comments_dict)
        logging.debug(dt_string + " returning all the comments associated with project.")
        return jsonify(comments_list),200


#######################################################################################

def issue_commentadd(issue_id,description,user_ID):
        """This endpoint is used to add a comment to an issue.
          It expects the issue ID, user ID, the author's name, and the comment description. 
          The comment is then stored in the database, and the newly added comment, along with other comments for that issue, is returned."""
        
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside issue_commentadd function.....")
        logging.debug(dt_string + " Adding new comment to issue_id passed ", issue_id)

        query = "select Name from Users where user_ID =%s"
        values = (user_ID,)
        cursor.execute(query, values)
        a_name=cursor.fetchone()
        if not a_name:
            return jsonify({"error": "Invalid user_ID"}), 400
        author_name=a_name[0]

        query = "INSERT INTO comments(ID,description,user_ID,author_name,date) VALUES (%s, %s,%s,%s,now())"
        values = (issue_id,description,user_ID,author_name)
        cursor.execute(query, values)
        mydb.commit()
        logging.debug(dt_string + " Comment added sucessfully to issue_id ", issue_id)
        # to fetch newly added member comments
        logging.debug(dt_string + " Fetching all the comments related to issue ", issue_id)
        query = "select * from comments where ID=%s;"
        values = (issue_id,)
        cursor.execute(query, values)
        id=cursor.fetchall()
        comments_list = []
        for project in id:
                comments_dict = {
                    'comment_ID': project[0],
                    'ID': project[1],
                    'description': project[2],
                    'user_ID' : project[3],
                    'author_name': project[4],
                    'date' : project[5]
                }
                comments_list.append(comments_dict)
        logging.debug(dt_string + " Returning the list of all the comments related to this issue...")
        return jsonify(comments_list),200

##############################################################################

def displaycomments_projectswise(Project_ID):
        """This endpoint is used to display all the comments related to a specific project. 
        It expects the project ID and retrieves all the comments associated with that project from the database. 
        The comments are returned as a JSON response"""

        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside displaycomments_projectwise function.....")
        logging.debug(dt_string + " Fetching all the comments related to this project with Project_ID ",Project_ID)
        query = "select comment_ID,user_ID,description,author_name,date from comments where ID=%s;"
        values = (Project_ID,)
        cursor.execute(query, values)
        id=cursor.fetchall()
        if(id is None):
                return jsonify({"error":"no project found with this Project_ID"}),400
        
        logging.debug(dt_string + " All the comments if exists fetched sucessfuly ....")
        comments_list = []
        for project in id:
                comments_dict = {
                    'comment_ID': project[0],
                    'user_ID' : project[1],
                    'description': project[2],
                    'author_name' : project[3],
                    'date' : project[4]
                }
                comments_list.append(comments_dict)
        if(len(comments_list)==0 ):
            return jsonify({"error":"no matching results"}),400
        else:
            logging.debug(dt_string + " returning the list of all comments for the project with Project_ID ", Project_ID)
            return jsonify(comments_list),200
        

############################################################################################

def displaycomments_issuewise(issue_id):
        """This endpoint is used to display all the comments related to a specific issue. 
        It expects the project ID and issue ID and retrieves all the comments associated with that issue from the database.
          The comments are returned as a JSON response."""
        
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside displaycomments_issuewise function.....")
        logging.debug(dt_string +  " Fetching all the comments related to the issue with issue_id ",issue_id)
        query = "select comment_ID,user_ID,description,author_name,date from comments where ID = %s"
        values = (issue_id,)
        cursor.execute(query, values)
        id=cursor.fetchall()
        if(id is None):
                return jsonify({"error":"no issue found with this issue_id"}),400

        logging.debug(dt_string + " All comments fetched sucessfully...")
        comments_list = []
        for project in id:
                comments_dict = {
                    'comment_ID': project[0],
                    'user_ID' : project[1],
                    'description': project[2],
                    'author_name' : project[3],
                    'date' : project[4]
                }
                comments_list.append(comments_dict)

        if(len(comments_list)==0 ):
            return jsonify({"error":"no matching results"}),400
        else:
            logging.debug(dt_string + " Returning all the comments related to issueId ",issue_id)
            return jsonify(comments_list),200

####################################################################################

def updateprojectwise_comments(user_ID, description, comment_ID, Project_ID):
    """
    Updates a project-wise comment in the database.

    Args:
        user_ID (int): The ID of the user making the comment.
        description (str): The updated comment description.
        author_name (str): The author's name.
        comment_ID (int): The ID of the comment to be updated.
        Project_ID (int): The ID of the project.

    Returns:
        list: A list of dictionaries representing the updated comments for the project, each containing the comment details.

    Raises:
        Exception: If there is an error executing the SQL queries.
    """

    now = datetime.now()
    dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
    logging.debug(dt_string + " Inside updateprojectwise_comments function.....")
    logging.debug(dt_string + "fetching the author name based on user_ID")
    # Fetch the author_name from the users table

    query = "SELECT Name FROM users WHERE user_ID = %s"
    values = (user_ID,)
    cursor.execute(query, values)
    a_name=cursor.fetchone()
    if not a_name:
            return jsonify({"error": "Invalid user_ID"}), 400
    author_name=a_name[0]  # Assign the fetched result to a variable
    logging.debug(dt_string + " The author name fetched sucessfully.... ")
    # Update the comment
    logging.debug(dt_string + " Updating the comment...")
    query="select * from comments where comment_ID=%s "
    values=(comment_ID,)
    cursor.execute(query,values)
    a=cursor.fetchone()
    if not a:
            return jsonify({"error": "Invalid comment_ID"}), 400
    logging.debug(dt_string + " Updating the comment")
    query = "UPDATE comments SET description = %s, user_ID = %s, author_name = %s , date=now() WHERE comment_ID = %s;"
    values = (description, user_ID, author_name, comment_ID)
    cursor.execute(query, values)
    mydb.commit()
    logging.debug(dt_string + " Comment updated sucessfully...")

    # Retrieve the updated comments for the project
    logging.debug(dt_string + " Fetching all the comments along with the upade")
    query = "SELECT comment_ID, user_ID, description, author_name, date FROM comments WHERE ID = %s"
    values = (Project_ID,)
    cursor.execute(query, values)

    updated_comments = cursor.fetchall()
    logging.debug(dt_string + " All comments fetched successfully....")
    comments_list = []
    for project in updated_comments:
        comments_dict = {
            'comment_ID': project[0],
            'user_ID': project[1],
            'description': project[2],
            'author_name': project[3],
            'date': project[4]
        }
        comments_list.append(comments_dict)

    logging.debug(dt_string + " Returing the list of all comments...")
    return jsonify(comments_list)

##########################################################################

def updateissuewise_comments(user_ID,description,comment_ID,issue_id):
                """Update an issue comment with the provided details.

                Args:
                user_ID (int): The ID of the user updating the comment.
                description (str): The updated comment description.
                comment_ID (int): The ID of the comment to update.
                issue_id (int): The ID of the issue associated with the comment.

                Returns:
                A JSON response containing the updated comment details.

                Raises:
                Exception: If an error occurs during the update process.
                """
        
                now = datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                logging.debug(dt_string + " Inside updateissuewise_comments API.....")

                logging.debug(dt_string + " fetching name from the given the user_ID")
                
                query = "select Name from users where user_ID =%s"
                values = (user_ID,)
                cursor.execute(query, values)
                a_name=cursor.fetchone()
                if not a_name:
                        return jsonify({"error": "Invalid user_ID"}), 400
                author_name=a_name[0]  # Assign the fetched result to a variable
                logging.debug(dt_string + " Assigned the fetched name to author name.")
                logging.debug(dt_string + " Updating the comment related details into the databse....")

                query="select * from comments where comment_ID=%s "
                values=(comment_ID,)
                cursor.execute(query,values)
                a=cursor.fetchone()
                if not a:
                    return jsonify({"error": "Invalid comment_ID"}), 400

                query = "update comments set description=%s,user_ID=%s,author_name=%s where comment_ID=%s;"
                values = (description,user_ID,author_name,comment_ID)
                cursor.execute(query, values)
                mydb.commit()
                logging.debug(dt_string + " updation done successfully....")
                logging.debug(dt_string + " Fetching all the comments ...")
                query = "select comment_ID,user_ID,description,author_name,date from comments where ID = %s"
                values = (issue_id,)
                cursor.execute(query, values)

                id=cursor.fetchall()
                logging.debug(dt_string + " Comments fetched successfully....")
                comments_list = []
                for project in id:
                        comments_dict = {
                        'comment_ID': project[0],
                        'user_ID' : project[1],
                        'description': project[2],
                        'author_name' : project[3],
                        'date' : project[4]
                        }
                        comments_list.append(comments_dict)
                logging.debug(dt_string + " Returning the comments list for the issue with issue_id ",issue_id)
                return jsonify(comments_list)

#######################################################################################

def delete_comments(comment_ID):
            """it deletes a comment based on comment_ID"""
            now = datetime.now()
            dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            logging.debug(dt_string + " Inside delete_comments function.....")
            
            query="select * from comments where comment_ID=%s "
            values=(comment_ID,)
            cursor.execute(query,values)
            a=cursor.fetchone()
            if not a:
                    return jsonify({"error": "Invalid comment_ID"}), 400

            query = "delete from comments where comment_ID=%s;"
            values= (comment_ID,)
            cursor.execute(query,values)
            mydb.commit()
            
            return jsonify({"msg":"Comment deleted sucessfully"}),200



def create_project_query(user_ID,project_name, project_description, 
                   planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, 
                  client_name, risk, mitigation):
        cursor = mydb.cursor()
        query1 = "INSERT INTO Project_Details (Project_Name, Project_Description, Planned_SD, Planned_ED,Actual_SD, Actual_ED, Planned_Hours, Actual_Hours, Status, Project_Lead, Client_Name, Risk, Mitigation) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values1 = (project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation)
        cursor.execute(query1, values1)
        mydb.commit()
        query2 =  "select Project_ID from Project_Details where project_name = %s;"
        values2 = (project_name,)
        cursor.execute(query2,values2)
        id =cursor.fetchone()
        print(id[0])
        query3 = "Insert into project_member(user_ID,Project_ID) values(%s,%s);"
        values3 = (user_ID,id[0])
        cursor.execute(query3,values3)
        mydb.commit()
        return jsonify({"message": "Project created successfully"}), 200




def update_project_details(project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation, Project_ID):
        cursor = mydb.cursor()
        query = "UPDATE Project_Details SET project_name = %s, project_description = %s, planned_sd = %s, planned_ed = %s,actual_sd = %s,actual_ed = %s,planned_hours = %s,actual_hours =%s,status = %s,project_lead = %s,client_name = %s,risk = %s,mitigation = %s where Project_ID = %s"
        values = (project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation, Project_ID)
        cursor.execute(query, values)
        mydb.commit()
        return jsonify({"message": "Project updated successfully"}), 200




############################ CREATE ISSUE  #################################


def create_issue(Issue_name, Description):
        query = "INSERT INTO issue_details (issue_name, description) VALUES (%s, %s)"
        values = (Issue_name, Description)
        cursor.execute(query, values)
        mydb.commit()
    
        
        logging.debug("Issue created: issue_name={}, description={}".format(Issue_name, Description))
        return jsonify({"message": "Issue created successfully"}), 200


########################### UPDATE ISSUE DETAILS #################################

def updateissues(status,issue_id):
   
        logging.debug("Inside updateissues function")
        
        query = "UPDATE Issue_Details SET status = %s WHERE issue_id=%s"
        values = (status, issue_id)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Issue updated: status={}".format(status))
        return jsonify({"message": "Issue Updated Successfully"}), 200


########################### UPDATE ISSUE DESCRIPTION #################################

def updateissuesdesc(descripition,issue_id):
   
        logging.debug("Inside updateissues function")
        
        query = "UPDATE Issue_Details SET description = %s WHERE issue_id=%s"
        values = (descripition, issue_id)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Issue updated: description={}".format(descripition))
        return jsonify({"message": "Issue Updated Successfully"}), 200



############################ DELETE ISSUE DETAILS #################################

def deleteissues(issue_id):
        logging.debug("Inside deleteissues function")
        

        check_query = "SELECT * FROM Issue_Details WHERE issue_id = %s"
        cursor.execute(check_query, (issue_id,))
        result = cursor.fetchone()
        if result is None:
            return jsonify({"error": "Issue not found"}), 400
        
        # Delete related records from defect table
        defect_query = "DELETE FROM Defect WHERE issue_id = %s"
        values = (issue_id,)
        cursor.execute(defect_query, values)
        
        # Delete related records from Task table
        task_query = "DELETE FROM Task WHERE issue_id = %s"
        cursor.execute(task_query, values)

        
        # Delete related records from issue_workflow table
        issuewf_query = "DELETE FROM Issueworkflow_Connection WHERE issue_id = %s"
        cursor.execute(issuewf_query, values)
    
        # Delete project details from issue_details table
        query = "DELETE FROM Issue_Details WHERE issue_id = %s"
        cursor.execute(query, values)
        mydb.commit()

        
        logging.debug("Issue deleted: issue_id={}".format(issue_id))
        return jsonify({"message": "Issue Deleted successfully"}), 200

############################ CREATE TASK #################################

def createtask(issue_id, title, task_sd, task_ed, estimated_time, priority):
        logging.debug("Inside createtask function")
        query = "INSERT INTO Task (issue_id,title,task_sd, task_ed, estimated_time, priority) VALUES (%s, %s, %s, %s, %s,%s)"
        values = (issue_id, title, task_sd, task_ed, estimated_time, priority)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "Task created successfully"}), 200

############################ UPDATE TASK #################################

def updatetask( title, task_sd, task_ed, estimated_time, priority, file_attachment, task_id, issue_id):
        logging.debug("Inside update task function")
        query = "UPDATE Task SET title = %s,task_sd=%s, task_ed=%s, estimated_time=%s, priority=%s, file_attachment=%s WHERE task_id=%s and issue_id=%s"
        values = ( title, task_sd, task_ed, estimated_time, priority, file_attachment, task_id, issue_id)
        cursor.execute(query, values)
        mydb.commit()
        mydb.close()
        return jsonify({"message": "Task updated successfully"}), 200

############################ DELETE TASK #################################

def deletetask(task_id):
        
        query = "DELETE FROM task WHERE task_id = %s"
        values = (task_id,)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Task deleted: task_id={}".format(task_id))
        return jsonify({"message": "Task Deleted successfully"}), 200

############################ CREATE DEFECT #################################

def createdefects(issue_id, title, product, component, component_description, version,severity, os, summary, defect_sd, defect_ed, priority,estimated_time):
        query = "INSERT INTO Defect (issue_id, title, product, component, component_description, version, severity, OS, summary, defect_sd, defect_ed, priority,estimated_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (issue_id, title, product, component, component_description, version,severity, os, summary, defect_sd, defect_ed, priority,estimated_time)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({'message': 'Defect created successfully'}), 200

############################ UPDATE DEFECT #################################
def updatedefects(issue_id, title, product, component, component_description, version,severity, os, summary, defect_sd, defect_ed, priority,estimated_time, file_attachment, defect_id):
        query = "UPDATE Defect SET issue_id=%s, title=%s, product=%s, component=%s, component_description=%s,version=%s, severity=%s, os=%s, summary=%s, defect_sd=%s, defect_ed=%s,priority=%s, estimated_time=%s, file_attachment=%s WHERE defect_id=%s"
        values = (issue_id, title, product, component, component_description, version,severity, os, summary, defect_sd, defect_ed, priority,estimated_time, file_attachment, defect_id)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({'message': 'Defect updated successfully'}), 200

############################ DELETE DEFECT #################################

def deletedefect(defect_id):
        
        query = "DELETE FROM defect WHERE defect_id = %s"
        values = (defect_id,)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Defect deleted: defect_id={}".format(defect_id))
        return jsonify({"message": "Defect Deleted successfully"}), 200


def user_update(user_ID , Name, Email_ID, Contact):#add role after test3
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside user_update function.....")

        query = "Select Email_ID from Users where user_ID = %s;"
        values = (user_ID,)
        cursor.execute(query,values)
        id = cursor.fetchone()
        print(id)
        if(id[0]==Email_ID):
               query="update Users set Name = %s, Contact = %s where user_ID = %s;"
               values = (Name,Contact,user_ID)
               cursor.execute(query,values)
               mydb.commit()
               logging.debug(dt_string + "User details updated successfully.")
               return jsonify({"msg":" User Details updated successfully"}),200
        logging.debug(dt_string,"checking if the email is already associated with exixting user.")
        query = "select user_ID from Users where Email_ID = %s;"
        values = (Email_ID,)
        cursor.execute(query,values)
        id=cursor.fetchall()
        if id :
               return jsonify({"error":"email already exsists."}),400
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

        logging.debug(dt_string + " updating the users details into the database...")
        query = "update  Users set Name = %s, Email_ID =%s,Contact = %s , password = %s where user_ID = %s ;" #add role after test
        values = ( Name, Email_ID, Contact,hashed_password,user_ID)#add role after test
        cursor.execute(query, values)
        mydb.commit()
        logging.debug(dt_string + " Details successfully updated into the database....")

        return jsonify({"message": "User details updated successfully."}), 200


def user_delete(user_ID):
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside user_delete function.....")
        query = "select 1 from Users where user_ID=%s;"
        values = (user_ID,)
        cursor.execute(query,values)
        id = cursor.fetchone()
        if not id:
               return jsonify({"error":"User doesn't exists."}),400
        query1 = "delete from project_member where user_ID=%s;"
        values1 = (user_ID,)
        cursor.execute(query1,values1)
        query2 = "delete from Users where user_ID = %s;"
        values2 = (user_ID,)
        cursor.execute(query2,values2)
        mydb.commit()
        return jsonify({"msg":"User Successfully deleted."}),200



def commentadd(ID, description,user_ID):
        """This endpoint is used to add a comment to a project.
          It expects the project ID, user ID, and the comment description. 
          The comment is then stored in the database, and the newly added comment, along with other comments for that project, is returned."""
        
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside project_commentadd function .....")
        logging.debug(dt_string +  " Adding comment to the project....")

        query = "select Name from Users where user_ID =%s"
        values = (user_ID,)
        cursor.execute(query,values)
        a_name=cursor.fetchone()
        if not a_name:
            return jsonify({"error": "Invalid user_ID"}), 400
        author_name=a_name[0]
        
        print(author_name)
        logging.debug(dt_string + "noted....")
        
        query = "INSERT INTO comments(ID, description, user_ID, author_name, date) VALUES (%s, %s, %s, %s, now())"
        values = (ID, description, user_ID, author_name)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug(dt_string + " Comment successfully added....")
        # to fetch newly added member comments
        logging.debug(dt_string + " getting all the comments associated with this project....")
        return jsonify({"msg":"Comment Successfully added"}),200



#############################################################################################

def displaycomments(ID):
        """This endpoint is used to display all the comments related to a specific issue. 
        It expects the project ID and issue ID and retrieves all the comments associated with that issue from the database.
          The comments are returned as a JSON response."""
        
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside displaycomments_issuewise function.....")
        logging.debug(dt_string +  " Fetching all the comments related to the issue with issue_id ",ID)
        query = "select comment_ID,user_ID,description,author_name,date from comments where ID = %s"
        values = (ID,)
        cursor.execute(query, values)
        ID=cursor.fetchall()
        logging.debug(dt_string + " All comments fetched sucessfully...")
        comments_list = []
        for project in ID:
                comments_dict = {
                    'comment_ID': project[0],
                    'user_ID' : project[1],
                    'description': project[2],
                    'author_name' : project[3],
                    'date' : project[4]
                }
                comments_list.append(comments_dict)

        if(len(comments_list)==0 ):
            return jsonify({"error":"no matching results","array ": comments_list }),200
        else:
            logging.debug(dt_string + " Returning all the comments related to issueId ",ID)
            return jsonify(comments_list),200


       

def issue_member(issue_id, user_ID,Project_ID):

        logging.debug("Inside issue member function")
        query = "INSERT INTO Issue_Member (issue_id, user_ID,Project_ID) VALUES (%s, %s, %s)"
        values = (issue_id, user_ID,Project_ID)
        cursor.execute(query, values)
        mydb.commit()


        logging.debug("Defect deleted: issue_id={},user_ID={},Project_ID={}".format(issue_id, user_ID,Project_ID))
        return jsonify({"message": "Issue Members assigned Successfully"}), 200


def issuemembers_update(issue_id, user_ID, Project_ID,issueMember_id):

        logging.debug("Inside update issuemembers_update function")
        query = "UPDATE Issue_Member SET issue_id = %s,user_ID = %s, Project_ID=%s WHERE issueMember_id=%s"
        values = (issue_id, user_ID, Project_ID,issueMember_id)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Issue Member Updated: issue_id={}, user_ID={}, Project_ID={},issueMember_id={}".format(issue_id, user_ID, Project_ID,issueMember_id))
        return jsonify({"message": "Issue_Member Updated Successfully"}), 200

def issuemembers(issueMember_id):

        logging.debug("Inside delete issuemembers function")
        query = "DELETE FROM Issue_Member WHERE issueMember_id = %s"
        values = (issueMember_id,)
        cursor.execute(query, values)

        mydb.commit()

        logging.debug("Issue Member deleted: issueMember_id={}".format(issueMember_id))
        return jsonify({"message": "Issue Member Deleted successfully"}), 200



######################################################################


def updatestatus(ID,status):
            """it updates the status based on id"""
            now = datetime.now()
            dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            logging.debug(dt_string + " Inside updatestatus function.....")
            query="select * from project_status where ID=%s "
            values=(ID,)
            cursor.execute(query,values)
            a=cursor.fetchone()
            if not a:
                    return jsonify({"error": "Invalid id"}), 400
            query = "update project_status set status=%s where ID = %s;"
            values= (status,ID)
            cursor.execute(query,values)
            mydb.commit()
            return jsonify({"msg":"status updated sucessfully"}),200


#########################################################################################################################


def statusadd(ID,status):
        """This endpoint is used to add a comment to a project.
          It expects the project ID, user ID, and the comment description. 
          The comment is then stored in the database, and the newly added comment, along with other comments for that project, is returned."""
        
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside status add function .....")
        logging.debug(dt_string +  " Adding status to the id....")
        query = "select * from project_status where ID =%s"
        values = (ID,)
        cursor.execute(query,values)
        id_status=cursor.fetchone()
        if  id_status:
            return jsonify({"error": "status for this id already present you can't add new status for this id you can update it. "}), 400
        logging.debug(dt_string + " check one done.")
        query = "INSERT INTO project_status(ID,status) VALUES (%s, %s);"
        values = (ID, status)
        cursor.execute(query, values)
        mydb.commit()
        logging.debug(dt_string + " Status successfully added....")
        return jsonify({"msg":"status added Successfully"}),200


#############################################################################################


def displaystatus(ID):
        
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside displaystatus function.....")
        logging.debug(dt_string +  " Fetching status related to the project with id ",ID)
        query = "select status from project_status where ID = %s"
        values = (ID,)
        cursor.execute(query, values)
        id1=cursor.fetchall()
        print(id1)
        if(id1 is None):
                return jsonify({"error":"no status found with this id"}),400
        logging.debug(dt_string + " displaying status for id  ",ID)
        return jsonify(id1),200



def updatecomments(description,comment_ID):
            """it deletes a comment based on comment_ID"""
            now = datetime.now()
            dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            logging.debug(dt_string + " Inside update_comments function.....")
            query="select * from comments where comment_ID=%s "
            values=(comment_ID,)
            cursor.execute(query,values)
            a=cursor.fetchone()
            if not a:
                    return jsonify({"error": "Invalid comment_ID"}), 400
            query = "update comments set description = %s where comment_ID=%s;"
            values= (description , comment_ID,)
            cursor.execute(query,values)
            mydb.commit()
            return jsonify({"msg":"Comment updated sucessfully"}),200
