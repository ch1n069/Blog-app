from flask import redirect,render_template,url_for, flash
from app.main import main
from app.auth.forms import RegistrationForm , LoginForm
#Views go here

    



@main.route('/register' , methods=['GET', 'POST'])
def register():

    forms = RegistrationForm()

    if forms.validate_on_submit():
        flash(f'Account created for {forms.username.data}!!', 'success')
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
    