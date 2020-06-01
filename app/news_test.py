import unittest
from models import news
News = news.News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1, 'Guru',
                             'Tellvinch imani', 'New awesome webapp created', 'A moringa school student creates an awesome website for news','2020-06-01T04:41:16Z' )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))


if __name__ == '__main__':
    unittest.main()
