import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/profile/<name>')
def profile(name):
    # todo access the JSON and look for the corresponding name, then pass it over as a variable to render it
    return render_template('profile.html', name=name, url=os.getenv("URL"))
