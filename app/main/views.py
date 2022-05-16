from flask import redirect,render_template,url_for, flash
from app.main import main
from app import db , bcrypt
from app.models import User, Post
from app.auth.forms import RegistrationForm , LoginForm
#Views go here

    



@main.route('/register' , methods=['GET', 'POST'])
def register():

    forms = RegistrationForm()

    if forms.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(forms.password.data).decode('utf-8')
        user = User(username= forms.username.data, email=forms.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()


        flash('Your account has been created', 'success')
        return redirect(url_for('main.login'))

    '''This is the home page for the application'''



    return render_template('register.html' ,title='Register' , forms=forms)
    


@main.route('/login',  methods=['GET', 'POST'])
def login():

    forms = LoginForm()


    if forms.validate_on_submit():
        if forms.email.data == "user@test.com" and forms.password.data == "password":

            flash('You have been logged in', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Log in unsuccessful please check username and password', 'danger')
    



    '''This is the home page for the application'''



    return render_template('login.html' ,title='Login' , forms=forms)
    




@main.route('/')
def index():


    '''This is the home page for the application'''



    return render_template('index.html')
    