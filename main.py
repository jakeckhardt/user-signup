#!/usr/bin/env python

__author__ = "student"
__version__ = "1.0"
# June 2017
# Flask User Sign-up re: LaunchCode
# Rubric: http://education.launchcode.org/web-fundamentals/assignments/user-signup/


from flask import Flask, request, render_template, redirect
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=["GET", "POST"])
def index():

    username = ""
    email = ""
    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""
    title = "Signup"

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        verify_password = request.form["verify_password"]
        email = request.form["email"]

        if username == "":
            username_error = "Please enter a username"
        elif (len(username) < 3) or (len(username) > 20):
            username_error = "Username must be between 3 and 20 characters"
            username = ""
        elif " " in username:
            username_error = "Username cannot contain spaces"
            username = ""
        else:
            pass

        if password == "":
            password_error = "Please enter a password"
        elif (len(password) < 3) or (len(password) > 20):
            password_error = "Password must be between 3 and 20 charactors"
        elif " " in password:
            password_error = "Password cannot contain spaces"
        else:
            pass

        if password != verify_password:
            verify_password_error = "Passwords did not match"
        elif verify_password == "":
            verify_password_error = "Please verify your password"
        else:
            pass

        if (email != '') and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
            email_error = "Not a valid email"
            email = ""

        if (not username_error) and (not password_error) and (not verify_password_error):
            return redirect("/welcome?username={0}".format(username))

    return render_template('signup.html', title=title, username_error=username_error, password_error=password_error,
                           verify_password_error=verify_password_error, email_error=email_error, username=username,
                           email=email)


@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    title = 'Welcome!'
    return render_template('success.html', title=title, username=username)


if __name__ == '__main__':
    app.run()
