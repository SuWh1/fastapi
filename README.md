# FastAPI Application

This is a FastAPI application that implements a basic RESTful API with user authentication, post creation, and voting functionalities. It uses PostgreSQL as the database and supports JWT for authentication.

## How to Run

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/fastapi-app.git
cd fastapi-app
```

### 2. Set Up the Environment
Make sure you have Python and pip installed. If you haven't installed them yet, you can download them from the official Python website.

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
1. Create a PostgreSQL database and user.
2. Update the database connection settings in the .env file:
```bash
database_hostname=localhost
database_port=5432
database_username=your_username
database_password=your_password
database_name=your_database_name
secret_key=your_secret_key
algorithm=HS256
access_token_expire_minutes=30
```
Replace your_username, your_password, your_database_name, and your_secret_key with your actual database credentials and a secret key for JWT.

### 5. Run the Application
To run the FastAPI application, execute the following command in your terminal:

```bash
uvicorn app.main:app --reload
```
You can now access the API documentation at http://127.0.0.1:8000/docs.
