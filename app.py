import os
from lib.users import User
from lib.homes import Home
from lib.users_repository import UserRepository
from lib.homes_repository import HomesRepository
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

def start_session():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    repository = UserRepository(connection)
    user_as_dict = repository.find_user(email)
    user_as_object = User(user_as_dict['id'], user_as_dict['username'], user_as_dict['email'], user_as_dict['password'])
    session['users_id'] = user_as_object.id
    session['username'] = user_as_object.username

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    repository = HomesRepository(connection)
    homes = repository.all_homes()
    return render_template('index.html', homes=homes)

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Get email and password from the form
    connection = get_flask_database_connection(app)
    email = request.form['email']
    password = request.form.get('password') 
    repository = UserRepository(connection)
    if repository.check_password(email, password):
        start_session()
        return redirect(url_for('get_index')) # Redirect to the main page after successful login
    else:
        return redirect('/create_account') # Redirect to create account page if email not found

@app.route('/create_account', methods=['GET'])
def get_create_account():
    return render_template('create_account.html')

@app.route('/create_account', methods = ['POST'])
def create_new_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    new_user = User(None, request.form['username'], request.form['email'], request.form['password'])
    if not new_user.is_valid():
        return render_template('create_account.html', new_user=new_user, errors=new_user.generate_errors()), 400
    repository.create_user(new_user.username, new_user.email, new_user.password)
    return redirect(url_for('get_login'))

@app.route('/logout', methods=['GET'])
def get_logout():
    session.clear()  # Clears all session data
    return redirect(url_for('get_login'))

@app.route('/create_home', methods=['GET'])
def get_create_home():
    return render_template('create_home.html')

@app.route('/show_home/<id>', methods=['GET'])
def get_show_home(id):
    connection = get_flask_database_connection(app)
    repository = HomesRepository(connection)
    home = repository.find(id)
    user = UserRepository(connection).get_username(home.user_id)
    user = user.get('username')
    booked_dates = repository.fetch_booked_dates(id)
    return render_template('show_home.html', home=home, home_owner=user, month=range(1, 32), booked_dates=booked_dates)

@app.route("/show_home/<id>", methods=["POST"])
def book(id):
    if request.method == "POST":
        start_date = request.form.get("day")
        end_date = request.form.get("day")

        if not start_date or not end_date:
            return "Please select both dates."

        # Ensure the end date is not earlier than the start date
        if start_date > end_date:
            return "Error: Check-out date must be after check-in date."

        # Perform booking logic here (e.g., save to database, check availability, etc.)
        return f"Booking successful from {start_date} to {end_date}!"
    
    return render_template("index.html")

@app.route('/all_requests', methods=['GET'])
def get_all_requests():
    connection = get_flask_database_connection(app)
    repository = HomesRepository(connection)
    users_id = session.get('users_id') 
    homes = repository.find_all(users_id)
    return render_template('all_requests.html', homes=homes)

@app.route('/auth_requests', methods=['GET'])
def get_auth_requests():
    return render_template('auth_request.html')

@app.route('/create_home', methods = ['POST'])
def create_home():
    users_id = session.get('users_id') 
    if not users_id:
        return redirect(url_for('get_login'))
    connection = get_flask_database_connection(app)
    repository = HomesRepository(connection)
    title = request.form['title']
    description = request.form['description']
    location = request.form['location']
    price_per_night = request.form['price_per_night']
    home = Home(None, title, description, location, price_per_night, int(users_id))
    if not home.is_valid():
        return render_template('create_home.html', home=home, errors=home.generate_errors()), 400
    repository.create_home(title, description, location, price_per_night, int(users_id))
    return redirect(url_for('get_index'))



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.secret_key = os.environ.get('SECRET_KEY', 'super secret key')
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
