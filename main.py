from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def welcome():
    isError = False
    username = request.form['username']
    password = request.form['password']
    password_verify = request.form['password_verify']
    email = request.form['email']

    params = dict(username = username, email = email)

    if not bool(re.match(r"^[a-zA-Z0-9_-]{3,20}$", username)):
        params['uerror'] = "Invalid Username"
        isError = True
    
    if not bool(re.match(r"^.{3,20}$", password)):
        params['perror'] = "Invalid Password"
        isError = True

    if password != password_verify:
        params['verror'] = "Passwords do not match"
        isError = True

    if email != "":
        if not bool(re.match(r"^[\S]+@[\S]+\.[\S]+$", email)):
            params['emerror'] = "Invalid Email"
            isError = True
        else:
            return render_template('welcome.html', username = username)

    if isError:
        return render_template('base.html', **params)
    else:
        return render_template('welcome.html', username = username)


    
@app.route("/")    
def index():
    
    error = request.args.get("error")
    
    return render_template('base.html', error = error)

app.run()