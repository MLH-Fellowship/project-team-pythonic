import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/profile/<name>')
def profile(name):
    data = load_profiles_from_json('data.json')
    info = data[name]
    # todo check if name exists
    print(info)
    return render_template('profile.html', name=name, info=info, url=os.getenv("URL"))


def load_profiles_from_json(filename) -> dict:
    # Get the relative path for the JSON data
    path = f'{os.getcwd()}/{filename}'
    # Open the file and return its parsed contents
    # UTF-8 encoding is used to parse apostrophes correctly
    with open(path, "r", encoding='utf8') as file:
        return json.load(file)


def find_info_by_name(name: str):
    print(name)