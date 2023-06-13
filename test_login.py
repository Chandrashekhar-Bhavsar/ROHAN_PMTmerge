import requests
import json
import unittest


class TestLoginApi(unittest.TestCase):
    def test_login_api_with_valid_credentials(self):
        print("#" * 50)
        print("Test case id: TCLA01")
        print("Test case name: Login API - Valid Credentials")
        print("Inside the Test Case")

        # Define the API endpoint for login
        API_ENDPOINT = "http://127.0.0.1:5000/login"

        # Prepare the data for login
        data = {
            "email_id": "rupa@gmail.com",
            "password": "123"
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for login
        r = requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=headers)

        # Print the response status code
        print("Response status code:", r.status_code)

        # Get the response content as JSON
        response_data = r.json()

        # Print the JSON response
        print("Response content:", response_data)
        print("")

        # Assert that the response status code is 200 (OK)
        self.assertEqual(r.status_code, 200)
        # Assert that the "Return" key in the response contains "login successful"
        

        

    def test_login_api_with_invalid_email(self):
        print("#" * 50)
        print("Test case id: TCLA02")
        print("Test case name: Login API - Invalid Email")
        print("Inside the Test Case")

        # Define the API endpoint for login
        API_ENDPOINT = "http://127.0.0.1:5000/login"

        # Prepare the data for login with invalid email
        data = {
            "email_id": "invalid@example.com",
            "password": "password123"
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for login
        r = requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=headers)

        # Print the response status code
        print("Response status code:", r.status_code)

        # Get the response content as JSON
        response_data = r.json()

        # Print the JSON response
        print("Response content:", response_data)
        print("")

        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(r.status_code, 400)
        # Assert that the "error" key in the response contains "Email id is not valid"
        



    def test_login_api_with_invalid_password(self):
        print("#" * 50)
        print("Test case id: TCLA03")
        print("Test case name: Login API - Invalid Password")
        print("Inside the Test Case")

        # Define the API endpoint for login
        API_ENDPOINT = "http://127.0.0.1:5000/login"

        # Prepare the data for login with invalid password
        data = {
            "email_id": "rupa@gmail.com.com",
            "password": "invalid_password"
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for login
        r = requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=headers)

        # Print the response status code
        print("Response status code:", r.status_code)

        # Get the response content as JSON
        self.assertEqual(r.status_code, 400)


if __name__ == "__main__":
    unittest.main()