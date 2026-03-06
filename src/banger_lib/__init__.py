"""
##################################################################################
#
# Bänger (Library) by Marcin Orlowski
# Because your `banner` deserves to be a `bänger`!
#
# @author    Marcin Orlowski <mail@marcinOrlowski.com>
# Copyright  ©2025-2026 Marcin Orlowski <MarcinOrlowski.com>
# @link      https://github.com/MarcinOrlowski/banger-lib
#
##################################################################################
"""

from .banger import Banger
from .exceptions import BangerError, FontNotFoundError, CharacterNotSupportedError
from . import fonts
from .fonts import (
    TtfFont,
    BaseFont,
    register_font,
    CharacterData,
    FontMetadata,
    FontInterface,
)

__version__ = "1.0.0"

__all__ = [
    # Main API
    "Banger",
    # Fonts module
    "fonts",
    "TtfFont",
    "BaseFont",
    "register_font",
    # Data structures
    "CharacterData",
    "FontMetadata",
    "FontInterface",
    # Exceptions
    "BangerError",
    "FontNotFoundError",
    "CharacterNotSupportedError",
]
