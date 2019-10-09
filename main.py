from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('signup.html')


@app.route("/signup", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm']
    email = request.form['email']

    username_error = ''
    password_error = ''
    confirm_error = ''
    email_error = ''

    if int(len(username)) <= 0:
        username_error = 'Thats not a valid username'
        username = ''
    else:
        if int(len(username)) < 3 or int(len(username)) > 20:
            username_error = 'Thats not a valid username'
            username = ''

    if int(len(password)) <= 0:
        password_error = 'Thats not a valid password'
        password = ''
    else:
        if int(len(password)) < 3 or int(len(password)) > 20:
            password_error = 'Thats not a valid password'
            password = ''

    if int(len(confirm)) <= 0:
        confirm_error = 'Password do not match'
        confirm = ''
    else:
        if password != confirm:
            confirm_error = 'Password do not match'
            confirm = ''

    if int(len(email)) > 0:
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
                email_error = "Not a valid email address."

    if not username_error and not password_error and not confirm_error and not email_error:
        username = str(username)
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html',
                               username_error=username_error,
                               password_error=password_error,
                               confirm_error=confirm_error,
                               email_error=email_error,
                               username=username,
                               password=password, confirm=confirm, email=email)


@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


app.run()
