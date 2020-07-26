#!/usr/bin/env python3

import re, sys, time, random
from .colors import _color_chart

def _get_foreground(color):
	if isinstance(color, int):
		return _esc + "38;5;" + str(color) + _end

	spec = "hex" if re.match("^#", color) else "name"
	if _color_chart[spec][color]:
		return _esc + "38;5;" + _color_chart[spec][color] + _end
	else:
		return ""

def _get_background(color):
	if isinstance(color, int):
		return _esc + "48;5;" + str(color) + _end

	spec = "hex" if re.match("^#", color) else "name"
	if _color_chart[spec][color]:
		return _esc + "48;5;" + _color_chart[spec][color] + _end
	else:
		return ""

def _typewrite(olist, wpm=50):
	for letter in olist:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10.0/wpm)
	print("")

def _typeslow(olist, speed=0.1):
	for letter in olist:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(speed)
	print("")

def _validate_effects(fg=None, bg=None, bold=None, dim=None, underlined=None, blink=None, reverse=None, hidden=None):
	fg = _get_foreground(fg) if not fg == None else ""
	bg = _get_background(bg) if not bg == None else ""
	bold = _effects["bold"] if bold == 1 else ""
	dim = _effects["dim"] if dim == 1 else ""
	underlined = _effects["underlined"] if underlined == 1 else ""
	blink = _effects["blink"] if blink == 1 else ""
	reverse = _effects["reverse"] if reverse == 1 else ""
	hidden = _effects["hidden"] if hidden == 1 else ""
	return fg, bg, bold, dim, underlined, blink, reverse, hidden

_attributes = {
	"bold": "1",
	"dim": "2",
	"underlined": "4",
	"blink": "5",
	"reverse": "7",
	"hidden": "8",
	"reset_all": "0",
	"reset_bold": "21",
	"reset_dim": "22",
	"reset_underlined": "24",
	"reset_blink": "25",
	"reset_reverse": "27",
	"reset_hidden": "28"
}

_esc = "\033["
_end = "m"
_reset_all = _esc + _attributes["reset_all"] + _end
_reset_bold = _esc + _attributes["reset_bold"] + _end
_reset_dim = _esc + _attributes["reset_dim"] + _end
_reset_underlined = _esc + _attributes["reset_underlined"] + _end
_reset_blink = _esc + _attributes["reset_blink"] + _end
_reset_reverse = _esc + _attributes["reset_reverse"] + _end
_reset_hidden = _esc + _attributes["reset_hidden"] + _end
_bkgd_default = _esc + "49" + _end

_effects = {
	"bold": _esc + _attributes["bold"] + _end,
	"dim": _esc + _attributes["dim"] + _end,
	"underlined": _esc + _attributes["underlined"] + _end,
	"blink": _esc + _attributes["blink"] + _end,
	"reverse": _esc + _attributes["reverse"] + _end,
	"hidden": _esc + _attributes["hidden"] + _end
}
