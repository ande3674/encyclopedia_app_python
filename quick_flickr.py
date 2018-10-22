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

    giphy_photos = giphy_api.search_by_tag_return_giphy_objects(search_term)
    giphy_links = giphy_api.build_urls(giphy_photos)

    unsplash_photos = unsplash_api.search_by_tag_return_unsplash_objects(search_term)
    unsplash_links = unsplash_api.build_urls(unsplash_photos)

    return (render_template('search.html', links1=links, links2=giphy_links, links3=unsplash_links))

@app.route('/upload', methods=['POST'])
def upload():
    url = request.form['data']
    return url

if __name__ == '__main__':
    app.run()
