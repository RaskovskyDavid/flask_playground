from flask import Flask
from markupsafe import escape
app = Flask(__name__)
#Decoradores Decorators
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper
def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper
def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center;">Hello, World!</h1>'
@app.route('/bye')
def bye():
    return 'bye'

@app.route('/brappper')
@make_bold
@make_emphasis
@make_underlined
def brappper():
    return 'wrappper'    

@app.route('/user/<username>/<int:number>')
def show_user_profile(username,number):
    # show the user profile for that user
    return f"{number}"'User %s' % escape(username)
