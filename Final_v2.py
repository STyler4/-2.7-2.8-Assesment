"""Rearranging code and creating functions
"""

import easygui


def add_monster():
    name_1 = easygui.enterbox("Enter the monster's name:").title()
    strength = int(easygui.enterbox("Enter the monster's strength:"))
    speed = int(easygui.enterbox("Enter the monster's speed:"))
    stealth = int(easygui.enterbox("Enter the monster's stealth:"))
    cunning = int(easygui.enterbox("Enter the monster's cunning:"))

    cards[name_1] = {
        "Strength": strength,
        "Speed": speed,
        "Stealth": stealth,
        "Cunning": cunning
    }
    easygui.msgbox(f"{name_1} added to the card catalogue.")


def find_monster():
    name_1 = easygui.enterbox("Enter the monster name you want to search for: ").title()

    if name_1 in cards:
        attributes = cards[name_1]
        easygui.msgbox(f"Match found: {name_1}\n"
                       f"Strength: {attributes['Strength']}\n"
                       f"Speed: {attributes['Speed']}"
                       f"\nStealth: {attributes['Stealth']}\n"
                       f"Cunning: {attributes['Cunning']}")
    else:
        easygui.msgbox(f"{name_1} not found")


def delete_monster():
    name_1 = easygui.enterbox("Enter the Monster name to delete:").title()

    if name_1 in cards:
        del cards[name_1]
        easygui.msgbox(f"{name_1} deleted.")
    else:
        easygui.msgbox(f"{name_1} not found.")


def output_all():
    output = "Monsters:\n"
    for name_1, attributes in cards.items():
        output += f"- {name_1}: Strength={attributes['Strength']} " \
                  f"Speed={attributes['Speed']} "
        output += f"Stealth={attributes['Stealth']} " \
                  f"Cunning={attributes['Cunning']}\n"
    easygui.msgbox(output)


# Main program
name = easygui.enterbox("What is your name")
symbol = "!"
text = "Welcome to the monster card catalogue"
sides = symbol * 3

# Output of formal greeting
formatted_text = f"{sides} {text} {name.upper()} {sides}"
top_bottom = symbol * len(formatted_text)

easygui.msgbox(formatted_text)

# Card values
card_list = ["Stoneling", "Vexscream", "Dawnmirage", "Blazegolem", "Websnake",
             "Moldvine", "Vortexwing", "Rotthing",
             "Froststep", "Wispghoul"]

cards = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}

while True:
    choice = easygui.buttonbox("What would you like to do?",
                               "Monster Cards", ["Add Monster",
                                                 "Find Monster",
                                                 "Delete Monster",
                                                 "Output all", "Exit"])

    if choice == "Add Monster":
        add_monster()

    elif choice == "Find Monster":
        find_monster()

    elif choice == "Delete Monster":
        delete_monster()

    elif choice == "Output all":
        output_all()

    elif choice == "Exit":
        symbol = "!"
        text = "Thank you for using this catalogue, Bye "
        sides = symbol * 3

        formatted_text = f"{sides} {text} {sides}"
        top_bottom = symbol * len(formatted_text)

        easygui.msgbox(formatted_text)
        break
