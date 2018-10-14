from flask import Flask, render_template, request
from apis import flickr_api, giphy_api, unsplash_api

app = Flask(__name__)

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

    return render_template('search.html', url1=links[0], url2=links[1], url3=links[2], url4=links[3], url5=links[4],
                           url6=links[5], url7=links[6], url8=links[7], url9=links[8], url10=links[9], url11=giphy_links[0],
                           url12=giphy_links[1], url13=giphy_links[2], url14=giphy_links[3], url15=giphy_links[4],
                           url16=giphy_links[5], url17=giphy_links[6], url18=giphy_links[7], url19=giphy_links[8], url20=giphy_links[9],
                           url21=unsplash_links[0], url22=unsplash_links[1], url23=unsplash_links[2], url24=unsplash_links[3], url25=unsplash_links[4],
                           url26=unsplash_links[5], url27=unsplash_links[6], url28=unsplash_links[7], url29=unsplash_links[8], url30=unsplash_links[9])


if __name__ == '__main__':
    app.run()
