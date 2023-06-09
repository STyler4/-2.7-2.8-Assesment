"""Create a menu using easygui to navigate
through the problem using different options"""

import easygui

card_list = ["Stoneling", "Vexscream", "Dawnmirage", "Blazegolem", "Websnake", "Moldvine", "Vortexwing", "Rotthing",
             "Froststep", "Wispghoul"]

cards = {name: None for name in card_list}


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
                easygui.msgbox(f"Search matched: {name} ")

        else:
            easygui.msgbox(f"{name} not found")

    elif choice == "Delete Monster":
        name = easygui.enterbox("Enter the Monster name to delete:")

        if name in cards:
            del cards[name]
            easygui.msgbox(f"{name} deleted.")
        else:
            easygui.msgbox(f"{name} not found.")

    elif choice == "Output all":
        output = "Monsters:\n"
        for name in cards.keys():
            output += f"- {name}\n"
        easygui.msgbox(output)

    elif choice == "Exit":
        break
