import unittest 
import os 
os.environ['TESTING'] = 'true'

from app import app 

class AppTestCase(unittest.TestCase): 
    def setUp(self): 
        self.client = app.test_client()

    def test_home(self): 
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Team Pythonic</title>" in html 
        
        assert "<div class=\"hero_header\">" in html 
        assert "<h1 id=\"herofont\"><span id=\"pythonic_color\">Hanna </span>Gersten</h1>" in html 
        assert "<h2 id=\"herosubfont\">Aspiring Software Engineer</h2>" in html 
        # TODO Add more tests relating to the home page 
    
    def test_timeline(self): 
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200 
        assert response.is_json 
        json = response.get_json()
        assert "timeline_posts" in json 
        assert len(json["timeline_posts"]) == 0 #28
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        # TODO Add more tests relating to the timeline page 