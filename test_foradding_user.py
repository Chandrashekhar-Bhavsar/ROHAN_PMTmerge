import unittest 
import requests
import json

class TestFlask(unittest.TestCase):

#############################################
    ####        CASE1       ####
#############################################

    def test_add_user_api_for_correct_data(self):
        print("#"*50)
        print("Test case id: TCAU01")
        print("Test case name: Checking for CORRECT data  ")
        print("Inside the Test Case ")
        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_user"

        # Prepare the data for the new user
        data = {"name":"Saurabh",
                "email_id":"Saurabh@infobellit.com",
                "contact":"9876543201",
                "role":"Project Manager"}


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
    ####        CASE2      ####
#############################################

    def test_add_user_api_for_missing_name(self):


        print("#"*50)
        print("Test case id: TCAU02")
        print("Test case name: Checking for missing name  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_user"

        # Prepare the data for the new user
        data = {
                "email_id":"Saurabh@infobellit.com",
                "contact":"9876543201",
                "role":"Project Manager"}


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


    def test_add_user_api_for_missing_emailid(self):

        print("#"*50)
        print("Test case id: TCAU03")
        print("Test case name: Checking for missing email_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_user"

        # Prepare the data for the new user
        data = {"name":"Saurabh",
                "contact":"9876543201",
                "role":"Project Manager"}


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


    def test_add_user_api_for_missing_contact(self):

        print("#"*50)
        print("Test case id: TCAU04")
        print("Test case name: Checking for missing contact ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_user"

        # Prepare the data for the new user
        data = {"name":"Saurabh",
                "email_id":"Saurabh@infobellit.com",
                "role":"Project Manager"}


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


    def test_add_user_api_for_missing_role(self):

        print("#"*50)
        print("Test case id: TCAU05")
        print("Test case name: Checking for missing role  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_user"

       
        data = {"name":"Saurabh",
                "email_id":"Saurabh@infobellit.com",
                "contact":"9876543201"}
        
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


    def test_add_user_api_for_incorrect_name(self):

        print("#"*50)
        print("Test case id: TCAU06")
        print("Test case name: Checking for incorrect name  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_user"

        # Prepare the data for the new user
        data = {"name":"1Saurabh",
                "email_id":"Saurabh@infobellit.com",
                "contact":"9876543201",
                "role":"Project Manager"}


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


    def test_add_user_api_for_incorrect_emailid(self):

        print("#"*50)
        print("Test case id: TCAU07")
        print("Test case name: Checking for incorrect email_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_user"

        # Prepare the data for the new user
        data = {"name":"Saurabh",
                "email_id":"Saurabhinfobellit.com",
                "contact":"9876543201",
                "role":"Project Manager"}


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

#############################################
    ####        CASE8       ####
#############################################



    def test_add_user_api_for_incorrect_contact(self):

        print("#"*50)
        print("Test case id: TCAU08")
        print("Test case name: Checking for incorrect contact  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_user"

        # Prepare the data for the new user
        data = {"name":"Saurabh",
                "email_id":"Saurabh@infobellit.com",
                "contact":"983201",
                "role":"Project Manager"}


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


    
    def test_add_user_api_for_duplicate_email(self):

        print("#"*50)
        print("Test case id: TCAU09")
        print("Test case name: Checking for duplicate email  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//add_user"

        # Prepare the data for the new user
        data = {"name":"Saurabh",
                "email_id":"Saurabh@infobellit.com",
                "contact":"983201",
                "role":"Project Manager"}


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



