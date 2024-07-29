# Employee API

This is a RESTful API service for managing employees made by following Operations Task for AI Labs

## Project Structure

my_rest_api/
├── app/
│ ├── init.py
│ ├── config.py
│ ├── models.py
│ ├── routes.py
├── tests/
│ ├── init.py
│ ├── test_api.py
├── venv/
├── Dockerfile
├── requirements.txt
├── setup.bat
├── init_db.py
├── run.bat
├── test.bat
├── run.py

## Setup

### Using Makefile

1. **Setup the project:**
    ```sh
    make setup
    ```

2. **Run the application:**
    ```sh
    make run
    ```

3. **Run the tests:**
    ```sh
    make test
    ```

### Batch Files

1. **Setup the project:**
    ```sh
    ./setup.bat
    ```

2. **Run the application:**
    ```sh
    ./run.bat
    ```

3. **Run the tests:**
    ```sh
    ./test.bat
    ```

### **What is being tested while running the tests***
    setUp and tearDown Methods: testing the setUp and tearDown of the project

    test_index: Testing the Index to make sure it returns the correct number and message

    test_add_employee: POST /employee route test to add a new employee and checks if the response is correct

    test_get_employees: GET /employees route test to retrieve all employees and checks if the response contains the added employee.

    test_get_employee: GET /employee/<id> route test to retrieve a specific employee by ID.

    test_update_employee: PUT /employee/<id> route test to update an existing employee and checks if the response is correct.

    test_delete_employee: DELETE /employee/<id> route test to delete an employee and verifies that the employee no longer exists.

    test_populate: POST /populate route test to populate the database with sample data and checks if the response contains 5 employees.

### Using Docker

1. **Make sure Docker is installed on your device.**
    In case it is not, please visit the following website and install it:
    https://www.docker.com/

1. **Build the Docker image:**
    ```sh
    docker build -t employee-api .
    ```

2. **Run the Docker container:**
    ```sh
    docker run -p 5000:5000 employee-api
    ```

### Endpoints

- `GET /`: Welcome message.
- `GET /employees`: Retrieve all employees.
- `GET /employee/<id>`: Retrieve a specific employee by ID.
- `POST /employee`: Add a new employee.
- `PUT /employee/<id>`: Update an existing employee.
- `DELETE /employee/<id>`: Delete an employee.
- `POST /populate`: Populate the table with sample data.


By following these steps, you should be able to automate the population of your database when running the Docker container. If you encounter any issues or have further questions, please let me know!

Completed by Rokas Klimasauskas


