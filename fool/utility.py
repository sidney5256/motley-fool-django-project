import random
import json

content_file = 'fool/data_content/content_api.json'
quote_file = 'fool/data_content/quotes_api.json'


def get_articles_via_content_api():
    with open(content_file, encoding='utf-8') as content_json_file:
        content_data = json.load(content_json_file)
    content_json_file.close()
    return content_data.get('results')

# get stocks from the api 
def get_stocks_via_content_api():
    with open(quote_file, encoding='utf-8') as quote_json_file:
        quote_data = json.load(quote_json_file)
    quote_json_file.close()
    return quote_data

# look in the articles to find article that 
# has slug of 10-promise and return it
def get_homepage_article():
    articles_list = get_articles_via_content_api()
    for article in articles_list:
        for item in article['tags']:
            if item['slug'] == '10-promise':
                    return article

# grab the article by uuid
def get_article_by_uuid(uuid):
    articles_list = get_articles_via_content_api()
    for article in articles_list:
        if article['uuid'] == uuid:
            return article

# get random articles
def get_random_articles(count):
    articles_list = get_articles_via_content_api()
    result = []

    homepage_article = get_homepage_article() 

    while len(result) < count:
        item = random.choice(articles_list)
        if item !=homepage_article and item not in result:
            result.append(item)

    return result

# get random stocks
def get_random_stocks(count):
    stocks_list = get_stocks_via_content_api()
    result = []

    while len(result) < count:
        stock = random.choice(stocks_list)
        if stock not in result:
            result.append(stock)
    return result