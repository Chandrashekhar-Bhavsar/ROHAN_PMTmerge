import unittest 
import requests
import json

class TestFlask(unittest.TestCase):

#############################################
    ####        CASE1       ####
#############################################

    def test_assign_user_api_for_correct_data(self):

        print("#"*50)
        print("Test case id: TCASU01")
        print("Test case name: Checking for CORRECT data  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//assign_user"

        # Prepare the data for the new user
        data = {"project_id":100,
                "user_ID":2007,
                "role_in_project":"Team member"}


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

    def test_assign_user_api_for_missing_project_id(self):

        print("#"*50)
        print("Test case id: TCASU02")
        print("Test case name: Checking for missing project_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//assign_user"

        # Prepare the data for the new user
        data = {
                "user_ID":2007,
                "role_in_project":"Team member"}

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

    def test_assign_user_api_for_missing_user_id(self):

        print("#"*50)
        print("Test case id: TCASU03")
        print("Test case name: Checking for missing user_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//assign_user"

        # Prepare the data for the new user
        data = {"project_id":100,
                "role_in_project":"Team member"}


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

    def test_assign_user_api_for_missing_roleinproject(self):

        print("#"*50)
        print("Test case id: TCASU04")
        print("Test case name: Checking for missing role_in_project  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//assign_user"

        # Prepare the data for the new user
        data = {"project_id":100,
                "user_ID":2007}


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

    def test_assign_user_api_for_incorrect_projectID(self):

        print("#"*50)
        print("Test case id: TCASU05")
        print("Test case name: Checking for incorrect project_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//assign_user"

       
        data = {"project_id":"100dvwd",
                "user_ID":2007,
                "role_in_project":"Team member"}
        
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

    def test_assign_user_api_for_incorrect_userid(self):

        print("#"*50)
        print("Test case id: TCASU06")
        print("Test case name: Checking for incorrect user_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//assign_user"

        # Prepare the data for the new user
        data =  {"project_id":100,
                "user_ID":"2007vev",
                "role_in_project":"Team member"}


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


    def test_assign_user_api_for_incorrect_projectid_data(self):

        print("#"*50)
        print("Test case id: TCASU07")
        print("Test case name: Checking for incorrect project_id value  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//assign_user"

        # Prepare the data for the new user
        data =  {"project_id" : 10000,
                "user_ID":2007,
                "role_in_project":"Team member"}


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

    def test_assign_user_api_for_incorrect_userid_data(self):

        print("#"*50)
        print("Test case id: TCASU08")
        print("Test case name: Checking for incorrect user_id value  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//assign_user"

        # Prepare the data for the new user
        data =  {"project_id":100,
                "user_id":20070,
                "role_in_project":"Team member"}


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

    


if __name__ == "__main__":
    unittest.main()



