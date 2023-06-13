import requests
import json
import unittest 


class TestStatusUpdate(unittest.TestCase):

    def test_Status_api_testing_by_giving_right_parameter(self):
        print("#"*50)
        print("Test case id: TCGWF01")
        print("Test case name: Checking for Right Parameter ")
        print("Inside the Test Case ")
        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000/StatusUpdate"
        # Prepare the data for the new user
        data = {"wf":"w0","curr":"In_Progress","prev":"Done","succ":"In_review"}
        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        # Send a POST request to the API endpoint to add the new user
        r = requests.get(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)
        # Print the response status code
        print("response error code we got",r.status_code)
        # Get the response content as JSON
        pastebin_url = r.json()
        # Print the JSON response
        print("response content we got",pastebin_url)
        print(" ")
        # Assert that the response status code is 200 (OK)
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main()

