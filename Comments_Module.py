from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
import smtplib
import random
import logging
from datetime import datetime
from flask_bcrypt import Bcrypt

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')
bcrypt = Bcrypt(app)

#################################################################################3
                    #API to add comment to project
##################################################################################3

def add_projectcomment():
    """
    API endpoint for adding a comment to a project.

    Returns:
        If successful, returns the result of the 'project_commentadd' function.
        If any errors occur during execution, returns a JSON response with an error message and an appropriate status code.

    Raises:
        KeyError: If any of the required fields ('project_id', 'user_id', 'description') are missing in the request data.
        mysql.connector.Error: If there is an error related to the MySQL database.
        Exception: If any other unexpected exception occurs.

    Usage:
        - Send a POST request to the 'add_projectcomment' endpoint.
        - The request data must be in JSON format and include the following fields:
            - 'project_id' (integer): The ID of the project to add the comment to.
            - 'user_id' (integer): The ID of the user adding the comment.
            - 'description' (string): The content of the comment to be added.
"""


    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside add_project_comment api....")
        data = request.get_json()
        print(data)
        logging.debug(dt_string + " Accepting values for add project comment.....")

        if "project_id" not in data:
            return jsonify({"error": "Missing 'project_id' in request data"}), 400
        if "user_id" not in data:
            return jsonify({"error": "Missing 'user_id' in request data"}), 400
        if "description" not in data:
            return jsonify({"error": "Missing 'description' in request data"}), 400
        
        project_id=data['project_id']
        
        user_id =data["user_id"]
        
        description=data["description"]

        if(type(user_id) is not int):
            return jsonify({"error":"user_id must be integer"}),400
        if(type(project_id) is not int):
            return jsonify({"error":"project_id must be integer"}),400
        
        logging.debug(dt_string + ' calling project_commentadd function.....')

        return project_commentadd(project_id,description,user_id)

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
    


#######################################################################################
                # Add comment to issue
#######################################################################################


def add_issuecomment():
    """
    API endpoint for adding a comment to an issue.

    Returns:
        If successful, returns the result of the 'issue_commentadd' function.
        If any errors occur during execution, returns a JSON response with an error message and an appropriate status code.

    Raises:
        KeyError: If any of the required fields ('issue_id', 'user_id', 'description') are missing in the request data.
        mysql.connector.Error: If there is an error related to the MySQL database.
        Exception: If any other unexpected exception occurs.

    Usage:
        - Send a POST request to the 'add_issuecomment' endpoint.
        - The request data must be in JSON format and include the following fields:
            - 'issue_id' (integer): The ID of the issue to add the comment to.
            - 'user_id' (integer): The ID of the user adding the comment.
            - 'description' (string): The content of the comment to be added.
    """
    
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside add_issue_comment api....")
        data = request.get_json()

        logging.debug(dt_string + " Accepting values for add_issue_comments.....")

        if "issue_id" not in data:
            return jsonify({"error": "Missing 'issue_id' in request data"}), 400
        if "user_id" not in data:
            return jsonify({"error": "Missing 'user_id' in request data"}), 400
        if "description" not in data:
            return jsonify({"error": "Missing 'description' in request data"}), 400

        issue_id=data['issue_id']

        user_id =data["user_id"]
        
        description=data["description"]
        

        if(type(issue_id) is not int):
            return jsonify({"error":"issue_id must be integer"}),400
        if(type(user_id) is not int):
            return jsonify({"error":"user_id must be integer"}),400
        
        logging.debug(dt_string + " calling issue_commentadd function....")

        return issue_commentadd(issue_id,description,user_id)

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


##################################################################################################
                #api to display the comments related to a project 
##################################################################################################

def display_projectwisecomments():
    """
    API endpoint for displaying comments for a specific project.

    Returns:
        If successful, returns the result of the 'displaycomments_projectswise' function.
        If any errors occur during execution, returns a JSON response with an error message and an appropriate status code.

    Raises:
        KeyError: If the required field 'project_id' is missing in the request data.
        mysql.connector.Error: If there is an error related to the MySQL database.
        Exception: If any other unexpected exception occurs.

    Usage:
        - Send a POST request to the 'display_projectwisecomments' endpoint.
        - The request data must be in JSON format and include the following field:
            - 'project_id' (integer): The ID of the project for which to retrieve the comments.
    """
    
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside display_projectwise_comments.....")
        data = request.get_json()
        
        if "project_id" not in data:
            return jsonify({"error": "Missing 'project_id' in request data"}), 400
        
        project_id = data["project_id"]

        logging.debug(dt_string + " Accepting project_id for displaying project wise comments....")
        
        return displaycomments_projectswise(project_id)

    except KeyError as e:
        # Handle missing key in the request data0.
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        logging.error("Database error: " + str(err))
        return jsonify({"error": "Database error: " + str(err)}), 500
 
    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500



################################################################################################
                    #api to display the comments related to a issue
################################################################################################

def display_issuewisecomments():
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
        #project_id= data["project_id"]

        if "issue_id" not in data:
            return jsonify({"error": "Missing 'issue_id' in request data"}), 400
        issue_id=data["issue_id"]
       
        if(type(issue_id) is not int):
            return jsonify({"error":"issue_id must be integer"}),400
        
        
        logging.debug(dt_string + " calling displaycomments_issuewise function......")

        return displaycomments_issuewise(issue_id)

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
    

