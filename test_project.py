import requests
import json
import unittest


class TestCreateProjectApi(unittest.TestCase):
    def test_valid_values(self):
        print("#" * 50)
        print("Test case id: TCCP01")
        print("Test case name: Create Project API")
        print("Inside the Test Case")

        # Define the API endpoint for creating a project
        API_ENDPOINT = "http://127.0.0.1:5000/create_project"

        # Prepare the data for creating a project
        data = {
               
        "project_name":"trail",
        "project_description":"trail2",
        "planned_sd":"2023-05-26 09:32:29",
        "planned_ed":"2023-05-26 09:32:29",
        "actual_sd":"2023-05-26 09:32:29",
        "actual_ed":"2023-05-26 09:32:29",
        "planned_hours":"30 minute",
        "actual_hours": "40 minute",
        "status": "To_do",
        "project_lead":"pratik",
        "client_name":"tcs",
        "risk":"high",
        "mitigation":"no"

        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for creating a project
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
       


    def test_missing_values(self):
        print("#" * 50)
        print("Test case id: TCCP02")
        print("Test case name: Create Project API - Missing Values")
        print("Inside the Test Case")

        # Define the API endpoint for creating a project
        API_ENDPOINT = "http://127.0.0.1:5000/create_project"

        # Prepare the data for creating a project with missing values
        data = {
               
        "project_name":"trail",
        "project_description":"trail2",
        "planned_sd":"2023-05-26 09:32:29",
        "planned_ed":"2023-05-26 09:32:29",
        "actual_sd":"2023-05-26 09:32:29",
        "actual_ed":"2023-05-26 09:32:29",
        "planned_hours":"30 minute",
        "actual_hours": "40 minute"
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for creating a project
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

         


if __name__ == '__main__':
    unittest.main()
