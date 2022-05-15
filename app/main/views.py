from flask import redirect,render_template
from . import main
#Views go here
@main.route('/')
def index():
    return render_template('index.html')
    