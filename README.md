# TextEffects
---
Very simple Python library for color and formatting in the terminal.

https://github.intuit.com/gdanko/texteffects
# Installation
---
To install the texteffects module you must clone the repository and use pip to install it.
```
pip install file:///path/to/local/texteffects/repo
```
# Usage
---
Once you have a constructor, using the NetGenie module is quite easy.
```python
from texteffects import colorize, rainbow

colorize("This is a test", fg="blue", bg="green")
rainbow("This is rainbow text", blink=1, underline=1)
```
# Functions
---
* colors_by_name() - Displays a color swatch list of all available colors by name.
* colors_by_code() - Displays a color swatch list of all available colors by code.
* colorize(string, [options]) - Colorize a string of text.
* rainbow(string, [options]) - Print a string of text in a rainbow effect.
* foreground(color|#hex) - Returns the ANSI sequence for <color> foreground.
* background(color|#hex) - Returns the ANSI sequence for <color> background.
* fg(color|#hex) - Alias for foreground.
* bg(color|#hex) - Alias for background.
* bold() - Return the ANSI sequence for bold text.
* dim() - Return the ANSI sequence for dim text.
* underlined() - Return the ANSI sequence for underlined text.
* blink() - Return the ANSI sequence for blinking text.
* reverse() - Return the ANSI sequence for reversed text.
* hidden() - Return the ANSI sequence for hidden text.
* reset_all() - Returns the ANSI sequence for terminal text reset.
* reset_bold() - Returns the ANSI sequence for terminal bold reset.
* reset_dim() - Returns the ANSI sequence for terminal dim reset.
* reset_underlined() - Returns the ANSI sequence for terminal underlined reset.
* reset_blink() - Returns the ANSI sequence for terminal blink reset.
* reset_reverse() - Returns the ANSI sequence for terminal reverse reset.
* reset_hidden() - Returns the ANSI sequence for terminal hidden reset.

# Options for colorize and rainbow
---
These two functions have a few options you can specify to further stylize the text.
The following options require arguments.
* fg=<color> (colorize only) - Set the foreground color.
* bg=<color> - Set the background color.
* wpm=<int> - Simulate typing, set the words per minute speed.
* speed=<float> - Specify a delay between the display of each character. The <float> is reperesented in seconds.

The following options are enabled by setting them to 1.
* bold - Boldens the text.
* dim - Dims the texts.
* underlined - Underlines the text.
* blink - Blinks the text.
* reverse - Reverses the text.
* hide - Hides the text.
* backwards - Prints the text backwards.

# Examples
---
```python
colorize("My color text", bold=1, underlined=1, dim=1, fg="#000000", bg="red")
rainbow("My typrwritten text", bg="green", wpm=40)
```
