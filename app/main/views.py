from flask import redirect,render_template,url_for
from app.main import main
#Views go here
@main.route('/')
def index():


    '''This is the home page for the application'''
    return render_template('index.html')
    