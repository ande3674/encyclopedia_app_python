from flask import Flask, render_template, request
from apis import flickr_api

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/search')
def search():
    search_term = request.args.get('search')
    flickr_photos = flickr_api.search_by_tag_return_flickr_objects(search_term)
    links = flickr_api.build_urls(flickr_photos)

    return render_template('search.html', url1=links[0], url2=links[1], url3=links[2], url4=links[3], url5=links[4],
                           url6=links[5], url7=links[6], url8=links[7], url9=links[8], url10=links[9],)


if __name__ == '__main__':
    app.run()
