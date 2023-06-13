import requests
import json
import unittest 


class TestFlask(unittest.TestCase):

#############################################
    ####        CASE1       ####
#############################################
    
    def test_display_issuewise_comments_api_for_correct_data(self):

        print("#"*50)
        print("Test case id: TCDC01")
        print("Test case name: Checking for correct data  ")
        print("Inside the Test Case ")


        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//display_issuewise_comments"

        # Prepare the data for the new user
        data = {"issue_id":3000}


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

    def test_display_issuewise_comments_api_for_missing_data(self):

        print("#"*50)
        print("Test case id: TCDC02")
        print("Test case name: Checking for missing data ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//display_issuewise_comments"

        # Prepare the data for the new user
        data = {}


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
        # Assert that the response status code is 200 (OK)
        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE3       ####
#############################################

    def test_display_issuewise_comments_api_for_issueStringdata(self):

        print("#"*50)
        print("Test case id: TCDC03")
        print("Test case name: Checking for issue_id is string or int  ")
        print("Inside the Test Case ")

        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000//display_issuewise_comments"

        # Prepare the data for the new user
        data = {"issue_id":"fsdfn"}


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

        print("case 3")
        # Assert that the response status code is 200 (OK)
        self.assertEqual(r.status_code,400)


#############################################
    ####        CASE4       ####
#############################################


    def test_display_issuewise_comments_api_for_Wrongdata(self):
            
            print("#"*50)
            print("Test case id: TCDC04")
            print("Test case name: Checking for incorrect data  ")
            print("Inside the Test Case ")
       
            # Define the API endpoint for adding a new user
            API_ENDPOINT_post = "http://127.0.0.1:5000//display_issuewise_comments"

            # Prepare the data for the new user
            data = {"issue_id":"fsdfn@123"}


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
            print('case4')
            # Assert that the response status code is 200 (OK)
            self.assertEqual(r.status_code,400)
            
if __name__ == "__main__":
    unittest.main()