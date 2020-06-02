import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1, 'dope app','imani' 'A new web app','thrilling','00675')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))
