"""In this version I have fixed the find the monster problem"""

import easygui

# card values
card_list = ["Stoneling", "Vexscream", "Dawnmirage", "Blazegolem", "Websnake", "Moldvine", "Vortexwing", "Rotthing",
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
            attributes = cards[name]
            easygui.msgbox(f"Match found: {name}\nStrength: {attributes['Strength']}\nSpeed: {attributes['Speed']}"
                           f"\nStealth: {attributes['Stealth']}\nCunning: {attributes['Cunning']}")
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
        for name, attributes in cards.items():
            output += f"- {name}: Strength={attributes['Strength']} Speed={attributes['Speed']} "
            output += f"Stealth={attributes['Stealth']} Cunning={attributes['Cunning']}\n"
        easygui.msgbox(output)

    elif choice == "Exit":
        break