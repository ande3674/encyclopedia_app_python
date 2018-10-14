import requests
import flask
import flickr_photo

URL_GET_RECENT = "https://api.flickr.com/services/rest/?method=flickr.photos.getRecent" \
            "&api_key=41014e55b2a616bc84ba31aa9c8966cb&per_page=10&format=json&nojsoncallback=1"
URL_GET_PARIS = "https://api.flickr.com/services/rest/?method=flickr.photos.search" \
            "&api_key=41014e55b2a616bc84ba31aa9c8966cb&tags=paris&format=json&nojsoncallback=1"
URL_GET_BY_TAG = "https://api.flickr.com/services/rest/?method=flickr.photos.search" \
            "&api_key=41014e55b2a616bc84ba31aa9c8966cb&tags={TAG}&format=json&nojsoncallback=1"
SECRET = "ec70c827417a7332"
KEY = "41014e55b2a616bc84ba31aa9c8966cb"

#TEMPLATE FOR A URL FOR A FETCHED PHOTO !
#farm, server, id, secret
photoUrlTemplate = "http://farm{NUM}.staticflickr.com/{S1}/{S2}_{S3}.jpg";
#Some working examples:
photoUrl1 = photoUrlTemplate.format(NUM='2', S1="1955", S2="30131952017", S3="b057dd127b")
photoUrl2 = photoUrlTemplate.format(NUM='2', S1="1969", S2="30132175597", S3="be81e484a5")
photoUrl3 = photoUrlTemplate.format(NUM='2', S1="1971", S2="30165278177", S3="23e6aa75a1")

def search_by_tag_return_flickr_objects(tag):
    tag = split_up(tag)
    url = URL_GET_BY_TAG.format(TAG=tag)
    response = requests.get(url).json()
    photos_array = response['photos']['photo']

    flickr_list = []
    #owner, server, ispublic, isfriend, farm, id, secret, title, isfamily
    for i in range(10):
        photo_object = photos_array[i]
        owner = photo_object['owner']
        ispublic = photo_object['ispublic']
        isfriend = photo_object['isfriend']
        title = photo_object['title']
        isfamily = photo_object['isfamily']
        farm = photo_object['farm']
        server = photo_object['server']
        id = photo_object['id']
        secret = photo_object['secret']
        flickr = flickr_photo.Flickr(owner, server, ispublic, isfriend, farm, id, secret, title, isfamily)
        flickr_list.append(flickr)
    return flickr_list


def build_urls(photos):
    url_list = ['' for i in range(10)]

    for i in range(len(photos)):
        farm = photos[i].farm
        server = photos[i].server
        id = photos[i].id
        secret = photos[i].secret
        display_url = photoUrlTemplate.format(NUM=farm, S1=server, S2=id, S3=secret)
        url_list[i] = display_url
    return url_list



def search_by_tag_return_display_urls(tag):
    tag = split_up(tag)
    url = URL_GET_BY_TAG.format(TAG=tag)
    response = requests.get(url).json()
    photos_array = response['photos']['photo']

    url_list = ['' for i in range(10)]

    for i in range(10):
        photo_object = photos_array[i]
        farm = photo_object['farm']
        server = photo_object['server']
        id = photo_object['id']
        secret = photo_object['secret']
        display_url = photoUrlTemplate.format(NUM=farm, S1=server, S2=id, S3=secret)
        url_list[i] = display_url
    return url_list


def split_up(s):
    split = s.split(" ")
    return_string = ''
    for i in range(len(split)):
        if i == len(split)-1:
            return_string += split[i]
        else:
            return_string += (split[i] + '+')
    return return_string

r = search_by_tag_return_display_urls('cats')
print(r)