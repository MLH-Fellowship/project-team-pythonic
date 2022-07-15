import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
from flask import Response
import re

load_dotenv()  # Loads the environment variables from the .env file

app = Flask(__name__)  # Initializes a Flask app

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    #creates database 
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
    )
print(mydb)

#creates table for timeline post
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

# os.getenv("API_KEY")  # Obtains the value of the .env variable containing the Google Maps API key

# Route for the landing page
@app.route('/')
def index():
    """
    Serves the landing page.
    """
    return render_template('index.html', title="Team Pythonic", url=os.getenv("URL"))

# Route for the profile page
@app.route('/profile/<name>')
def profile(name):
    """
    Loads profile dynamically from the JSON file and serves profile page.
    
    If profile could not be found, redirects to the landing page.
    """
    data = load_profiles_from_json('data.json')
    if name in data:
        info = data[name]
        return render_template('profile.html', name=name, info=info, url=os.getenv("URL"), API_KEY=os.getenv("API_KEY"))
    else:
        return index()


# Route for the projects page
@app.route('/projects')
def projects():

    data = load_profiles_from_json('projects.json')
    info1 = data['portfolio']
    info2 = data['strace']
    info3 = data['qa']
    info4 = data['weather']
    return render_template('projects.html', info1=info1, info2 = info2, info3 = info3, info4= info4,url=os.getenv("URL"))

# Route for the contact page
@app.route('/contact')
def contact():

    return render_template('contact.html', url=os.getenv("URL"))

# Route for the resume page
@app.route('/resume')
def resume():

    return render_template('resume.html', url=os.getenv("URL"))

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline") 

# Route for handling 404 errors
@app.errorhandler(404)
def not_found(e):
    """
    Serves the projects page.
    """
    return render_template("index.html")


def load_profiles_from_json(filename) -> dict:
    """
    Loads profile data by parsing the JSON file provided.

    :param: The JSON file to parse
    :return: A dict containing all the JSON info parsed
    """
    # Get the relative path for the JSON data
    path = f'{os.getcwd()}/{filename}'
    # Open the file and return its parsed contents
    # UTF-8 encoding is used to parse apostrophes correctly
    with open(path, "r", encoding='utf8') as file:
        return json.load(file)

#create GET endpoint to retrieve timeline posts by create_at descending
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

#add POST route for timeline post, DELETE attempt 2
@app.route('/api/timeline_post', methods=['POST']) #'DELETE'])
# if request.method =='POST':
def post_time_line_post():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    try:
        name = request.form['name']
        email = request.form['email']
        content = request.form['content'] 
        if content == "":
            return Response(
            "Invalid content",
            status=400,
            )
        elif name == "":
            return Response(
            "Invalid name",
            status=400,
            )
        else:
            if(re.fullmatch(regex, email)):
                timeline_post = TimelinePost.create(name=name, email=email, content=content)
                return model_to_dict(timeline_post)
            else:
                return Response(
                "Invalid email",
                status=400,
                )
    except:
	    return Response(
        "Invalid name",
        status=400,
    )
# elif request.method =='DELETE':
#     def delete_time_line_post():
#         nid = request.form['id']
#         obj=TimelinePost.get(TimelinePost.id==nid)
#         obj.delete_instance()

#         return "Done"

# DELETE attempt 3
# @app.route('/api/timeline_post', methods=['DELETE'])
# def delete_time_line_post():
    # nid = request.form['id']
    # obj=TimelinePost.get(TimelinePost.id==nid)
    # obj.delete_instance()

    # return "Done"

# Delete attempt 1
@app.route('/api/timeline_post/<int:nid>', methods=['DELETE'])
def delete_time_line_post(nid):
    try:
        obj=TimelinePost.get(TimelinePost.id==nid)
        obj.delete_instance()
        return get_time_line_post()
        # return "Done"
    except TypeError:
        from traceback import format_exec
        print(format_exec())
    # print("deleted result")
