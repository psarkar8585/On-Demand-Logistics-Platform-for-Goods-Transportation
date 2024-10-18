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

@app.route('/')
def index():
    return render_template('index.html')  # The HTML file with the frontend code goes here.

@app.route('/get-price', methods=['POST'])
def get_price():
    location = request.form['location']
    destination = request.form['destination']
    
    # In real-world apps, call an API or calculate price dynamically here.
    # For now, we'll mock up a price based on static data.
    
    mock_price = 15.99  # Example static price
    return f"Estimated price from {location} to {destination} is ${mock_price:.2f}"

# @app.route('/user')

if __name__ == '__main__':
    app.run(debug=True)
