import urllib.request,json
from .models import Quote
# from app import app


# Getting api key
# api_key = None
# Getting the quote base url
base_url = None

def configure_request(app):
    global base_url
    # base_url =['BLOG_API_BASE_URL']

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    base_url ='http://quotes.stormconsultancy.co.uk/random.json'
    print(base_url)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_object = None

        if get_quotes_response:

          id=get_quotes_response.get('id')
          author=get_quotes_response.get('author')
          quote=get_quotes_response.get('quote')
          quote_object = Quote(id,author,quote)


import urllib.request,json
from .models import Quote


base_url = None
# base_url =['QUOTE_API_BASE_URL']

def configure_request():
    global base_url
    

def get_quotes():

    get_movies_url = base_url
  
    print(base_url)

    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_object = None

        if get_quotes_response:
            id=get_quotes_response.get('id')
            author=get_quotes_response.get('author')
            quote=get_quotes_response.get('quote')
            quote_object = Quote(id,author,quote)

    return quote_object

