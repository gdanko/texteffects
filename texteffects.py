#!/usr/bin/env python3

"""
Documentation here
"""

from .utils import _get_foreground, _get_background, _attributes, _reset_all, _validate_effects, _typewrite, _typeslow, _effects, _reset_blink
from .colors import _color_chart
from pprint import pprint
import sys

# http://www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/
# Add staggered blink

__author__ = "Gary Danko"
__copyright__ = "Copyright 2016-17, Intuit, Inc."
__maintainer__ = "Gary Danko"
__version__ = "0.1.0"
__status__ = "Development"

class texteffects(object):
	def __init__(self):
		return self

def _hrun(start, width, padding=0):
	return [None] * padding + list(range(start, start + width)) + [None] * padding

def _vrun(start, width, height, padding=0):
	return [_hrun(s, width, padding) for s in range(start, start + width * height, width)]

def _fg_seq(color):
	return '\033[38;5;%dm' % color

def _bg_seq(color):
	return '\033[48;5;%dm' % color

def _color_bar_name(seq, color, trail, max_length):
	if color is None:
		return "%s  %s" % (_reset_all, trail)
	else:
		padding = max_length + 4
		return seq(color) + _color_chart["code"][str(color)].center(padding) + _reset_all

def colors_by_name():
	"""
    Print a swatch using all 256 colors of 256-color-capable terminals.
	"""
	pprint(_color_chart["name"])
	max_length = 0
	for name in _color_chart["name"]:
		if len(name) > max_length:
			max_length = len(name)

	layout = [
		_vrun(0, 4, 4, 0), # 16 standard xterm colors   # start=0, width=8, height=2, padding=0
		_vrun(16, 3, 72, 1), # 6x6x6 color cube         # start=16, width=6, height=36, padding=1
		_vrun(232, 4, 3, 0)  # 24 grey levels           # start=232, width=8, height=3, padding=0
	]

	for block in layout:
		print("")
		for row in block:
			fg_bar = "".join(_color_bar_name(_fg_seq, color, "", max_length) for color in row)
			bg_bar = "".join(_color_bar_name(_bg_seq, color, " ", max_length) for color in row)
			print("%s%s %s%s" % (fg_bar, _reset_all, bg_bar, _reset_all))

def _color_bar_code(seq, color, trail):
	if color is None:
		return '%s  %s' % (_reset_all, trail)
	else:
		return "%s %03d%s" % (seq(color), color, trail)

def colors_by_code():
	layout = [
		_vrun(0, 8, 2), # 16 standard xterm colors	  # start=0, width=8, height=2, padding=0
		_vrun(16, 6, 6 * 6, 1), # 6x6x6 color cube	  # start=16, width=6, height=36, padding=1
		_vrun(16 + 6 * 6 * 6, 8, 3), # 24 grey levels   # start=232, width=8, height=3, padding=0
	]
	for block in layout:
		print("")
		for row in block:
			fg_bar = "".join(_color_bar_code(_fg_seq, color, "") for color in row)
			bg_bar = "".join(_color_bar_code(_bg_seq, color, " ") for color in row)
			print("%s%s %s%s" % (fg_bar, _reset_all, bg_bar, _reset_all))

def colorize(string=None, fg=None, bg=None, bold=None, dim=None, underlined=None, blink=None, reverse=None, hidden=None, backwards=None, wpm=None, speed=None):
	"""
    Colorize text strings.

    Parameters:
        string: The string to colorize.
        fg: The foreground color.
        bg: The background color.
        bold: Set to 1 to enable bold text.
        dim: Set to 1 to enable dim text.
        underlined: Set to 1 to enable underlined text.
        blink: Set to 1 to enable blinking text.
        reverse: Set to 1 to enable reverse text.
        hidden: Set to 1 to enable hidden text.
        backwards: Set to 1 to enable backwards text.
        wpm: Simulate a typewriter. Set to INT to determine words per minute.
        speed: Print text slowly. Set to FLOAT <seconds>.
	"""
	if backwards: string = string[::-1]
	olist = []
	fg, bg, bold, dim, underlined, blink, reverse, hidden = _validate_effects(fg, bg, bold, dim, underlined, blink, reverse, hidden)
	olist = [fg, bg, bold, dim, underlined, blink, reverse, hidden, string, _reset_all]
	if wpm:
		_typewrite(olist, wpm)
	elif speed:
		_typeslow(olist, speed)
	else:
		print("".join(olist))

def rainbow(string=None, bg=None, bold=None, dim=None, underlined=None, blink=None, reverse=None, hidden=None, backwards=None, wpm=None, speed=None):
	"""
    Print rainbow text.

    Parameters:
        bg: The background color.
        bold: Set to 1 to enable bold text.
        dim: Set to 1 to enable dim text.
        underlined: Set to 1 to enable underlined text.
        blink: Set to 1 to enable blinking text.
        reverse: Set to 1 to enable reverse text.
        hidden: Set to 1 to enable hidden text.
        backwards: Set to 1 to enable backwards text.
        wpm: Simulate a typewriter. Set to INT to determine words per minute.
        speed: Print text slowly. Set to FLOAT <seconds>.
	"""
	olist, clist = [], ["maroon", "dark_orange", "olive", "green", "navy", "blue_violet", "purple"]
	if backwards: string = string[::-1]
	slist = list(string)
	scounter, ccounter = 0, 0
	while scounter < len(slist):
		if not slist[scounter] == " ":
			if ccounter == len(clist):
				ccounter = 0
			fg, bkgd, bold, dim, underlined, blink, reverse, hidden = _validate_effects(clist[ccounter], bg, bold, dim, underlined, blink, reverse, hidden)
			olist.append("".join([fg, bkgd, bold, dim, underlined, blink, reverse, hidden, slist[scounter]]))
			ccounter += 1
		else:
			olist.append(slist[scounter])
		scounter += 1
	olist.append(_reset_all)

	if wpm:
		_typewrite(olist, wpm)
	elif speed:
		_typeslow(olist, speed)
	else:
		print("".join(olist))

def reset_all():
	"""
    Return the ANSI sequence for text reset.
	"""
	return _reset_all

def reset_bold():
	return _reset_bold

def reset_dim():
	return _reset_dim

def reset_underlined():
	return _reset_underlined

def reset_blink():
	return _reset_blink

def foreground(color):
	"""
    Return the ANSI sequence for <color> foreground.
	"""
	return _get_foreground(color)

def fg(color):
	"""
    This is an alias for foreground
	"""
	return _get_foreground(color)

def background(color):
	"""
    Return the ANSI sequence for <color> background.
	"""
	return _get_background(color)

def bg(color):
	"""
    This is an alias for background
	"""
	return _get_background(color)

def bold():
	"""
    Return the ANSI sequence for bold text
	"""
	return _effects["bold"]

def dim():
	"""
    Return the ANSI sequence for dim text
	"""
	return _effects["dim"]

def underlined():
	"""
    Return the ANSI sequence for underlined text
	"""
	return _effects["underlined"]

def blink():
	"""
    Return the ANSI sequence for blinking text
	"""
	return _effects["blink"]

def reverse():
	"""
    Return the ANSI sequence for reversed text
	"""
	return _effects["reverse"]

def hidden():
	"""
    Return the ANSI sequence for hidden text
	"""
	return _effects["hidden"]
