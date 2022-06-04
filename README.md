# PE Track: Week 1 - TEAM PYTHONIC - Portfolio Site

## Introduction

TEAM PYTHONIC is from 22.SUM.21 of the Production Engineering Track at MLH Fellowship. For week 1, an interactive team portfolio was made with an enjoyable user interface and a variety of multimedia components. The purpose of the project was to explore new technologies in web development and using the best practices to collaborate as a team on Github.

## Badges


## Description

Team Pythonic's portfolio website consists of two main components:

###### Landing page

- Animated heading text to display team name
- Medium subheading, animated text to display team info
- Profile pictures of each member which lead to their respective profile pages


###### Profile page

Cards with relevant profile sections, including:
- About me
- Experience
- Projects
- Countries I've visited: Interactive Google maps with markers of locations a member has visited
- Hobbies: Hover effect tooltip boxes with more information

###### Additional features

- Landing page with pop-up CSS animations when user hovers over main text
- Responsive website that adjusts according to screen size and works on mobile screens
- Animated menu bar leading to corresponding pages

## Visuals

##### Landing page

![image](https://user-images.githubusercontent.com/68432655/171975341-1461f565-c145-4f11-a82a-af86d4897b87.png)

## Technologies used in the project

- The python microframework Flask
- HTML/CSS and Bootstrap
- Jinja and json to parse through data
- Javascript for the menu dropdown
- Google Maps API to mark locations visited in each profile page

## File Structure

```
main
│   README.md
│   .gitignore
|   .python-version
|   example.env
|   requirements.txt
|   data.json
│
└───app
    │   __init__.py
    │
    └───static
    |   └───fonts
    |   |   |   flux-regular.otf
    |   |
    |   └───img
    |   |   |   (all images for website)
    |   |
    |   └───scripts
    |   |   |   index.js
    |   |   |   maps.js
    |   |   |   profile.js
    |   |
    |   └───styles
    |   |   |   index.css
    |   |   |   maps.css
    |   |   |   profile.css
    |
    └───templates
        |   index.html
        |   profile.html
        
```

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

*Note: Also make sure to add an API_KEY in the .env file in order to use Google Maps section in the website*

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: For now, the portfolio site will only work on your local machine while you have it running inside of your terminal. We plan to host it in the cloud in the next few weeks!* 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Tasks
Each of the following tasks have been completed.

Note: Our team has ensured that we created an issue for each task, we used a new branch for each issue and made corresponding pull requests.

### GitHub Tasks
- [x] Create Issues for each task below
- [x] Work on each task in a new branch
- [x] Open a Pull Request when a task is finished to get feedback

### Portfolio Tasks
- [x] Add a photo of yourself to the website
- [x] Add an "About youself" section to the website.
- [x] Add your previous work experiences
- [x] Add your hobbies (including images)
- [x] Add your current/previous education
- [x] Add a map of all the cool locations/countries you visited

### Flask Tasks
- [x] Get your Flask app running locally on your machine using the instructions below.
- [x] Add a template for adding multiple work experiences/education/hobbies using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/api/#basics)
- [x] Create a new page to display hobbies.
- [x] Add a menu bar that dynamically displays other pages in the app

## Authors
* Emilie Zhang ([EmilieYZhang](https://github.com/EmilieYZhang))
* Hanna Gersten ([Hgersten-hash](https://github.com/Hgersten-hash))
* Emily Lim ([emilyllim](https://github.com/emilyllim))
* Juan Escalada ([jescalada](https://github.com/jescalada))
