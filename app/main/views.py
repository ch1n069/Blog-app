from flask import redirect,render_template,url_for, flash,request, abort
from app.main import main
from app import db , bcrypt
from app.models import User, Post
from app.auth.forms import RegistrationForm , LoginForm , UpdateAccountForm , PostForm
from flask_login import login_user , current_user ,logout_user, login_required

#Views go here

    

@main.route('/')
def index():
    page = request.args.get('page', 1 , type=int)

    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=1)


    '''This is the home page for the application'''



    return render_template('index.html', posts= posts)
    


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

    forms = PostForm()
    if forms.validate_on_submit():

        post = Post(title=forms.title.data, content=forms.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()

        flash('post has been created successfully.', 'success')
        return redirect(url_for('main.index'))


    return render_template('create_post.html' , title= "New post", forms=forms, legend='New post')
    


@main.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html' , title= "Post.title", post=post)



@main.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
def update_post(post_id):

    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    forms = PostForm()
    if forms.validate_on_submit():
        post.title = forms.title.data
        post.content = forms.content.data
        db.session.commit()
        flash('your post has been updated', 'success')
        return redirect(url_for('main.post', post_id=post.id ))

    elif request.method == 'GET':

        forms.title.data = post.title
        forms.content.data = post.content
    return render_template('create_post.html' , title= "update post", post=post ,forms=forms, legend='update post')


@main.route('/post/<int:post_id>/delete', methods=[ 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('main.index'))
