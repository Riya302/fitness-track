from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from . import mydb
mycursor = mydb.cursor()
import json


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.statistics'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/delete_account')
@login_required
def delete_account():
    mycursor.execute(f'DELETE FROM user_info WHERE id="{current_user.Userid}"')
    print(mycursor)
    mydb.commit()
    id = current_user.id
    logout_user()
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            mycursor.execute('SELECT count(id) from user_info')
            userID = "USR(N)0"
            for i in mycursor:
                if i[0]==None:
                    pass
                else:
                    userID = "USR(N)"+str(int(i[0]))
            mycursor.execute(f'INSERT INTO user_info (id,fname,gender,height,weight) VALUES ("{userID}","{first_name}",3,0,0)')
            mycursor.execute(f'INSERT INTO user_info_email VALUES ("{userID}","{email}")')
            mydb.commit()
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1,method='pbkdf2:sha256'),Userid = userID)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.statistics'))

    return render_template("sign_up.html", user=current_user)
