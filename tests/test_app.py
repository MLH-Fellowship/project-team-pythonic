# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Emily Lim</title>" in html
        # add more tests relating to the homepage
        assert '<meta charset="utf-8" />' in html
        assert '<meta property="og:title" content="Personal Portfolio" />' in html
        assert '<meta property="og:description" content="My Personal Portfolio" />' in html
    
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline-posts" in json
        assert len(json["timeline-posts"]) == 0

        # Add more tests relating to the POST GET api
        # Testing POST request
        first_post = self.client.post('/api/timeline_post', data={'name':'Tom Doe', 'email':'tom@example.com', 'content':'Hello world, I\'m Tom!'})
        assert first_post.status_code == 200

        second_post = self.client.post('/api/timeline_post', data={'name':'Jenn Doe', 'email':'jenn@example.com', 'content':'Hello world, I\'m Jenn!'})
        assert first_post.status_code == 200

        # Testing GET request
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline-posts" in json

        assert len(json["timeline-posts"]) == 2

        # Checking second_post is correct
        assert json["timeline-posts"][0]['id'] == 2
        assert json["timeline-posts"][0]['name'] == 'Jenn Doe'

        # Checking first_post is correct
        assert json["timeline-posts"][1]['id'] == 1
        assert json["timeline-posts"][1]['name'] == 'Tom Doe'
    
    # Testing timeline page
    def test_timelinepage(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html
        assert '<button type="submit">Submit</button>' in html
        assert '<input name="name" placeholder="Name" type="text">' in html
        assert '<input name="email" placeholder="Email" type="text">' in html
        assert '<textarea name="content" placeholder="Content" type="text"></textarea>' in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name" : "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name" : "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html