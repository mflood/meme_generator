import random
from typing import List
import os
import requests
from flask import Flask, render_template, abort, request


from utils.file import find_image_files, find_files
from ingest.ingestor import Ingestor
from meme_generator.meme_engine import MemeEngine

app = Flask(__name__)

meme = MemeEngine.make_default_engine(output_directory='./static')

def setup():
    """ Load all resources """

    quote_files = find_files(directory='./_data/DogQuotes')
    print(quote_files)

    quotes = []
    for path in quote_files:
        if Ingestor.can_ingest(path):
            file_quotes = Ingestor.parse(path)
            quotes.extend(file_quotes)

    # Get all image files in the photos directory
    images_path = "./_data/photos"
    imgs = find_image_files(directory=images_path)
    return quotes, imgs


quotes, imgs = setup()

@app.route('/home')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
