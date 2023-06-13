import requests
import json
import unittest 


class TestGetWorkFlowApi(unittest.TestCase):

    def test_get_workflow_api_testing_by_giving_right_parameter(self):
        print("#"*50)
        print("Test case id: TCGWF01")
        print("Test case name: Checking for Right Parameter ")
        print("Inside the Test Case ")
        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000/GetWorkFlow"
        # Prepare the data for the new user
        data = {"wf":"w0","curr":"In_Progress","prev":"Done","succ":"In_review"}
        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        # Send a POST request to the API endpoint to add the new user
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)
        # Print the response status code
        print("response error code we got",r.status_code)
        # Get the response content as JSON
        pastebin_url = r.json()
        # Print the JSON response
        print("response content we got",pastebin_url)
        print(" ")
        # Assert that the response status code is 200 (OK)
        self.assertEqual(r.status_code, 200)

    def test_get_workflow_api_testing_by_giving_numeric_parameter(self):
        print("#"*50)
        print("Test case id: TCGWF02")
        print("Test case name: Checking for numeric parameter ")
        print("Inside the Test Case ")
        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000/GetWorkFlow"
        # Prepare the data for the new user
        data = {"wf":123,"curr":123,"prev":123,"succ":123}
        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        # Send a POST request to the API endpoint to add the new user
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)
        # Print the response status code
        print("response error code we got",r.status_code)
        # Get the response content as JSON
        pastebin_url = r.json()
        # Print the JSON response
        print("response content we got",pastebin_url)
        print(" ")
        # Assert that the response status code is 200 (OK)
        self.assertEqual(r.status_code,400) 

    def test_get_workflow_api_testing_by_giving_missing_parameter(self):
        print("#"*50)
        print("Test case id: TCGWF03")
        print("Test case name: Checking for missing parameter ")
        print("Inside the Test Case ")
        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000/GetWorkFlow"
        # Prepare the data for the new user
        data = {"wf":"w0","curr":"In_Progress","prev":"Done"}
        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        # Send a POST request to the API endpoint to add the new user
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)
        # Print the response status code
        print("response error code we got",r.status_code)
        # Get the response content as JSON
        pastebin_url = r.json()
        # Print the JSON response
        print("response content we got",pastebin_url)
        print(" ")
        # Assert that the response status code is 200 (OK)
        self.assertEqual(r.status_code,400)




if __name__ == "__main__":
    unittest.main()

