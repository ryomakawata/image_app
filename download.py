from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os, time, sys

key = "294179ddcdba2f893c88bea687c55122"
secret = "27b919eed837634e"
wait_time = 1

keyword = sys.argv[1]
savedir = "./" + keyword

flickr = FlickrAPI(key,secret,format='parsed-json')
result = flickr.photos.search(
    text = keyword,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, license'
)

photos = result['photos']

for i , photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)
