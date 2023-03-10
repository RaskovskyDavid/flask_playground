from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center;">Hello, World!</h1>'
@app.route('/bye')
def bye():
    return 'bye'
@app.route('/user/<username>/<int:number>')
def show_user_profile(username,number):
    # show the user profile for that user
    return f"{number}"'User %s' % escape(username)
