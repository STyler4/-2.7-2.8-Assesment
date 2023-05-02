"""Create A Welcome Screen using easygui"""

import easygui

symbol = "!"
text = "Welcome to the monster card catalogue"
sides = symbol * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = symbol * len(formatted_text)

easygui.msgbox(formatted_text)

