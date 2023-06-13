import requests
import json
import unittest


class TestUpdateTaskApi(unittest.TestCase):
    def test_valid_values(self):
        test_case_id = "TCUT01"
        test_case_name = "Update Task API - Valid Values"

        print("#" * 50)
        print("Test case id:", test_case_id)
        print("Test case name:", test_case_name)
        print("Inside the Test Case")

        # Define the API endpoint for updating a task
        API_ENDPOINT = "http://127.0.0.1:5000/update_tasks"

        # Prepare the data for updating a task
        data = {
             "task_id":"5010",  
        "issue_id": "3001",
        "description": "hello task",
        "status": "In Review",
        "task_sd": "2023-06-01",
        "task_ed": "2023-06-02",
        "planned_hours": "40 hrs",
        "actual_hours": "90 hrs",
        "priority": "high"
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for updating a task
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
        test_case_id = "TCUT02"
        test_case_name = "Update Task API - Missing Values"

        print("#" * 50)
        print("Test case id:", test_case_id)
        print("Test case name:", test_case_name)
        print("Inside the Test Case")

        # Define the API endpoint for updating a task
        API_ENDPOINT = "http://127.0.0.1:5000/update_tasks"

        # Prepare the data for updating a task with missing values
        data = {
            "task_id": "5011",
            "description": "Updated task description",
            "status": "In Progress",
            # Missing values for other required fields
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for updating a task
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
        test_case_id = "TCUT03"
        test_case_name = "Update Task API - Invalid Data Type"

        print("#" * 50)
        print("Test case id:", test_case_id)
        print("Test case name:", test_case_name)
        print("Inside the Test Case")

        # Define the API endpoint for updating a task
        API_ENDPOINT = "http://127.0.0.1:5000/update_tasks"

        # Prepare the data for updating a task with invalid data types
        data = {
          "task_id":5010,  
        "issue_id": 3001,
        "description": "hello task",
        "status": "In Review",
        "task_sd": "2023-06-01",
        "task_ed": "2023-06-02",
        "planned_hours": "40 hrs",
        "actual_hours": "90 hrs",
        "priority": 123  # Invalid data type
        
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for updating a task
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
        test_case_id = "TCUT04"
        test_case_name = "Update Task API - Length Limit"

        print("#" * 50)
        print("Test case id:", test_case_id)
        print("Test case name:", test_case_name)
        print("Inside the Test Case")

        # Define the API endpoint for updating a task
        API_ENDPOINT = "http://127.0.0.1:5000/update_tasks"

        # Prepare the data for updating a task with values exceeding length limits
        data = {
            "task_id":"5010",  
        "issue_id": "3001",
        "description": "hello task"*8000,
        "status": "In Review",
        "task_sd": "2023-06-01",
        "task_ed": "2023-06-02",
        "planned_hours": "40 hrs",
        "actual_hours": "90 hrs",
        "priority": "123" 
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for updating a task
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
  
