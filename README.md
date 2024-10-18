# On-Demand-Logistics-Platform-for-Goods-Transportation
# Goods Pickup and Delivery Web Application

This is a Flask web application for booking goods pickup and delivery services. Users can select pickup and drop-off locations, get an estimated price based on the distance, and book the service. The application also provides real-time booking status updates via the user dashboard.

## Features

- **User Authentication**: Users can log in or sign up for the service.
- **Pickup & Drop-off Selection**: Users can select a pickup location and a drop-off location through a UI select field.
- **Price Estimation**: Based on the distance between the pickup and drop-off locations, the estimated price is calculated using the Google Maps Distance Matrix API.
- **Booking**: Once the price is shown, the user can book the service, and the booking data is saved in the database.
- **Real-time Status Tracking**: Users can check their booking status in real-time from the dashboard.

## Setup Instructions

### Prerequisites

- Python 3.x
- PostgreSQL
- Google Maps API Key

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo-name.git
    cd your-repo-name
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your PostgreSQL database:

    - Ensure PostgreSQL is installed and running.
    - Create a new database with the name `user_system`.
    - Update the connection parameters (`hostname`, `database`, `username`, `password`, `port_id`) in the `get_db_connection()` function within `app.py`.

4. Set up your Google Maps API Key:

    - Replace `'YOUR_API_KEY_HERE'` with your actual API key in the `GOOGLE_MAPS_API_KEY` variable.

5. Run the application:

    ```bash
    python app.py
    ```

### API Routes

- **`/get-price` (POST)**: Calculates the estimated price for delivery based on the pickup and drop-off locations provided by the user. Uses Google Maps Distance Matrix API to calculate the distance and then applies a pricing logic to calculate the fare.

    **Parameters**:
    - `location`: The origin location (pickup).
    - `destination`: The destination location (drop-off).

    **Response**:
    - Estimated price based on the distance.

- **`/signup` (GET, POST)**: Handles user registration.

    **Parameters (POST)**:
    - `username`: Unique username.
    - `contact`: Contact number.
    - `password`: Account password.

    **Response**:
    - Success message if registration is successful, or an error if the username or contact number already exists.

- **`/user`, `/users`, `/diver`, `/divers`, `/dashboard`**: Renders respective HTML templates for login, signup, and user dashboard.

### Pricing Logic

The price is calculated using a base fare of $5.00 USD and a rate of $2.00 USD per kilometer. The formula is:

Where:
- `base_fare` is $5.00
- `per_km_rate` is $2.00

### Database

The app uses a PostgreSQL database to store user and booking information.

- **Database Schema**:
    - Users table with `username`, `contact`, and `password` fields.
    - Bookings table with information about pickup and drop-off locations, price, and booking status.

### File Structure

- **`app.py`**: The main Flask application.
- **`templates/`**: Contains HTML templates for rendering pages.
- **`static/`**: Contains static assets such as CSS and JavaScript files.
- **`requirements.txt`**: Contains the list of dependencies.

### Running the Application

Once the application is running, you can access it at:


- **User Dashboard**: `/dashboard` shows the real-time status of the user's bookings.

### Notes

- Remember to replace the placeholder `GOOGLE_MAPS_API_KEY` with your actual Google Maps API key.
- Password hashing and other security measures are not implemented in this example. Please add password hashing and proper authentication in production.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

