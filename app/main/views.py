from flask import redirect,render_template,url_for
from app.main import main
from auth.forms import RegistrationForm , LoginForm
#Views go here

    



@main.route('/register')
def register():

    form = RegistrationForm()


    '''This is the home page for the application'''



    return render_template('register.html' ,title='Register' , form=form)
    


@main.route('/login')
def login():

    form = LoginForm()


    '''This is the home page for the application'''



    return render_template('login.html' ,title='Login' , form=form)
    




@main.route('/')
def index():


    '''This is the home page for the application'''



    return render_template('index.html')
    