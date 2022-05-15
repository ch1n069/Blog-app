from app import create_app,db
from flask_script import Manager,Server
from app.models import User,role
from flask_migrate import Migrate,MigrateCommand
#Creating the app instance and loading the config option
app = create_app('development')
manager = Manager(app)
manager.add_command('runserver',Server)
migrate = add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app=app,db=db)
if _name_ == '_main_':
    manager.run()
        