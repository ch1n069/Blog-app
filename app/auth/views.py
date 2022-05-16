from flask import redirect,render_template,url_for
from app.auth import auth
#Views go here
@auth.route('/')
def login():


    '''This is the home page for the application'''


    
    return render_template('auth.register')
    