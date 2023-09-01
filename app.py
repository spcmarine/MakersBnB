import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import Spacerepository
from lib.spaces import Spaces

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/spaces', methods = ['GET'])
def all_spaces():
    connection = get_flask_database_connection(app)
    repository = Spacerepository(connection)
    return ', '.join([
            str(space) for space in repository.all()
        ])


# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
