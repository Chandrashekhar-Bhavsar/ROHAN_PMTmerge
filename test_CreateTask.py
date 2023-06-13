import requests
import json
import unittest


class TestCreateTaskApi(unittest.TestCase):
    def test_valid_values(self):
        print("#" * 50)
        print("Test case id: TCCCT01")
        print("Test case name: Create Task API")
        print("Inside the Test Case")

        # Define the API endpoint for creating a task
        API_ENDPOINT = "http://127.0.0.1:5000/create_tasks"

        # Prepare the data for creating a task
        data = {
            "issue_id": 3001,
            "description": "Task description",
            "status": "To_Do",
            "task_sd": "2023-06-02",
            "task_ed": "2023-07-03",
            "planned_hours": 4,
            "actual_hours": 2,
            "priority": "high"
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for creating a task
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
        print("Test case id: TCCCT02")
        print("Test case name: Create Task API - Missing Values")
        print("Inside the Test Case")

        # Define the API endpoint for creating a task
        API_ENDPOINT = "http://127.0.0.1:5000/create_tasks"

        # Prepare the data for creating a task with missing values
        data = {
            "issue_id": 3002,
            "description": "abcd",
            "status": "To_do",
            "task_sd": "2023-06-03",
            "task_ed": "2023-05-26 09:32:29",
            "planned_hours": 4,
            "actual_hours": 2
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for creating a task
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
        test_case_id = "TCCT03"
        test_case_name = "Create Task API - Invalid Data Type"

        print("#" * 50)
        print("Test case id:", test_case_id)
        print("Test case name:", test_case_name)
        print("Inside the Test Case")

        # Define the API endpoint for creating a task
        API_ENDPOINT = "http://127.0.0.1:5000/create_tasks"

        # Prepare the data for creating a task with invalid data types
        data = {
            "issue_id": 3001,
            "description":"hello",
            "status": 123,
            "task_sd": "2023-06-01",
            "task_ed": "2023-06-02",
            "planned_hours": "2 hours",
            "actual_hours": "5 hours ",  # Invalid data type
            "priority": "High"
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint for creating a task
        r = requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=headers)

        # Print the response status code
        print("Response status code:", r.status_code)

        # Get the response content as JSON
        response_data = r.json()

        # Print the JSON response
        print("Response content:", response_data)
        print("")

        # Assert that the response status code is 500 (Bad Request)
        self.assertEqual(r.status_code, 500)





if __name__ == '__main__':
    unittest.main()
