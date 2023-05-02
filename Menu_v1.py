"""Create a menu using easygui to navigate
through the problem using different options"""

import easygui

cards: {}

card_list = ["Stoneling", "Vexscream", "Dawnmirage", "Blazegolem", "Websnake", "Moldvine", "Vortexwing", "Rotthing",
             "Froststep", "Wispghoul"]

while True:
    choice = easygui.buttonbox("What would you like to do?", "Monster Cards", ["Add Monster", "Find Monster",
                                                                               "Delete Monster", "Output all", "Exit"])
    if choice == "Add Monster":
        name = easygui.enterbox("Enter the monsters name: ")

        cards[name] = None

    elif choice == "Find Monster":
        name = easygui.enterbox("Enter the monster name you want to search for: ")

        if name in cards:
            if cards[name] is not None:
                easygui.msgbox(f"{name}: ")
