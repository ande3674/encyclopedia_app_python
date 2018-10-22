from flask import Flask, render_template, request
from apis import flickr_api, giphy_api, unsplash_api

app = Flask(__name__)
db = 'jdbc:sqlite:C:/Users/ce691/PycharmProjects/quick_flickr\library.sqlite'

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
    p = request.form['data']
    print(p)
    return p

if __name__ == '__main__':
    app.run()
