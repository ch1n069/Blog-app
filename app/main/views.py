from flask import redirect,render_template,url_for, flash,request
from app.main import main
from app import db , bcrypt
from app.models import User, Post
from app.auth.forms import RegistrationForm , LoginForm , UpdateAccountForm , PostForm
from flask_login import login_user , current_user ,logout_user, login_required

#Views go here

    



@main.route('/register' , methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
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
            next_page = request.args.get('next')

            return redirect(next_page) if next_page else redirect (url_for('main.index'))

        else:

            flash('Login unsuccessful please check email and password', 'danger')
           


    '''This is the home page for the application'''



    return render_template('login.html' ,title='Login' , forms=forms)
    



@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/account',methods=['GET', 'POST'] )
@login_required
def account():
    forms = UpdateAccountForm()
    if forms.validate_on_submit():
        current_user.username = forms.username.data
        current_user.email = forms.email.data
        db.session.commit()
        flash('your account has been updated', 'success')
        return redirect(url_for('main.account'))

    elif request.method == 'GET':
        forms.username.data = current_user.username
        forms.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file, forms=forms)

    return render_template('account.html', title='Account ', image_file= image_file,forms=forms)




@main.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():

    forms= PostForm()
    if forms.validate_on_submit():
        flash('post has been created')
        return redirect(url_for('main.index'))




    '''This is the home page for the application'''



    return render_template('create_post.html' , title= "New post", forms=forms)
    




@main.route('/')
def index():


    '''This is the home page for the application'''



    return render_template('index.html')
    

