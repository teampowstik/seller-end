from flask import url_for, redirect, render_template, flash, request, Blueprint
from flask_login import login_required, current_user, login_user, logout_user
from flaskFile.models import User
from flaskFile import bcrypt
from flaskFile.user.forms import LoginForm

user = Blueprint('user', __name__)

@user.route("/login/<int:ps_id>", methods=['GET', 'POST'])
def login(ps_id: int):
    if current_user.is_authenticated:
        return redirect(url_for('general.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).filter_by(ps_id = ps_id).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login successful', 'info')
            nextPage = request.args.get('next', 'home')
            return redirect(nextPage)
        else:
            flash('Login Unsuccessful. Please check details', 'danger')
    return render_template('user/login.html', title='Login', form=form)

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('general.home'))

@user.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    imageFile = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('user/account.html', title=current_user.username, imageFile=imageFile)










