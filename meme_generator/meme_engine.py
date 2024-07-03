from PIL import Image, ImageDraw, ImageFont

from meme_generator.fonts import get_font, FontId

from typing import Optional

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

    # make_meme(self, img_path, text, author, width=500) -> str
    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """
            returns: relative URL path of image
        """
        print(f"loading image '{img_path}'")
        img_object = Image.open(img_path)

        outpath = "static/generated.jpg"

        if width is not None:
            ratio = width / float(img_object.size[0])
            height = int(ratio * float(img_object.size[1]))
            img_object = img_object.resize((width, height), Image.NEAREST)

        if text is not None:
            draw = ImageDraw.Draw(img_object)
            draw.text((10, 30), text, font=self._font, fill='white')

        if author is not None:
            draw = ImageDraw.Draw(img_object)
            draw.text((40, 30), author, font=self._font, fill='white')

        img_object.save(outpath)
        return outpath
        
if __name__=='__main__':
    meme_engine = MemeEngine.make_default_engine(output_directory="static")
    outpath = meme_engine.make_meme(img_path="_data/photos/dog/xander_3.jpg", 
    text="don't do it",
    author = "thor")
    print(outpath)


