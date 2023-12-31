import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import Spacerepository
from lib.spaces import Spaces
from lib.users import User
from lib.users_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')
@app.route('/newuser/new', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/newuser', methods=['GET', 'POST'])
def new_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    if request.method == 'POST':
        username = request.form['username']
        fullname = request.form['fullname']
        password = request.form['password']
        user = User(None, username, fullname, password)
        repository.create(user)
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        connection = get_flask_database_connection(app)
        result = connection.execute('SELECT * FROM users where username = %s AND password = %s', (username, password,))
        user = result
        if user:
            return redirect(url_for('all_spaces'))
        else:
            message = 'please enter correct username and password'
    else:
        return render_template('login.html', message=message)
    
@app.route('/spaces', methods = ['GET'])
def all_spaces():
    connection = get_flask_database_connection(app)
    repository = Spacerepository(connection)
    return ', '.join([
            str(space) for space in repository.all()
        ])

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
