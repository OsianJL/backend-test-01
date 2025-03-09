backend-test-01 API
This API was developed using Flask and various extensions to handle authentication, database management, migrations, and more. It uses PostgreSQL as the database, which is run in a Docker container, and it supports user management, email confirmation, password recovery, user profiles, public messages, and chat functionality. Additionally, a Flask‑Admin panel is available to manage and inspect the data.

Technologies Used

Flask: Python web framework.
Flask-SQLAlchemy: ORM for database interactions.
Flask-Migrate: Database migration management.
Flask-JWT-Extended: JWT-based authentication.
Flask-Bcrypt: Password hashing.
Flask-Mail: (Optional) Email sending.
Flask-RESTful: Build RESTful API endpoints.
Flask-Admin: Administration panel for the API.
python-dotenv: Loads environment variables from a .env file.
psycopg2-binary: PostgreSQL database adapter.
itsdangerous: Token generation and verification.


Cloning the Project from GitHub
To clone the repository, run the following commands in your terminal:
bashCopygit clone https://github.com/your_username/backend-test-01.git
cd backend-test-01
(Replace your_username with your GitHub username and update the URL as needed.)
Installation

Create and activate a virtual environment:
For Windows (using Bash):
bashCopypython -m venv venv
source venv/Scripts/activate

Install the dependencies:
bashCopypip install -r requirements.txt


Configuring the Database with Docker
The API uses a PostgreSQL database running in a Docker container. If the database is not running, you can start a new container using the command below:
bashCopydocker run --name postgres_backend_test_01 -e POSTGRES_USER=osiapp -e POSTGRES_PASSWORD=osiapp25 -e POSTGRES_DB=backend_test_01_db -p 5433:5432 -d postgres:16

This command starts a PostgreSQL container on port 5433 of your machine.
Ensure that your .env file has the following (or similar) configuration:

dotenvCopyDATABASE_URL=postgresql://osiapp:osiapp25@localhost:5433/backend_test_01_db
To restart or remove the container, use:
bashCopydocker rm -f postgres_backend_test_01
or, if using docker-compose:
bashCopydocker-compose down -v
docker-compose up -d
Running the Server

Database Migrations (First Migration and Future Migrations):
Make sure the FLASK_APP variable is set:
bashCopyexport FLASK_APP=run.py
Then, if this is the first time:
bashCopyflask db init
flask db migrate -m "Initial migration: create users table"
flask db upgrade

Start the Application:
bashCopypython run.py
The application will run in development mode (debug=True) and can be accessed at http://127.0.0.1:5000/.

Flask-Admin Panel
The API includes a Flask‑Admin panel to manage and inspect your data. Once the application is running, you can access the admin panel by navigating to:
http://127.0.0.1:5000/admin