#!/usr/bin/env python3

import json

filename = "chart3.json"
f = open(filename, "r")
content = f.read().rstrip()
_color_chart = json.loads(content)
