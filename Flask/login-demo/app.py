
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import configs
from models import query_user, User

app = Flask(__name__)
app.config.from_object(configs)
Bootstrap(app)

# login management
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Please login'
login_manager.init_app(app)

# user loader
@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id

        return curr_user

# home page
@app.route('/')
# @login_required
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form.get('userid')
        password = request.form.get('password')

        user = query_user(userid)
        if user is not None and password == user['password']:
            curr_user = User()
            curr_user.id = userid

            login_user(curr_user)

            return redirect(url_for('index'))
        else:
            flash('Incorrect user id or password.')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logout successfully.'


if __name__ == '__main__':
    app.run()
