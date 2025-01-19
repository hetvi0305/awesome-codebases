# Sample Coding Questions Week 02
# First Name: Hetvi
# Last Name: Patel
import random

def main():
    # Define the weapons array
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

    try:
        # Roll the dice (1-6)
        weaponRoll = random.randint(1, 6)
        print(f"You rolled: {weaponRoll}")

        # Get the hero's weapon based on the roll
        hero_weapon = weapons[weaponRoll - 1]
        print(f"Your weapon is: {hero_weapon}")

        # Conditions for weapon strength
        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend.")
        elif weaponRoll <= 4:
            print("Your weapon is meh.")
        else:
            print("Nice weapon, friend!")

        # Check if the weapon is not Fist
        if hero_weapon != "Fist":
            print("Thank goodness you didn't roll the Fist...")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()