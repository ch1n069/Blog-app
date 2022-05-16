from flask import redirect,render_template,url_for, flash
from app.main import main
from app import db , bcrypt
from app.models import User, Post
from app.auth.forms import RegistrationForm , LoginForm
from flask_login import login_user , current_user ,logout_user

#Views go here

    



@main.route('/register' , methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated():
        return redirect(url_for('main.index'))


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


    if current_user.is_authenticated:


        return redirect(url_for('main.index'))


    forms = LoginForm()


    if forms.validate_on_submit():
        user  = User.query.filter_by(email=forms.email.data).first()

        if user and bcrypt.check_password_hash(user.password, forms.password.data):
            login_user(user,remember=forms.remember.data)
            return redirect(url_for('main.index'))

        else:

            flash('Login unsuccessful please check email and password', 'danger')
           


    '''This is the home page for the application'''



    return render_template('login.html' ,title='Login' , forms=forms)
    



@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))






@main.route('/')
def index():


    '''This is the home page for the application'''



    return render_template('index.html')
    

