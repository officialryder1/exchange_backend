# Django Exchange Setup 

This guide outlines the steps to set up and run the Django project locally.

## Prerequisites

Ensure you have the following installed on your machine:

- **Python 3.8+**: [Download and install Python](https://www.python.org/downloads/)
- **pip**: Python package manager (comes with Python 3.4+)
- **virtualenv**: (Optional but recommended) for creating a virtual environment
<!-- - **PostgreSQL** (if using a PostgreSQL database) -->

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/officialryder1/exchange_backend.git
cd your-project
```


### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies 

```bash
pip install -r requirements.txt
```
### 4 Configure Environment Variable

Create a .env file in the project root directory and add the following variables:

EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password

DM me for the email configuration if needed, but if you can setup a gmail smtp it will be preferable

### Set Up the Database Migrations

Ensure your database is running and then run the following commands to apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6 Create a SuperUser

Create an admin user to access the Django admin interface.(optional)

```bash
python manage.py createsuperuser
```

### 7 Run the Development Server
Start the Django development server.

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your web browser to see the project in action.

### 8. Get the Endpoints Documentation using OpenAi

Visit http://127.0.0.1:8000/api/swagger/ in your web browser to see the endpoints.



### Key Sections Explained:
1. **Prerequisites**: Lists necessary software and tools.
2. **Getting Started**: Detailed steps for setting up the project.
3. **Environment Variables**: Guide to setting up environment-specific configurations.
4. **Database Setup**: Instructions for initializing the database.
5. **Running the Project**: Steps to run the Django server and access the project.
6. **Documentation and Contact**: Information about API documentation and how to reach out for support.

This `README.md` provides a clear, structured guide to setting up and running your Django project.
