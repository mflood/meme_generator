from PIL import Image, ImageDraw, ImageFont

from meme_generator.fonts import get_font, FontId

from typing import Optional

class MemeEngine():

    def __init__(self, output_directory: str, font: ImageFont.FreeTypeFont, max_width_px: Optional[int]):
        """
            max_width_px: maximum width of iage in pixels
    Arguments:
        in_path {str} -- the file location for the input image.
        out_path {str} -- the desired location for the output image.
        crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
        """
        self._static_directory = output_directory
        self._font = font
        self._max_width_px = max_width_px
        
    @classmethod
    def make_default_engine(cls, output_directory):
        """
        Make an engine appropriate for this project
        """
        font = get_font(FontId.K_LILITA_ONE_REGULAR, size=20)
        return cls(output_directory=output_directory,
                   font=font,
                   max_width_px=500)

    def make_meme(self, source_image_path: str, quote_body: str, quote_author: str) -> str:
        """
            returns: relative URL path of image
        """
        print(f"loading image '{source_image_path}'")
        img_object = Image.open(source_image_path)

        outpath = "static/generated.jpg"

        if self._max_width_px is not None:
            ratio = self._max_width_px / float(img_object.size[0])
            height = int(ratio * float(img_object.size[1]))
            img_object = img_object.resize((self._max_width_px, height), Image.NEAREST)

        if quote_body is not None:
            draw = ImageDraw.Draw(img_object)
            draw.text((10, 30), quote_body, font=self._font, fill='white')

        if quote_author is not None:
            draw = ImageDraw.Draw(img_object)
            draw.text((40, 30), quote_author, font=self._font, fill='white')

        img_object.save(outpath)
        return outpath
        
if __name__=='__main__':
    meme_engine = MemeEngine.make_default_engine(output_directory="static")
    outpath = meme_engine.make_meme(source_image_path="_data/photos/dog/xander_3.jpg", 
    quote_body="don't do it",
    quote_author = "thor")
    print(outpath)


