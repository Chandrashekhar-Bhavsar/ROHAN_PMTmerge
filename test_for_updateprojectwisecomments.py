import unittest 
import requests
import json

class TestFlask(unittest.TestCase):

#############################################
    ####        CASE1       ####
#############################################

    def test_update_projectwise_comments_api_for_correct_data(self):

        print("#"*50)
        print("Test case id: TCUPWC01")
        print("Test case name: Checking for CORRECT data  ")
        print("Inside the Test Case ")


        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_projectwise_comments"

        # Prepare the data for the new user
        data = {"Project_ID":100,
                "user_id":2001,
                "comment_id":21,
                "description":"comment added by shreya for projectid 100 is to be updated."}


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

    def test_update_projectwise_comments_api_for_missing_Project_ID(self):

        print("#"*50)
        print("Test case id: TCUPWC02")
        print("Test case name: Checking for missing Project_ID ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_projectwise_comments"

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

    def test_update_projectwise_comments_api_for_missing_userid(self):

        print("#"*50)
        print("Test case id: TCUPWC03")
        print("Test case name: Checking for Missing user_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_projectwise_comments"

        # Prepare the data for the new user
        data =  {"Project_ID":100,
                "comment_id":21,
                "description":"comment added by shreya for projectid 100 is to be updated."}



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

    def test_update_projectwise_comments_api_for_missing_description(self):

        print("#"*50)
        print("Test case id: TCUPWC04")
        print("Test case name: Checking for Missing description  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_projectwise_comments"

        # Prepare the data for the new user
        data =  {"Project_ID":100,
                "user_id":2001,
                "comment_id":21}



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


    def test_update_projectwise_comments_api_for_missing_commentid(self):

        print("#"*50)
        print("Test case id: TCUPWC05")
        print("Test case name: Checking for missing comment_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_projectwise_comments"

        # Prepare the data for the new user
        data =  {"Project_ID":100,
                "user_id":2001,
                "description":"comment added by shreya for projectid 100 is to be updated."}



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

    def test_update_projectwise_comments_api_for_incorrect_projectid(self):

        print("#"*50)
        print("Test case id: TCUPWC06")
        print("Test case name: Checking for incorrect Project_ID ")
        print("Inside the Test Case ")


        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_projectwise_comments"

        # Prepare the data for the new user
        data =  {"Project_ID":"100hy",
                "user_id":2001,
                "comment_id":21,
                "description":"comment added by shreya for projectid 100 is to be updated."}



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


    def test_update_projectwise_comments_api_for_incorrect_userid(self):

        print("#"*50)
        print("Test case id: TCUPWC07")
        print("Test case name: Checking for incorrect user_id  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_projectwise_comments"

        # Prepare the data for the new user
        data =  {"Project_ID":100,
                "user_id":"200civg",
                "comment_id":21,
                "description":"comment added by shreya for projectid 100 is to be updated."}



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

    def test_update_projectwise_comments_api_for_incorrect_userid_data(self):

        print("#"*50)
        print("Test case id: TCUPWC08")
        print("Test case name: Checking for incorrect userid data  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_projectwise_comments"

        # Prepare the data for the new user
        data = {"Project_ID":100,
                "user_id":2,
                "comment_id" : 21,
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
        print("case8")
        
        self.assertEqual(r.status_code,400)

#############################################
    ####        CASE9       ####
#############################################


def test_update_projectwise_comments_api_for_incorrect_commentid_data(self):

        print("#"*50)
        print("Test case id: TCUPWC09")
        print("Test case name: Checking for not valid comment_id data  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//update_projectwise_comments"

        # Prepare the data for the new user
        data = {"Project_ID":100,
                "user_id":2,
                "comment_id" : 2134565,
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
        print("case9")
        
        self.assertEqual(r.status_code,400)


if __name__ == "__main__":
    unittest.main()



