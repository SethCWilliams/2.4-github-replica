import csv



from flask import Flask
from flask import request
import requests
from flask import render_template

app = Flask(__name__)


response = requests.get('https://avatars2.githubusercontent.com/u/43652084?v=4')



user_data = requests.get("https://api.github.com/users/SethCWilliams")
decoded = user_data.json()
put_together = decoded['bio']
avatar = decoded ['avatar']

# def base():
#     return render_template('base.html', bio=put_together)
#ask why this isn't working outside of the app route, but it worked while in it
repos = requests.get("https://api.github.com/users/SethCWilliams/repos")
repo_info = repos.json()

@app.route("")
def base():
    return render_template('base.html', bio=put_together, avatar=avatar)

@app.route("/")
# def base():
#     return render_template('base.html', bio=put_together, avatar=response)
def index():


    return render_template('index.html')


# avatar=response
