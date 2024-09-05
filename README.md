#### Project Overview

This project is a FastAPI-based API application that manages tasks, companies, and users. It provides endpoints for creating, reading, updating, and deleting tasks, companies, and users. The project structure includes routers for users, companies, and tasks, each containing specific endpoints for different operations.

#### Installation

1.  git clone https://github.com/VanCongBang/python-fast-api-assignment.git
    
2.  pip install -r requirements.txt
    

#### Usage

1.  uvicorn app.main:app --reload
    
2.  Access the API documentation at http://127.0.0.1:8000/docs to interact with the available endpoints.
    

#### Project Structure

*   app/: Contains the main application code.
    
    *   main.py: Entry point of the FastAPI application.
        
    *   routers/: Contains router modules for tasks, companies, and users.
        
        *   tasks.py: Defines endpoints for tasks.
            
        *   companies.py: Defines endpoints for companies.
            
        *   users.py: Defines endpoints for users.
            
    *   models/: Contains database models.
        
    *   schemas/: Contains Pydantic models for request and response validation.
        
    *   database.py: Configures the database connection.
        
    *   auth/: Contains authentication-related functions.
        
*   requirements.txt: Lists the project dependencies.
    

#### Endpoints

*   **Users**
    
    *   POST /users/: Create a new user.
        
    *   GET /users/{user\_id}: Get user details by ID.
        
    *   GET /users/: Get a list of users.
        
    *   GET /users/me: Get current user details.
        
*   **Companies**
    
    *   POST /companies/: Create a new company.
        
    *   GET /companies/{company\_id}: Get company details by ID.
        
    *   GET /companies/: Get a list of companies.
        
*   **Tasks**
    
    *   POST /tasks/: Create a new task.
        
    *   GET /tasks/{task\_id}: Get task details by ID.
        
    *   GET /tasks/: Get a list of tasks.
        

#### API Configuration

The FastAPI application is configured to include routers for users, companies, and tasks. Each router is prefixed with the corresponding entity name and tagged accordingly.

#### Authentication

*   The API uses OAuth2 for user authentication.
    
*   To obtain an access token, send a POST request to /token with valid credentials.
    

#### Error Handling

*   The API returns appropriate HTTP status codes and error messages for different scenarios.
    

#### Testing

*   Unit tests can be found in the tests/ directory.
    
*   pytest
    

#### Deployment

*   Ensure to configure the appropriate database settings before deploying the application.
    
*   Deploy the application using a suitable ASGI server like gunicorn.
    

#### Contributing

*   Fork the repository, make your changes, and submit a pull request.
    
*   Follow the project's coding style and guidelines.
    

#### License

This project is licensed under the MIT License.

### Docker Deployment Guide

To run the FastAPI application in a Docker container, follow these steps:

1.  FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 COPY ./app /app
    
2.  docker build -t my-fastapi-app .
    
3.  docker run -d --name my-fastapi-container -p 80:80 my-fastapi-app
    
4.  Access the FastAPI application at http://localhost/docs in your browser.
    

This Docker deployment guide will containerize your FastAPI application and make it accessible through a Docker container.
