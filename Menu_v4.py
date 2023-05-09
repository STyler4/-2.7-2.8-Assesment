"""In this version I have created values for monsters already in the list but also for the monsters that are
being created/ input into the program """

import easygui

# card values
card_list = ["Stoneling", "Vexscream", "Dawnmirage", "Blazegolem", "Websnake", "Moldvine", "Vortexwing", "Rotthing",
             "Froststep", "Wispghoul"]


cards = {
    "Stoneling": {"strength": 5, "speed": 3, "stealth": 2, "cunning": 1},
    "Vexscream": {"strength": 8, "speed": 7, "stealth": 4, "cunning": 3},
    "Dawnmirage": {"strength": 3, "speed": 9, "stealth": 8, "cunning": 5},
    "Blazegolem": {"strength": 10, "speed": 2, "stealth": 1, "cunning": 2},
    "Websnake": {"strength": 4, "speed": 6, "stealth": 9, "cunning": 4},
    "Moldvine": {"strength": 2, "speed": 4, "stealth": 7, "cunning": 9},
    "Vortexwing": {"strength": 6, "speed": 8, "stealth": 3, "cunning": 6},
    "Rotthing": {"strength": 7, "speed": 3, "stealth": 1, "cunning": 5},
    "Froststep": {"strength": 9, "speed": 5, "stealth": 2, "cunning": 3},
    "Wispghoul": {"strength": 2, "speed": 9, "stealth": 8, "cunning": 7}, }

while True:
    choice = easygui.buttonbox("What would you like to do?", "Monster Cards", ["Add Monster", "Find Monster",
                                                                               "Delete Monster", "Output all", "Exit"])
    # Input new monster
    if choice == "Add Monster":
        name = easygui.enterbox("Enter the monster's name:").title()
        strength = int(easygui.enterbox("Enter the monster's strength:"))
        speed = int(easygui.enterbox("Enter the monster's speed:"))
        stealth = int(easygui.enterbox("Enter the monster's stealth:"))
        cunning = int(easygui.enterbox("Enter the monster's cunning:"))

        cards[name] = {
            "strength": strength,
            "speed": speed,
            "stealth": stealth,
            "cunning": cunning
        }
        easygui.msgbox(cards[name], name)
    # Find monster
    elif choice == "Find Monster":
        name = easygui.enterbox("Enter the monster name you want to search for: ").title()

        if name in cards:
            if cards[name]:
                easygui.msgbox(f"Match found: {name}\nStrength: {cards[name]['strength']}\nSpeed: "
                               f"{cards[name]['speed']}\nStealth: {cards[name]['stealth']}\nCunning: "
                               f"{cards[name]['cunning']}")
            else:
                easygui.msgbox(f"{name} is in the list but has no value.")
        else:
            easygui.msgbox(f"{name} not found")

    # Delete monster
    elif choice == "Delete Monster":
        name = easygui.enterbox("Enter the Monster name to delete:").title()

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
