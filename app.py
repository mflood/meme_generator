import os
import random
import tempfile
from typing import List

import requests
from flask import Flask, abort, render_template, request

from quote_engine.ingestor import Ingestor
from quote_engine.models import QuoteModel
from meme_generator.meme_engine import MemeEngine
from utils.file import find_files, find_image_files

app = Flask(__name__)


OUTPUT_DIR = "./static"
meme_engine = MemeEngine.make_default_engine(output_directory="./static")


def setup():
    """Create output directory and Load all resources"""

    try:
        os.mkdir(OUTPUT_DIR)
    except FileExistsError:
        pass

    quote_files: List[str] = find_files(directory="./_data/SimpleLines")
    quotes: List[QuoteModel] = Ingestor.parse_files(quote_files)

    # Get all image files in the photos directory
    images_path = "./_data/photos"
    image_files: List[str] = find_image_files(directory=images_path)
    return quotes, image_files

quotes, image_files = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from image_files array
    # 2. select a random quote from the quotes array

    img = random.choice(image_files)
    quote = random.choice(quotes)
    meme_output_path = meme_engine.make_meme(
        img_path=img, text=quote.body, author=quote.author
    )
    return render_template("meme.html", path=meme_output_path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""

    image_url = request.form["image_url"]
    body = request.form["body"]
    author = request.form["author"]
    image_name = os.path.basename(image_url)

    try:
        response = requests.get(image_url)
        response.raise_for_status()

        with tempfile.TemporaryDirectory() as tmpdirname:
            tmp_input_image_path = os.path.join(tmpdirname, image_name)

            with open(tmp_input_image_path, "wb") as f:
                f.write(response.content)

            meme_output_path = meme_engine.make_meme(
                img_path=tmp_input_image_path, text=body, author=author
            )
            return render_template("meme.html", path=meme_output_path)

    except requests.RequestException as e:
        return f"An error occurred while downloading the image: {e}"


if __name__ == "__main__":
    app.run()


