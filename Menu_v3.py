"""In this version I will be fixing up output problems when
finding monsters"""

import easygui

# card values
card_list = ["Stoneling: Strength=7 Speed=1 Stealth=25 Cunning=15",
             "Vexscream: Strength=1 Speed=6 Stealth=21 Cunning=19",
             "Dawnmirage: Strength=5 Speed=15 Stealth=18 Cunning=22",
             "Blazegolem: Strength=15 Speed=20 Stealth=23 Cunning=6",
             "Websnake: Strength=7 Speed=15 Stealth=10 Cunning=5",
             "Moldvine: Strength=21 Speed=18 Stealth=14 Cunning=5",
             "Vortexwing: Strength=19 Speed=13 Stealth=19 Cunning=2",
             "Rotthing: Strength=16 Speed=7 Stealth=4 Cunning=12",
             "Froststep: Strength=14 Speed=14 Stealth=17 Cunning=4",
             "Wispghoul: Strength=17 Speed=19 Stealth=3 Cunning=2"]


cards = {name: "" for name in card_list}

# Introduce different options
while True:
    choice = easygui.buttonbox("What would you like to do?", "Monster Cards", ["Add Monster", "Find Monster",
                                                                               "Delete Monster", "Output all", "Exit"])
    # Input new monster
    if choice == "Add Monster":
        name = easygui.enterbox("Enter the monsters name: ")
        cards[name] = ""

    # Find monster
    elif choice == "Find Monster":
        name = easygui.enterbox("Enter the monster name you want to search for: ")

        if name in cards:
            if cards[name] is not None:
                easygui.msgbox(f"Match found :{name}")
            else:
                easygui.msgbox(f"{name} is in the list but has no value.")
        else:
            easygui.msgbox(f"{name} not found")

    # Delete monster
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
