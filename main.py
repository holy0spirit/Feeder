import imp
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/feed', methods=["GET"])
def rssFeed():
    url = 'https://mfmejigboregion7lagos.org/blog/feed/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    mItems = soup.find_all('item')

    mFeeds = []
    for mItem in mItems:
        mText = mItem.title.get_text()
        mLink = mItem.guid.get_text()
        mDescription = mItem.description.get_text()

        mFeed = {
            "text" : mText,
            "link" : mLink,
            "description" : mDescription
        }
        if len(mFeeds) < 6:
            mFeeds.append(mFeed)
    print(len(mFeeds))

    return jsonify({"feeds" : mFeeds})



@app.route("/mInstagram", methods=["GET"])
def mInstagramFeed():

    url = 'https://mfmejigboregion7lagos.org/blog/instagram-feed/'
    # mImageURL = 'https://mfmejigboregion7lagos.org/blog/wp-content/uploads/sb-instagram-feed-images/%s_nfull.jpg' % mImageID
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    mPhotoFeed = []
    for mLink in soup.find_all('a'):
        try:
            mPhoto = mLink['class'][0]
            
            if mPhoto == 'sbi_photo':
                mPhotoLink = {
                    "src" : (mLink['data-full-res'])
                }
                if len(mPhotoFeed) < 20:
                    mPhotoFeed.append(mPhotoLink)

        except KeyError:
            continue

    



    return jsonify({"mPhotoFeed" : mPhotoFeed})