
# System packages
import csv
import os.path

# External packages
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from colored import Fore, Back, Style

# Calorie Goals
CALORIE_GOAL_LIMIT = 3600 # kcal
PROTEIN_GOAL = 200 # grams
FAT_GOAL = 80 # grams
CARBS_GOAL= 300 # grams

today = []

# dataclasses
@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int

# Functions for diet entries
def add_food_entry(entries):
    name = input("Enter the food name: ")
    try:
        calories = float(input("Enter the calories: "))
        protein = float(input("Enter the protein (g): "))
        fat = float(input("Enter the fat (g): "))
        carbs = float(input("Enter the carbs (g): "))
    except ValueError:
        print("Invalid input. Please enter a number for calories, protein, fat, and carbs.")
        return

    entries.append([name, calories, protein, fat, carbs])
    print("Food entry added successfully.")

def display_entries(entries):
    if not entries:
        print("No entries yet.")
        return

    with open("diet_entries.txt", "w") as file:
        file.write("Food Entries:\n")
        for entry in entries:
            file.write(f"{entry[0]}: Calories - {entry[1]}, Protein - {entry[2]}g, Fat - {entry[3]}g, Carbs - {entry[4]}g\n")

    print("Entries saved to 'diet_entries.txt'.")

def save_entries(entries, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(entries)

def load_entries(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def main():
    entries_file = "diet_entries.csv"
    entries = load_entries(entries_file)
# Menu function
    while True:
        print(f"{Style.italic}{Fore.medium_turquoise}{Back.black}Welcome to Your Diet Tracker!{Style.reset}")
        print(f"{Fore.dark_khaki}{Back.grey_3}1. Add Food Entry")
        print("2. Display Entries")
        print("3. Save Entries")
        print("4. Add Meal to Chart")
        print("5. Visualise Chart")
        print(f"6. Exit{Style.reset}")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_food_entry(entries)
        elif choice == '2':
            display_entries(entries)
        elif choice == '3':
            save_entries(entries, entries_file)
            print("Entries saved successfully.")
        elif choice == '4':
            print("Adding a new food")
            name = input("Name: ")
            calories = int(input("Calories: "))
            proteins = int(input("proteins: "))
            fats = int(input("fats: "))
            carbs = int(input("carbs: "))
            food = Food(name, calories, proteins, fats, carbs)
            today.append(food)
            print("Successfully added!")
        elif choice == '5':
            calorie_sum = sum(food.calories for food in today)
            protein_sum = sum(food.protein for food in today)
            fat_sum = sum(food.fat for food in today)
            carbs_sum = sum(food.carbs for food in today)

            fig, axs = plt.subplots(2,2)
            axs[0, 0].pie([protein_sum, fat_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f%%")
            axs[0, 0].set_title("Macronutrients Distribution")
            axs[0, 1].bar([0, 1, 2], [protein_sum, fat_sum, carbs_sum], width=0.4)
            axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4)
            axs[0, 1].set_title("Macronutrients Progress")
            axs[1, 0].pie([calorie_sum, CALORIE_GOAL_LIMIT - calorie_sum], labels=["Calories", "Remaining"], autopct="%1.1f%%")
            axs[1, 0].set_title("Calories Goal Progress")
            axs[1, 1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]), label=["Calories Consumed"])
            axs[1, 1].plot(list(range(len(today))), [CALORIE_GOAL_LIMIT] * len(today), label=["Calorie Goal"])
            axs[1, 1].legend()
            axs[1, 1].set_title("Calories Progress Over Time")
            fig.tight_layout()
            plt.show()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
