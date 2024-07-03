from PIL import Image, ImageDraw, ImageFont

from meme_generator.fonts import get_font, FontId

import random
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap
from typing import Optional



def generate_random_image_path(directory: str) -> str:
    """
        Generate a random output filepath for generated memes
    """
    random_int = random.randint(100000, 999999)  # Generate a random integer between 1000 and 9999
    filename = f"generated_{random_int}.jpg"  # Create a filename using the random integer
    return os.path.join(directory, filename)  # Combine the directory and filename to create the full path



    offset += draw.textbbox((0, 0), line, font=self._font)[3] - draw.textbbox((0, 0), line, font=self._font)[1]

class MemeEngine():

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
        print(f"loading image '{img_path}'")
        img_object = Image.open(img_path)

        outpath = generate_random_image_path(directory=self._static_directory)
        max_width = width

        # Resize image
        if width is not None:
            ratio = width / float(img_object.size[0])
            height = int(ratio * float(img_object.size[1]))
            img_object = img_object.resize((width, height), Image.NEAREST)

        # Draw text on image
        draw = ImageDraw.Draw(img_object)
        margin = 10
        offset = 30

        # Wrap text
        wrapped_text = textwrap.fill(text, width=40)
        wrapped_author = f"- {author}"

        # Draw wrapped text
        for line in wrapped_text.split('\n'):

            x, y = margin, offset

            self.draw_text_with_outline(draw=draw, x=margin, y=offset, line=line)

            # Get size and update offset
            offset += draw.textbbox((0, 0), line, font=self._font)[3] - draw.textbbox((0, 0), line, font=self._font)[1]


        # Draw author
        offset += 10  # Additional space between quote and author
        margin += 40 # indent
        self.draw_text_with_outline(draw=draw, x=margin, y=offset, line=wrapped_author)

        # Save image
        img_object.save(outpath)
        return outpath

    def draw_text_with_outline(self, draw: ImageDraw.ImageDraw, x: int, y: int, line: str):
        """
            return the height 
        """
        print(type(draw))
        # Draw outline
        draw.text((x - 1, y - 1), line, font=self._font, fill='black')
        draw.text((x + 1, y - 1), line, font=self._font, fill='black')
        draw.text((x - 1, y + 1), line, font=self._font, fill='black')
        draw.text((x + 1, y + 1), line, font=self._font, fill='black')

        # draw text
        draw.text((x, y), line, font=self._font, fill='white')

        



if __name__=='__main__':
    meme_engine = MemeEngine.make_default_engine(output_directory="static")
    outpath = meme_engine.make_meme(img_path="_data/photos/dog/xander_3.jpg", 
    text="don't do it",
    author = "thor")
    print(outpath)


