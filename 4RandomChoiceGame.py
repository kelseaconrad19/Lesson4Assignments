# Task 1: Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.
import random

items = ["coins", "sword", "axe", "wolf", "horse", "torch", "dragon", "medallion", "treasure", "robe", "wand", "spear"]

game_choice = random.choice(items)
user_guess = input(f"What item do you believe was chosen? Type an item from this list: {items}: ").lower()

if user_guess == game_choice:
    print(f"You guessed {user_guess}. That is correct!")
else:
    print(f"Alas, that is not the item that was chosen. The {game_choice} was the chosen item")

