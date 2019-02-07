import csv





from flask import Flask
from flask import request
import requests
from flask import render_template
from flask_humanize import Humanize

try:
    from githubkey import github_api_key
    headers = {"Authorization": "token {}".format(github_api_key)}
except:
    print("Hey, I see you don't have a github API key.")
    print("That's okay, you can use the public API key")
    headers = {}


app = Flask(__name__)
humanize = Humanize(app)

@app.route("/")
def index():
    user_data = requests.get("https://api.github.com/users/SethCWilliams", headers=headers)
    decoded = user_data.json()

    search_bar = requests.post("https://api.github.com/users/SethCWilliams", headers=headers)
    find_stuff = search_bar.json()

    repos = requests.get("https://api.github.com/users/SethCWilliams/repos", headers=headers)
    repo_info = repos.json()

    context = {
        'bio': decoded['bio'],
        'avatar': decoded['avatar_url'],
        'name': decoded['name'],
        'location': decoded['location'],
        'email': decoded['email'],
        'organizations': decoded['organizations_url'],
        'repos': repo_info[::-1]
    }

    # context1 = context
    # context1.reverse()

    return render_template('index.html', **context)

@app.route("/followers.html")
def followers():
    user_data = requests.get("https://api.github.com/users/SethCWilliams", headers=headers)
    decoded = user_data.json()

    follower_data = requests.get("https://api.github.com/users/SethCWilliams/followers", headers=headers)
    decode = follower_data.json()
    #new test is equal to all of the urls that I need to get api info on.
    #I need to ask why this works. I get the idea of it, but I took it from someone online.
    new_test = [user_info['login'] for user_info in decode]

    user_info_list = []

    for item in new_test:
        item2 = requests.get("https://api.github.com/users/{}".format(item), headers=headers)
        decoderama = item2.json()
        #I had to append this to a list because decoderama only lives in this function
        user_info_list.append(decoderama)


    ctxt = {
        'bio': decoded['bio'],
        'avatar': decoded['avatar_url'],
        'name': decoded['name'],
        'location': decoded['location'],
        'email': decoded['email'],
        'user_filler': user_info_list[::-1]
    }


    print(user_info_list)


    return render_template('followers.html', **ctxt)
# avatar=response




if __name__ == '__main__':
    app.run()