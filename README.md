# Makers BNB

## Description

This was a 5 day group project to sum up our Python Foundations course at Makers. In this, we worked from an existing code base and used Python, Flask, and Pytest. The concept is a clone of AirBNB where users are able to create an account, make listings, request bookings for other listings, and accept or deny requests on their own properties.

### Structure

This repo contains one application.

### Features

- Create account
- Login to account
- Create listings including image upload
- Make requests on properties
- Approve or deny requests on own properties
- Interactive calendar for booking dates

## Installation

### Set up the project

1. Fork this repository
2. Rename the fork
3. Clone the fork to their local machine

```
# Set up the virtual environment
; python -m venv makersbnb-venv

# Activate the virtual environment
; source makersbnb-venv/bin/activate 

# Install dependencies
(makersbnb-venv); pip install -r requirements.txt

# Install the virtual browser for testing
(makersbnb-venv); playwright install

# Create a test and development database
(makersbnb-venv); createdb YOUR_PROJECT_NAME
(makersbnb-venv); createdb YOUR_PROJECT_NAME_TEST

# Open lib/database_connection.py and change the database names
(makersbnb-venv); open lib/database_connection.py

# Run the tests (with extra logging)
(makersbnb-venv); pytest -sv

# Run the app
(makersbnb-venv); python app.py

# Now visit http://localhost:5001/index in your browser
```

## Authors and acknowledgment

This project was created by:
[Emily Sadler](https://github.com/EmiSadler)
[Benjamin Loveday](https://github.com/StrawberryScot)
[Etienne LeGoater](https://github.com/elegoater)
[Fliss Douglas](https://github.com/flissd1795)
[Kate Bancroft](https://github.com/ki-22)


