from flask import render_template
from app import app
from .request import get_news


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    trending_news = get_news('name')
    print(trending_news)
    title = 'Home - Welcome to The bestNews Website Online'
    return render_template('index.html', title = title,popular = trending_news)


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    title = f'You are viewing {news_id}'
    return render_template('news.html',title = title)