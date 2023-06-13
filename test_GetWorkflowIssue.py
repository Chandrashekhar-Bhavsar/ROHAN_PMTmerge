import requests
import json
import unittest 


class TestGetWorkflowIssueApi(unittest.TestCase):
    def test_get_workflow_issue_api_testing_by_giving_missing_parameter(self):
        print("#"*50)   
        print("Test case id: TCGWFI02")
        print("Test case name: Checking for MISSING Parameter ")
        print("Inside the Test Case ")
        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000/GetWorkflowIssue"
        # Prepare the data for the new user
        data = {"wfn":"w1"}
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
        self.assertEqual(r.status_code, 400)

    def test_get_workflow_issue_api_testing_by_giving_right_parameter(self):
        print("#"*50)
        print("Test case id: TCGWFI01")
        print("Test case name: Checking for Right Parameter ")
        print("Inside the Test Case ")
        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000/GetWorkflowIssue"
        # Prepare the data for the new user
        data = {"issueid":3000,"wfn":"w1"}
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


    def test_get_workflow_issue_api_testing_by_giving_wrong_dataype_entry_parameter(self):
        print("#"*50)
        print("Test case id: TCGWFI03")
        print("Test case name: Checking for wrong datatype Parameter ")
        print("Inside the Test Case ")
        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000/GetWorkflowIssue"
        # Prepare the data for the new user
        data = {"issueid":"3000","wfn":123}
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
        self.assertEqual(r.status_code, 400)

   


if __name__ == "__main__":
    unittest.main()

