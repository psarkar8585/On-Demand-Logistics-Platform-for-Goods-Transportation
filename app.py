import requests  # Import the requests module for making external HTTP requests
from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)
GOOGLE_MAPS_API_KEY = 'YOUR_API_KEY_HERE'

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
        return render_template('index.html')
    else:
        return "Failed to connect to the database."

@app.route("/user")
def user():
    return render_template('userlogin.html')

@app.route('/get-price', methods=['POST'])
def get_price():
    location = request.form['location']
    destination = request.form['destination']
    
    # Call Google Maps Distance Matrix API
    distance_data = get_distance(location, destination)
    
    if not distance_data:
        return f"Could not calculate distance between {location} and {destination}. Please try again."

    # Calculate the price based on distance
    distance_in_km = distance_data['distance']
    estimated_price = calculate_price(distance_in_km)
    
    return f"Estimated price from {location} to {destination} is ${estimated_price:.2f}"

def get_distance(origin, destination):
    """Call Google Maps API to get distance between two locations."""
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    
    params = {
        'origins': origin,
        'destinations': destination,
        'key': GOOGLE_MAPS_API_KEY,
        'units': 'metric'
    }
    
    # Use requests.get instead of request.get to make the API call
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    
    if data['status'] != 'OK':
        return None
    
    # Extract distance in kilometers from the response
    distance_info = data['rows'][0]['elements'][0]
    
    if distance_info['status'] != 'OK':
        return None
    
    distance_in_meters = distance_info['distance']['value']
    distance_in_km = distance_in_meters / 1000  # Convert meters to kilometers
    
    return {'distance': distance_in_km}

def calculate_price(distance_km):
    """Calculate price based on distance (example pricing logic)."""
    base_fare = 5.00  # Base fare in USD
    per_km_rate = 2.00  # Rate per kilometer in USD
    
    price = base_fare + (distance_km * per_km_rate)
    return price

if __name__ == '__main__':
    app.run(debug=True)
