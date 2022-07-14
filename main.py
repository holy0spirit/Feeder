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

        mFeeds.append(mFeed)

    return jsonify({"feeds" : mFeeds})