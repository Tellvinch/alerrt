import urllib.request,json
from .models import News

# Getting api key
api_key = None
# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(name):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(name, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_articles = None

        if get_news_response['articles']:
            news_articles_list = get_news_response['results']
            news_articles = process_articles(news_articles_list)
    return news_articles

def process_articles(articles_list):
    '''
    Function  that processes the news articles and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_articles: A list of news objects
    '''
    news_articles = []
    for news_item in articles_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author= news_item.get('author')
        title = news_item.get('original_title')
        publishedAt = news_item.get('publishedAt')
        description = news_item.get('description')

       
        if name:
            news_object = News(id,name,author,title,
                                 publishedAt,description)
            news_articles.append(news_object)

    return news_articles