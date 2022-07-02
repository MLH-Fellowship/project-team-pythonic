import unittest
from peewee import * 

from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests 
test_db = SqliteDatabase(':memory:') 

class TestTimleinePost (unittest.TestCase): 
    def setUp (self): 
        # Bind model classes to test db. Since we have a complete list of all the models we do not need to recursvely bind ependencies 
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False) 

        test_db.connect()
        test_db.create_tables(MODELS) 

    def tearDown (self): 
        # Not strictly necessary since SQLite in-memory databases only live for the duration of the connection, and in the next step we close the connection ... but a good practice all the time 
        test_db.drop_tables(MODELS) 
        
        # Close connection to db. 
        test_db.close() 

    def test_timeline_post (self): 
        # Create 2 timeline posts 
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2
        
        get_first_post = TimelinePost.select (1)
        assert get_first_post == {'name':'John Doe', 'email':'john@example.com', 'content':'Hello world, I\'m John!'}
        get_second_post = TimelinePost.select (2)
        assert get_second_post == {'name':'Jane Doe', 'email':'jane@example.com', 'content':'Hello world, I\'m Jane!'}