###################################################################################################################
                        #API to update a project comment
###################################################################################################################


def update_projectwisecomments():
    """
    API endpoint for updating a comment for a specific project.

    Returns:
        If successful, returns the result of the 'updateprojectwise_comments' function.
        If any errors occur during execution, returns a JSON response with an error message and an appropriate status code.

    Raises:
        KeyError: If any of the required fields ('project_id', 'comment_id', 'user_id', 'description') are missing in the request data.
        mysql.connector.Error: If there is an error related to the MySQL database.
        Exception: If any other unexpected exception occurs.

    Usage:
        - Send a POST request to the 'update_projectwisecomments' endpoint.
        - The request data must be in JSON format and include the following fields:
            - 'project_id' (integer): The ID of the project containing the comment to be updated.
            - 'comment_id' (integer): The ID of the comment to be updated.
            - 'user_id' (integer): The ID of the user updating the comment.
            - 'description' (string): The updated content of the comment.
    """
    
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside update_projectwise_comments api....")
        data = request.get_json()

        if "project_id" not in data:
            return jsonify({"error": "Missing 'project_id' in request data"}), 400
        if "comment_id" not in data:
            return jsonify({"error": "Missing 'comment_id' in request data"}), 400
        if "user_id" not in data:
            return jsonify({"error": "Missing 'user_id' in request data"}), 400
        if "description" not in data:
            return jsonify({"error": "Missing 'description' in request data"}), 400


        logging.debug(dt_string + " Accepting details to update comment....")

        project_id= data["project_id"]

        comment_id=data["comment_id"]

        description=data['description']
        
        user_id = data['user_id']

        print(type(user_id))
        if(type(user_id) is not int):
            return jsonify({"error":"user_id must be integer"}),400
        if(type(project_id) is not int):
            return jsonify({"error":"project_id must be integer"}),400
        if(type(comment_id) is not int):
            return jsonify({"error":"comment_id must be integer"}),400


        logging.debug(dt_string + " calling updateprojectwise_comments function to update database......")

        return updateprojectwise_comments(user_id, description, comment_id, project_id)
        

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
    
###############################################################################################################
                    #API to update a project comment
###############################################################################################################



def update_issuewisecomments():
    """
    API endpoint for updating a comment for a specific issue.

    Returns:
        If successful, returns the result of the 'updateissuewise_comments' function.
        If any errors occur during execution, returns a JSON response with an error message and an appropriate status code.

    Raises:
        KeyError: If any of the required fields ('issue_id', 'comment_id', 'user_id', 'description') are missing in the request data.
        mysql.connector.Error: If there is an error related to the MySQL database.
        Exception: If any other unexpected exception occurs.

    Usage:
        - Send a POST request to the 'update_issuewisecomments' endpoint.
        - The request data must be in JSON format and include the following fields:
            - 'issue_id' (integer): The ID of the issue containing the comment to be updated.
            - 'comment_id' (integer): The ID of the comment to be updated.
            - 'user_id' (integer): The ID of the user updating the comment.
            - 'description' (string): The updated content of the comment.
    """
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside update_issuewise_comments api....")
        data = request.get_json()

        
        if "issue_id" not in data:
            return jsonify({"error": "Missing 'issue_id' in request data"}), 400
        if "comment_id" not in data:
            return jsonify({"error": "Missing 'comment_id' in request data"}), 400
        if "user_id" not in data:
            return jsonify({"error": "Missing 'user_id' in request data"}), 400
        if "description" not in data:
            return jsonify({"error": "Missing 'description' in request data"}), 400



        logging.debug(dt_string + " Accepting values to update ")

        #project_id= data["project_id"]
        issue_id=data['issue_id']
        comment_id=data["comment_id"]
        description=data['description']
        user_id = data['user_id']

        if(type(user_id) is not int):
            return jsonify({"error":"user_id must be integer"}),400
        if(type(issue_id) is not int):
            return jsonify({"error":"project_id must be integer"}),400
        if(type(comment_id) is not int):
            return jsonify({"error":"comment_id must be integer"}),400

        logging.debug(dt_string + " Calling updateissuewise_comments function to update the database.....")
        return updateissuewise_comments(user_id,description,comment_id,issue_id)
        

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
    

###############################################################################################################
                    #API to delete a comment
###############################################################################################################



def delete_comment():
    """
    API endpoint for deleting a comment.

    Returns:
        If successful, returns the result of the 'delete_comments' function.
        If any errors occur during execution, returns a JSON response with an error message and an appropriate status code.

    Raises:
        KeyError: If the required field 'comment_id' is missing in the request data.
        mysql.connector.Error: If there is an error related to the MySQL database.
        Exception: If any other unexpected exception occurs.

    Usage:
        - Send a POST request to the 'delete_comment' endpoint.
        - The request data must be in JSON format and include the following field:
            - 'comment_id' (integer): The ID of the comment to be deleted.
    """
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside update_issuewise_comments api....")
        data = request.get_json()

        if "comment_id" not in data:
            return jsonify({"error": "Missing 'comment_id' in request data"}), 400
    

        logging.debug(dt_string + " Accepting values to update ")

        
        comment_id=data["comment_id"]
     
        if(type(comment_id) is not int):
            return jsonify({"error":"comment_id must be integer"}),400

        logging.debug(dt_string + " Calling updateissuewise_comments function to update the database.....")
        return delete_comments(comment_id)
        

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
    