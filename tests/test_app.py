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
        
    
    def test_timeline(self): 
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200 
        assert response.is_json 
        json = response.get_json()
        assert "timeline_posts" in json 
        assert len(json["timeline_posts"]) == 0 

        # Tests relating to the /api/timeline_post GET and POST 
        first_post = self.client.post("/api/timeline_post/name=John Doe&email=john@example.com&content=Hi!My name is John")
        second_post = self.client.post("/api/timeline_post/name=Jane Doe&email=jane@example.com&content=Hi!My name is Jane")
        
        response2 = self.client.get("/api/timeline_post")
        assert response2.is_json
        json2 = response2.get_json() 
        print (json2)
        assert "timeline_posts" in json2
        assert len(json["timeline_posts"]) == 2 
        
        # Tests relating to the timeline page 
        timeline_response = self.client.get('/timeline')
        assert timeline_response.status_code == 200
        html = timeline_response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html 