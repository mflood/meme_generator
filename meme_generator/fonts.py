"""
    defines FontId and get_font()
    to create an ImageFont
    from fonts that are included in this project
"""
import os
from enum import Enum
from typing import Dict

from PIL import ImageFont

_CURRENT_DIR = os.path.dirname(__file__)

_FONTS_DIR = os.path.join(_CURRENT_DIR, "font_data")


class FontId(Enum):
    """
    All the fonts we support
    """

    K_LILITA_ONE_REGULAR = "k_lilita_one_regular"


_FONT_PATHS: Dict[FontId, str] = {
    FontId.K_LILITA_ONE_REGULAR: os.path.join(
        _FONTS_DIR, "Lilita_One", "LilitaOne-Regular.ttf"
    )
}


def get_font(font_id: FontId, size: int) -> ImageFont.FreeTypeFont:
    """
    Return an ImageFont from a ttf file that we have

    :param font_id: a value from enim FontId e.g. FontId.K_LILITA_ONE_REGULAR
    :param size: font size e.g. 20
    """
    path = _FONT_PATHS[font_id]
    font = ImageFont.truetype(path, size=size)
    return font
