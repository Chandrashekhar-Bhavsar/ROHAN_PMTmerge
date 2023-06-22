import requests
import json
import unittest


class TestUpdateProjectApi(unittest.TestCase):
    def test_valid_values(self):
        test_case_id = "TCUP01"
        test_case_name = "Update Project API - Valid Values"

        print("#" * 50)
        print("Test case id:", test_case_id)
        print("Test case name:", test_case_name)
        print("Inside the Test Case")

        # Define the API endpoint for updating a project
        API_ENDPOINT = "http://127.0.0.1:5000/update_project"

        # Prepare the data for updating a project
        data = {
             
        "Project_ID" :118,
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

        # Send a POST request to the API endpoint for updating a project
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
        test_case_id = "TCUP02"
        test_case_name = "Update Project API - Missing Values"

        print("#" * 50)
        print("Test case id:", test_case_id)
        print("Test case name:", test_case_name)
        print("Inside the Test Case")

        # Define the API endpoint for updating a project
        API_ENDPOINT = "http://127.0.0.1:5000/update_project"

        # Prepare the data for updating a project with missing values
        data = {
             
       "Project_ID" :118,
        "project_name":"trail",
        "project_description":"trail2",
        "planned_sd":"2023-05-26 09:32:29",
        "planned_ed":"2023-05-26 09:32:29",
        "actual_hours": "40 minute",
        "status": "To_do",
        "project_lead":"pratik",
        "client_name":"tcs",
        "risk":"high",
        "mitigation":"no"
}

        

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for updating a project
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

    def test_invalid_data_type(self):
        test_case_id = "TCUP03"
        test_case_name = "Update Project API - Invalid Data Type"

        print("#" * 50)
        print("Test case id:", test_case_id)
        print("Test case name:", test_case_name)
        print("Inside the Test Case")

        # Define the API endpoint for updating a project
        API_ENDPOINT = "http://127.0.0.1:5000/update_project"

        # Prepare the data for updating a project with invalid data types
        data = {
            
       "Project_ID" :"118",
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
        "client_name":123, # invalid data type
        "risk":"high",
        "mitigation":"no"
}


        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for updating a project
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



    def test_length_limit(self):
        test_case_id = "TCUP05"
        test_case_name = "Update Project API - Length Limit"

        print("#" * 50)
        print("Test case id:", test_case_id)
        print("Test case name:", test_case_name)
        print("Inside the Test Case")

        # Define the API endpoint for updating a project
        API_ENDPOINT = "http://127.0.0.1:5000/update_project"

        # Prepare the data for updating a project with values exceeding length limits
        data = {
            "Project_ID" :118,
        "project_name":"trail" * 500, # length is predefined
        "project_description":"trail2"*500,
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
        "mitigation":"no"}

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for updating a project
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

    def test_empty_values(self):
        test_case_id = "TCUP06"
        test_case_name = "Update Project API - Empty Values"

        print("#" * 50)
        print("Test case id:", test_case_id)
        print("Test case name:", test_case_name)
        print("Inside the Test Case")

        # Define the API endpoint for updating a project
        API_ENDPOINT = "http://127.0.0.1:5000/update_project"

        # Prepare the data for updating a project with empty values
        data = {
                "Project_ID" :118,
        
        "project_description":"trail2",
        "planned_sd":"2023-05-26 09:32:29",
        "planned_ed":"2023-05-26 09:32:29",
        "actual_sd":"2023-05-26 09:32:29",
        "actual_ed":"2023-05-26 09:32:29",
        "planned_hours":"30 minute",
        "actual_hours": " ", # Empty Value
        "status": "To_do",
        "project_lead":"pratik",
        "client_name":"tcs",
        "risk":"high",
        "mitigation":"no"
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for updating a project
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
