from flask import Flask, request, redirect, url_for, render_template, abort
import psycopg2

app = Flask(__name__)

# Database connection parameters
hostname = 'localhost'
database = 'user_system'
username = 'postgres'
password = 'root'
port_id = 5432

def get_db_connection():
    """Establish and return a database connection."""
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=password,
            port=port_id
        )
        print("Connection to the database established successfully.")
        return conn
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        return None

# Route to test the database connection
@app.route('/')
def home():
    conn = get_db_connection()
    if conn:
        return "Connected to the database successfully!"
    else:
        return "Failed to connect to the database."

if __name__ == '__main__':
    app.run(debug=True)
