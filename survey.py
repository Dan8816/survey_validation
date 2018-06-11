from flask import Flask, render_template, request, redirect, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)

app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/', methods=['GET'])
def index():
    return render_template("index_dojo.html")

@app.route('/results', methods=['POST'])
def create():
    print(request.form)
    print('Name', request.form['name'])
    print('Email', request.form['email'])
    print('Dojo Location', request.form['location'])
    print('Favorite Language', request.form['language'])
    print('Comments', request.form['comments'])
    if len(request.form['email']) < 1:
        flash("Email cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
    else:
        flash("Success!")
    if len(request.form['comments']) < 1:
        flash("comments cannot be empty!")
    if len(request.form['comments']) > 120:
        flash("comments cannont exeed 120 characters")
    return render_template("created_dojo.html",)

@app.route('/danger')
def danger():
    print("User tried to visit /danger. we have redirected the users to /")

    return redirect('/')

if __name__=="__main__":
    # run our server
    app.run(debug=True) 