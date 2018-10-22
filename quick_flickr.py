from flask import Flask, render_template, request
from apis import flickr_api, giphy_api, unsplash_api
from database import db
import json, ast

app = Flask(__name__)
db_url = 'jdbc:sqlite:C:/Users/ce691/PycharmProjects/quick_flickr\library.sqlite'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/search')
def search():
    search_term = request.args.get('search')

    flickr_photos = flickr_api.search_by_tag_return_flickr_objects(search_term)
    links = flickr_api.build_urls(flickr_photos)
    #flickr_map = [ {'photo_object':flickr_photo, 'link':link } , ... ]
    flickr_data_list = []
    for i in range(len(flickr_photos)):
        flickr_data = {'photo': {'owner':flickr_photos[i].owner,
                                 'server':flickr_photos[i].server,
                                 'ispublic':flickr_photos[i].ispublic,
                                  'isfriend':flickr_photos[i].isfriend,
                                  'farm':flickr_photos[i].farm,
                                  'id':flickr_photos[i].id,
                                  'secret':flickr_photos[i].secret,
                                  'title':flickr_photos[i].title,
                                  'isfamily':flickr_photos[i].isfamily},
                       'link':links[i],
                       'type':'flickr'}
        flickr_data_list.append(flickr_data)

    giphy_photos = giphy_api.search_by_tag_return_giphy_objects(search_term)
    giphy_links = giphy_api.build_urls(giphy_photos)
    giphy_data_list = []
    for i in range(len(giphy_photos)):
        giphy_data = {'photo': {'type':giphy_photos[i].type,
                                'id':giphy_photos[i].id,
                                'slug':giphy_photos[i].slug,
                                'url':giphy_photos[i].url},
                      'link': giphy_links[i],
                      'type':'giphy'}
        giphy_data_list.append(giphy_data)

    unsplash_photos = unsplash_api.search_by_tag_return_unsplash_objects(search_term)
    unsplash_links = unsplash_api.build_urls(unsplash_photos)
    unsplash_data_list = []
    for i in range(len(unsplash_photos)):
        unsplash_data = {'photo': {'id':unsplash_photos[i].id,
                                   'width':unsplash_photos[i].width,
                                   'height':unsplash_photos[i].height,
                                   'description':unsplash_photos[i].description,
                                   'url':unsplash_photos[i].url},
                         'link': unsplash_links[i],
                         'type':'unsplash'}
        unsplash_data_list.append(unsplash_data)

    #return (render_template('search.html', links1=links, links2=giphy_links, links3=unsplash_links))
    return (render_template('search.html', flickr=flickr_data_list, giphy=giphy_data_list, unsplash=unsplash_data_list))

@app.route('/upload', methods=['POST'])
def upload():
    photo_name = request.form['name']
    photo_data = request.form['data']
    photo_data = ast.literal_eval(photo_data)
    print(photo_name)
    if photo_data.get('type') == 'flickr':
        db.insert_flickr(photo_name, photo_data.get('photo').get('owner'), photo_data.get('photo').get('server'), photo_data.get('photo').get('ispublic'),
                         photo_data.get('photo').get('isfriend'), photo_data.get('photo').get('farm'), photo_data.get('photo').get('id'),
                         photo_data.get('photo').get('secret'), photo_data.get('photo').get('title'), photo_data.get('photo').get('isfamily'))
    elif photo_data.get('type') == 'giphy':
        print(photo_data.get('link'))
        db.insert_giphy(photo_name, photo_data.get('photo').get('type'), photo_data.get('photo').get('id'), photo_data.get('photo').get('slug'),
                         photo_data.get('photo').get('url'))
    elif photo_data.get('type') == 'unsplash':
        print(photo_data.get('link'))
        db.insert_unsplash(photo_name, photo_data.get('photo').get('id'), photo_data.get('photo').get('width'), photo_data.get('photo').get('height'),
                         photo_data.get('photo').get('description'), photo_data.get('photo').get('url'))

    return render_template('upload.html', url=photo_data.get('link'))

@app.route('/pull')
def pull():
    search_term = request.args.get('keyword')
    # query each table
    flickr_photo_data = db.query_flickr(search_term)
    giphy_photo_data = db.query_giphy(search_term)
    unsplash_photo_data = db.query_unsplah(search_term)
    # Test data - delete later
    #print(flickr_photo_data)
    #print(giphy_photo_data)
    #print(unsplash_photo_data)
    #now we have to deal with all of the data
    # build/get url links
    all_photo_urls = [] # List of ALL photo urls that match the search term (from all tables)
    # FLICKR PHOTOS
    for i in range(len(flickr_photo_data)):
        farm = flickr_photo_data[i][5]
        server = flickr_photo_data[i][2]
        id = flickr_photo_data[i][6]
        secret = flickr_photo_data[i][7]
        url = flickr_api.build_one_url(farm, server, id, secret)
        #print(url)
        all_photo_urls.append(url)
    # GIPHY PHOTOS
    for i in range (len(giphy_photo_data)):
        id = giphy_photo_data[i][2]
        url = giphy_api.build_one_url(id)
        #print(url)
        all_photo_urls.append(url)
    # UNSPLASH PHOTOS
    for i in range(len(unsplash_photo_data)):
        url = unsplash_photo_data[i][5]
        #print(url)
        all_photo_urls.append(url)
    # send urls to the webpage to render
    return render_template('pull.html', term=search_term, links=all_photo_urls)


if __name__ == '__main__':
    app.run()
