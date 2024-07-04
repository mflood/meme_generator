import os
import random
import textwrap
from typing import Optional

from PIL import Image, ImageDraw, ImageFont

from meme_generator.fonts import FontId, get_font

MARGIN = 10
OFFSET = 30
QUOTE_LINE_SPACING = 4
AUTHOR_INDENT = 40
AUTHOR_EXTRA_LINE_SPACING = 10
QUOTE_TEXTWRAP_WIDTH = 40


def generate_random_image_path(directory: str) -> str:
    """
    Generate a random output filepath for generated memes
    """
    random_int = random.randint(
        100000, 999999
    )  # Generate a random integer between 1000 and 9999
    filename = (
        f"generated_{random_int}.jpg"  # Create a filename using the random integer
    )
    return os.path.join(
        directory, filename
    )  # Combine the directory and filename to create the full path


class MemeEngine:

    def __init__(self, output_directory: str, font: ImageFont.FreeTypeFont):
        """
        Arguments:
            in_path {str} -- the file location for the input image.
            out_path {str} -- the desired location for the output image.
            crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
        """
        self._static_directory = output_directory
        self._font = font

    @classmethod
    def make_default_engine(cls, output_directory):
        """
        Make an engine appropriate for this project
        """
        font = get_font(FontId.K_LILITA_ONE_REGULAR, size=20)
        return cls(output_directory=output_directory, font=font)

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """
        returns: relative URL path of image
        """
        img_object = Image.open(img_path)

        outpath = generate_random_image_path(directory=self._static_directory)
        max_width = width

        if width is not None:
            ratio = width / float(img_object.size[0])
            height = int(ratio * float(img_object.size[1]))
            img_object = img_object.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img_object)

        wrapped_text = textwrap.fill(text, width=QUOTE_TEXTWRAP_WIDTH)
        author_text = f"- {author}"

        # set starting coordinates
        x = MARGIN
        y = OFFSET

        # Draw quote text
        for line in wrapped_text.split("\n"):

            self._draw_text_with_outline(draw=draw, x=x, y=y, text=line)

            # Get height of the text and update y for next line
            y += self._get_text_height(draw=draw, text=line)
            y += QUOTE_LINE_SPACING

        # Draw author with extra offset and indent
        y += AUTHOR_EXTRA_LINE_SPACING
        x += AUTHOR_INDENT
        self._draw_text_with_outline(draw=draw, x=x, y=y, text=author_text)

        img_object.save(outpath)
        return outpath

    def _get_text_height(self, draw: ImageDraw.ImageDraw, text: str) -> int:
        bounding_box = draw.textbbox((0, 0), text, font=self._font)
        upper_y = bounding_box[3]
        bottom_y = bounding_box[1]
        height = upper_y - bottom_y
        return height

    def _draw_text_with_outline(
        self, draw: ImageDraw.ImageDraw, x: int, y: int, text: str
    ):
        """
        Draw a black outline around white text.
        """
        # Draw the black outline
        draw.text((x - 1, y - 1), text, font=self._font, fill="black")
        draw.text((x + 1, y - 1), text, font=self._font, fill="black")
        draw.text((x - 1, y + 1), text, font=self._font, fill="black")
        draw.text((x + 1, y + 1), text, font=self._font, fill="black")

        # draw white text on top of the black outline.
        draw.text((x, y), text, font=self._font, fill="white")


if __name__ == "__main__":
    meme_engine = MemeEngine.make_default_engine(output_directory="static")
    outpath = meme_engine.make_meme(
        img_path="_data/photos/dog/xander_3.jpg", text="don't do it", author="thor"
    )
    print(outpath)


# end
