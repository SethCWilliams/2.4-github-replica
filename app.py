import csv

from flask import Flask
from flask import request
import requests
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    user_data = requests.get("https://api.github.com/users/SethCWilliams")
    decoded = user_data.json()

    repos = requests.get("https://api.github.com/users/SethCWilliams/repos")
    repo_info = repos.json()

    context = {
        'bio': decoded['bio'],
        'avatar': decoded['avatar_url'],
        'name': decoded['name'],
        'location': decoded['location'],
        'email': decoded['email'],
        'organizations': decoded['organizations_url'],
        'repos': repo_info
    }

    # context1 = context
    # context1.reverse()

    return render_template('index.html', **context)

@app.route("/followers.html")
def followers():
    user_data = requests.get("https://api.github.com/users/SethCWilliams")
    decoded = user_data.json()

    folower_data = requests.get("https://api.github.com/users/SethCWilliams/followers")
    decode = folower_data.json()

    context = {
        'bio': decoded['bio'],
        'avatar': decoded['avatar_url'],
        'name': decoded['name'],
        'location': decoded['location'],
        'email': decoded['email'],
        'followers': decode
    }
    return render_template('followers.html', **context)
# avatar=response
