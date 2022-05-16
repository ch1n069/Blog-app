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
    


@main.route('/login')
def login():

    form = LoginForm()


    '''This is the home page for the application'''



    return render_template('login.html' ,title='Login' , form=form)
    




@main.route('/')
def index():


    '''This is the home page for the application'''



    return render_template('index.html')
    