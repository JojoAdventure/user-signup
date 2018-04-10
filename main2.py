from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    password_verify = request.form['password_verify']
    email = request.form['email']
    
    if not bool(re.match(r"^[a-zA-Z0-9_-]{3,20}$", username)):
        error = "Invalid Username"
        return redirect("/?error=" + cgi.escape(error, quote=True))
    
    if not bool(re.match(r"^.{3,20}$", password)):
        error = "Invalid Password"
        return redirect("/?error=" + cgi.escape(error, quote=True))
    
    if password != password_verify:
        error = "Passwords do not match"
        return redirect("/?error=" + cgi.escape(error, quote=True))
    
    if email != "":
        if not bool(re.match(r"^[\S]+@[\S]+\.[\S]+$", email)):
            error = "Invalid Email"
            return redirect("/?error=" + cgi.escape(error, quote=True))
    
    return render_template('welcome.html', username = username)
    
@app.route("/")    
def index():
    
    error = request.args.get("error")
    
    return render_template('base.html', error = error)

app.run()