# -*- coding: utf-8 -*


import re

import pyperclip


def clear(old_str):
        res = ""
        lines = old_str.splitlines()
        for line in lines:
            if len(line) > 18:
                res += "#### " + line + "\n\n"
        return res

data = pyperclip.paste()
data = clear(data)
print(data)
pyperclip.copy(data)