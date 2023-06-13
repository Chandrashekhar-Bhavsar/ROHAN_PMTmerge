import unittest 
import requests
import json

class TestFlask(unittest.TestCase):
    
#############################################
    ####        CASE1       ####
#############################################


    def test_add_project_comment_api_for_correct_data(self):

        print("#"*50)
        print("Test case id: TCACTP01")
        print("Test case name: Checking for CORRECT data  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_project_comment"

        # Prepare the data for the new user
        data = {"project_id":100,
                "user_id":2001,
                "description":"comment added by shreya for projectid 100"}


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



    def test_add_project_comment_api_or_missing_project_id(self):

        print("#"*50)
        print("Test case id: TCACTP02")
        print("Test case name: Checking for missing project_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_project_comment"

        # Prepare the data for the new user
        data = {"user_id":2001,
                "description":"comment added by shreya for projectid 100"}


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
        print("case2")
        
        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE3       ####
#############################################


    def test_add_project_comment_api_for_missing_userid(self):

        print("#"*50)
        print("Test case id: TCACTP03")
        print("Test case name: Checking for missing user_id ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_project_comment"

        # Prepare the data for the new user
        data = {"project_id":100,
                "description":"comment added by shreya for projectid 100"}


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

        print("case3")
        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE4       ####
#############################################



    def test_add_project_comment_api_for_missing_description(self):

        print("#"*50)
        print("Test case id: TCACTP04")
        print("Test case name: Checking for missing description  ")
        print("Inside the Test Case ")


        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_project_comment"

        # Prepare the data for the new user
        data = {"project_id":100,
                "user_id":2001
                }


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
        print("case4")

        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE5       ####
#############################################


    def test_add_project_comment_api_for_incorrect_projectid(self):

        print("#"*50)
        print("Test case id: TCACTP05")
        print("Test case name: Checking for incorrect project_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_project_comment"

        # Prepare the data for the new user
        data = {"project_id":"100a",
                "user_id":2001,
                "description":"comment added by shreya for projectid 100"}


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
        print("case5")
        
        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE6       ####
#############################################


    def test_add_project_comment_api_for_incorrect_userid(self):

        print("#"*50)
        print("Test case id: TCACTP06")
        print("Test case name: Checking for incorrect_userid ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_project_comment"

        # Prepare the data for the new user
        data = {"project_id":100,
                "user_id":"2001rgbegtr",
                "description":"comment added by shreya for projectid 100"}


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
        print("case6")

        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE7       ####
#############################################


    def test_add_project_comment_api_for_incorrect_userid_data(self):

        print("#"*50)
        print("Test case id: TCACTP07")
        print("Test case name: Checking for incorrect user_id data  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_project_comment"

        # Prepare the data for the new user
        data = {"project_id":100,
                "user_id":2,
                "description":"comment added by shreya for projectid 100"}


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
        print("case7")
        
        self.assertEqual(r.status_code,400)

            
if __name__ == "__main__":
    unittest.main()



