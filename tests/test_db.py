# test_db.py

import unittest
from peewee import *

from app import TimelinePost
from playhouse.shortcuts import model_to_dict

MODELS = [ TimelinePost ]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)
    
    def tearDown(self):
        # Note strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection... but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()
    
    def test_timeline_post(self):
        # Create 2 timeline posts.
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1

        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

        # Get timeline posts and assert that they are correct
        timeline_posts = [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]

        # Assert that length of timeline is as expected: 2 posts
        assert len(timeline_posts) == 2

        # Assert that first and second posts have correct name and id
        post_1 = TimelinePost.get(TimelinePost.id == 1)
        assert post_1.name == 'John Doe'
        post_2 = TimelinePost.get(TimelinePost.id == 2)
        assert post_2.name == 'Jane Doe'
