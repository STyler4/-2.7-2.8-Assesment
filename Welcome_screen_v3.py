"""Create A Welcome Screen using easygui
Expanding on Welcome_screen_v2"""

import easygui

name = easygui.enterbox("What is your name")
symbol = "!"
text = "Welcome to the monster card catalogue"
sides = symbol * 3

formatted_text = f"{sides} {text} {name.upper()} {sides}"
top_bottom = symbol * len(formatted_text)

easygui.msgbox(formatted_text)
