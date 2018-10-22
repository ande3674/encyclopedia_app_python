from pprint import pprint

import giphy_client
import requests
from giphy_client.rest import ApiException

from classes import giphy

# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC'  # str | Giphy API Key.
#q = 'cheeseburgers'  # str | Search query term or prhase.
limit = 10  # int | The maximum number of records to return. (optional) (default to 25)
offset = 0  # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = 'g'  # str | Filters results by specified rating. (optional)
lang = 'en'  # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
fmt = 'json'  # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)
DISPLAY_TEMPLATE = 'https://media.giphy.com/media/{ID}/giphy.gif'
KEY = 'U7bQ6qbG1jUVeB6oQkwhtxoDVwrABzGd'
URL = 'http://api.giphy.com/v1/gifs/search?q={TAG}&api_key=U7bQ6qbG1jUVeB6oQkwhtxoDVwrABzGd&limit=10'
# http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=U7bQ6qbG1jUVeB6oQkwhtxoDVwrABzGd&limit=10

def search_by_tag_return_giphy_objects(tag):
    tag = split_up(tag)
    url = URL.format(TAG=tag)
    response = requests.get(url).json()
    data = response['data']
    giphy_list = []
    for i in range(10):
        id = data[i]['id']
        typ = data[i]['type']
        slug = data[i]['slug']
        url = data[i]['url']
        giphy_list.append(giphy.Giphy(typ, id, slug, url))
    return giphy_list

def build_urls(giphys):
    link_list = []
    for i in range(10):
        id = giphys[i].id
        link_list.append(DISPLAY_TEMPLATE.format(ID=id))
    return link_list


def split_up(s):
    split = s.split(" ")
    return_string = ''
    for i in range(len(split)):
        if i == len(split)-1:
            return_string += split[i]
        else:
            return_string += (split[i] + '+')
    return return_string

def search(q):
    try:
        # Search Endpoint
        api_response = api_instance.gifs_search_get(KEY, q, limit=limit, offset=offset, rating=rating, lang=lang,
                                                    fmt=fmt)
        pprint(api_response)
        # data = api_response['data']
        # id = data[0]['id']
        # print(id)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)