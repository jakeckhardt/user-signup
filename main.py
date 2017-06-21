from flask import Flask, request, render_template, redirect


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
	return render_template('signup.html', username_input="", password_input="", v_password_input="", email_input="")


@app.route("/", methods=["POST"])
def success():
	username = request.form["username"]
	password = request.form["password"]
	v_password = request.form["v_password"]
	email = request.form["email"]

	username_input = ""
	password_input = ""
	v_password_input = ""
	email_input = ""



	if username == "":
		username_input = "Please enter a username"

	elif len(username) < 3 or len(username) > 20:
		username_input = "Username must be between 3 and 20 charactors"
		username = ""

	elif " " in username:
		username_input = "Username cannot contain spaces"
		username = ""



	if password == "":
		password_input = "Please enter a password"

	elif len(password) < 3 or len(password) > 20:
		password_input = "Password must be between 3 and 20 charactors"

	elif " " in password:
		password_input = "Password cannot contain spaces"



	if password != v_password:
		v_password_input = "Passwords did not match"


	elif v_password == "":
		v_password_input = "Please verify your password"




	if len(email) > 1:
		if " " in email or "@" not in email or "." not in email:
			email_input = "Not a valid email"
			email = ""

		if len(email) < 3 or len(password) > 20:
			email_input = "Not a valid email"
			email = ""





	if not username_input and not password_input:
		return render_template('success.html', username=username)
	else:
		return render_template('signup.html', username_input=username_input, password_input=password_input, v_password_input=v_password_input, email_input=email_input, username=username, email=email)


app.run()