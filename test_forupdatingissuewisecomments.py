import unittest 
import requests
import json

class TestFlask(unittest.TestCase):

#############################################
    ####        CASE1       ####
#############################################

    def test_update_issuewise_comments_api_for_correct_data(self):

        print("#"*50)
        print("Test case id: TCUIWC01")
        print("Test case name: Checking for correct data  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_issuewise_comments"

        # Prepare the data for the new user
        data = {"issue_id":3000,
                "user_id":2001,
                "comment_id":23,
                "description":"new"}


        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        

        # Send a POST request to the API endpoint to add the new user
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)

        # Print the response status code
        print(r.status_code)

        # Get the response content as JSON
        pastebin_url = r.json()

        # Print the JSON response
        print(pastebin_url)
        print("case1")
        # Assert that the response status code is 200 (OK)
        self.assertEqual(r.status_code,200) 

#############################################
    ####        CASE2       ####
#############################################

    def test_update_issuewise_comments_api_for_missing_issue_id(self):

        print("#"*50)
        print("Test case id: TCUIWC02")
        print("Test case name: Checking for missing issue_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_issuewise_comments"

        # Prepare the data 
        data = {"user_id":2001,
                "comment_id":23,
                "description":"comment updated by shreya for issue id 3000"}


        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        

        # Send a POST request to the API endpoint 
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)

        # Print the response status code
        print(r.status_code)

        # Get the response content as JSON
        pastebin_url = r.json()

        # Print the JSON response
        print(pastebin_url)
        print("case2")
        
        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE3       ####
#############################################

    def test_update_issuewise_comments_api_for_missing_userid(self):

        print("#"*50)
        print("Test case id: TCUIWC03")
        print("Test case name: Checking for missing issue_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint 
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_issuewise_comments"

        # Prepare the data 
        data =  {"project_id":13000,
                "comment_id":23,
                "description":"comment added by shreya for issueid 3000 is to be updated."}



        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        

        # Send a POST request to the API endpoint
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)

        # Print the response status code
        print(r.status_code)

        # Get the response content as JSON
        pastebin_url = r.json()

        # Print the JSON response
        print(pastebin_url)

        print("case3")
        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE4       ####
#############################################


    def test_update_issuewise_comments_api_for_missing_description(self):

        print("#"*50)
        print("Test case id: TCUIWC04")
        print("Test case name: Checking for missing description  ")
        print("Inside the Test Case ")

        # Define the API endpoint 
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_issuewise_comments"

        # Prepare the data 
        data =  {"issue_id":3000,
                "user_id":2001,
                "comment_id":23}



        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        

        # Send a POST request to the API endpoint 
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)

        # Print the response status code
        print(r.status_code)

        # Get the response content as JSON
        pastebin_url = r.json()

        # Print the JSON response
        print(pastebin_url)
        print("case4")

        self.assertEqual(r.status_code,400)

#############################################
    ####        CASE5       ####
#############################################



    def test_update_issuewise_comments_api_for_missing_commentid(self):

        print("#"*50)
        print("Test case id: TCUIWC05")
        print("Test case name: Checking for missing comment_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint 
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_issuewise_comments"

        # Prepare the data 
        data =  {"issue_id":3000,
                "user_id":2001,
                "description":"comment added by shreya for projectid 100 is to be updated."}



        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        

        # Send a POST request to the API endpoint 
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)

        # Print the response status code
        print(r.status_code)

        # Get the response content as JSON
        pastebin_url = r.json()

        # Print the JSON response
        print(pastebin_url)

        print("case5")
        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE6       ####
#############################################


    def test_update_issuewise_comments_api_for_incorrect_issueid(self):

        print("#"*50)
        print("Test case id: TCUIWC06")
        print("Test case name: Checking for incorrect issue_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint 
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_issuewise_comments"

        # Prepare the data 
        data =  {"issue_id":"100hy",
                "user_id":2001,
                "comment_id":23,
                "description":"comment updated by shreya for issueid 3000."}
        
        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        

        # Send a POST request to the API endpoint
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)

        # Print the response status code
        print(r.status_code)

        # Get the response content as JSON
        pastebin_url = r.json()

        # Print the JSON response
        print(pastebin_url)
        print("case6")
        
        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE7       ####
#############################################


    def test_update_issuewise_comments_api_for_incorrect_userid(self):

        print("#"*50)
        print("Test case id: TCUIWC07")
        print("Test case name: Checking for incorrect user_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint 
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_issuewise_comments"

        # Prepare the data 
        data =  {"issue_id":3000,
                "user_id":"200civg",
                "comment_id":23,
                "description":"comment updated by shreya for issue_id 3000."}



        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        

        # Send a POST request to the API endpoint 
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)

        # Print the response status code
        print(r.status_code)

        # Get the response content as JSON
        pastebin_url = r.json()

        # Print the JSON response
        print(pastebin_url)
        print("case7")

        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE8       ####
#############################################

    def test_update_issuewise_comments_api_for_incorrect_userid_data(self):

        print("#"*50)
        print("Test case id: TCUIWC08")
        print("Test case name: Checking for incorrect user_id value  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_issuewise_comments"

        # Prepare the data for the new user
        data = {"issue_id":3000,
                "user_id":2,
                "comment_id" : 21,
                "description":"comment updated by shreya for issue id 3000"}


        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        

        # Send a POST request to the API endpoint to add the new user
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)

        # Print the response status code
        print(r.status_code)

        # Get the response content as JSON
        pastebin_url = r.json()

        # Print the JSON response
        print(pastebin_url)
        print("case8")
        
        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE9       ####
#############################################


def test_update_issuewise_comments_api_for_incorrect_commentid_data(self):
        """Test case : Checking for incorrect comment_id value"""
        print("#"*50)
        print("Test case id: TCUIWC09")
        print("Test case name: Checking for incorrect comment_id value  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_issuewise_comments"

        # Prepare the data for the new user
        data = {"issue_id":3000,
                "user_id":2000,
                "comment_id" : 2134565,
                "description":"comment updated by shreya for issueid 3000"}


        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        

        # Send a POST request to the API endpoint to add the new user
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)

        # Print the response status code
        print(r.status_code)

        # Get the response content as JSON
        pastebin_url = r.json()

        # Print the JSON response
        print(pastebin_url)
        print("case9")
        
        self.assertEqual(r.status_code,400)


if __name__ == "__main__":
    unittest.main()



