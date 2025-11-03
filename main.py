"""
main.py - ET574 Homework 4: Dice Game Simulator
Author: Shahnaj Latif (QCC ID:23848861)

Implements a simple two-dice game with object-oriented design and a console UI.
Classes:
- Die: single die with configurable sides
- DiceGame: holds two dice; can play a round and evaluate outcome

Run this file directly to play in the console.
"""
import random
from typing import Tuple

class Die:
    def __init__(self, sides: int = 6) -> None:
        if not isinstance(sides, int) or sides < 2:
            raise ValueError("'sides' must be an integer >= 2")
        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        return f"Die(sides={self.sides})"


class DiceGame:
    def __init__(self) -> None:
        self.die1 = Die()
        self.die2 = Die()

    def play_round(self) -> Tuple[int, int, int, str]:
        r1 = self.die1.roll()
        r2 = self.die2.roll()
        total = r1 + r2
        result = self.evaluate_roll(total)
        return r1, r2, total, result

    def evaluate_roll(self, total: int) -> str:
        # Game rules:
        # 7 or 11 -> Win
        # 2, 3, 12 -> Lose
        # 4–6, 8–10 -> Roll Again
        if total in (7, 11):
            return "Win"
        if total in (2, 3, 12):
            return "Lose"
        if total in (4, 5, 6, 8, 9, 10):
            return "Roll Again"
        # For completeness with non-2d6 totals
        return "Invalid"


def main() -> None:
    print("=== Dice Game Simulator ===")
    game = DiceGame()

    while True:
        print("\nMenu:")
        print("1. Play a round")
        print("2. Exit")
        choice = input("Choose an option (1/2): ").strip()

        if choice == "1":
            r1, r2, total, result = game.play_round()
            print(f"You rolled: {r1} and {r2}")
            print(f"Total: {total}")
            print(f"Result: {result}")
        elif choice == "2" or choice.lower() == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
