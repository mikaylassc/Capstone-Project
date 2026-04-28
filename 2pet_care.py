"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Capstone Project: Pet Care Assistant (Final Version)
"""

# -------------------------------
# IMPORTS
# -------------------------------
import json
import random
from datetime import datetime

# -------------------------------
# CONSTANTS
# -------------------------------
FILE_NAME = "pet_data.json"
LOG_FILE = "activity_log.txt"

# -------------------------------
# DEFAULT DATA
# -------------------------------
def get_default_database():
    return {
        "puppy": [
            "Short play sessions throughout the day",
            "Basic obedience training",
            "Socialization with people and other dogs"
        ],
        "adult": [
            "Daily walks or runs",
            "Interactive toys for mental stimulation",
            "Consistent feeding and exercise schedule"
        ],
        "senior": [
            "Gentle walks and light activity",
            "Comfortable sleeping areas",
            "More frequent health checkups"
        ]
    }

# -------------------------------
# FILE HANDLING
# -------------------------------
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Using default data.")
        return get_default_database()


def save_data(care_database):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(care_database, file, indent=4)
    except Exception as e:
        print("Error saving data:", e)

# -------------------------------
# INPUT VALIDATION
# -------------------------------
def get_valid_age():
    while True:
        try:
            age = int(input("\nEnter your dog's age in years: "))
            if age < 0:
                print("Age cannot be negative.")
                continue
            return age
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_activity_level():
    valid_levels = ["low", "medium", "high"]

    while True:
        level = input("Is your dog low, medium, or high energy? ").lower()
        if level in valid_levels:
            return level
        else:
            print("Invalid input. Please type low, medium, or high.")

# -------------------------------
# CORE FUNCTIONS
# -------------------------------
def get_life_stage(age):
    if age < 2:
        return "puppy"
    elif 2 <= age <= 7:
        return "adult"
    else:
        return "senior"


def extra_care_tips(stage):
    if stage == "puppy":
        return "Puppies benefit from training and socialization."
    elif stage == "adult":
        return "Adult dogs need consistent exercise and a balanced diet."
    else:
        return "Senior dogs may need joint support and more frequent vet visits."


def display_stage_activities(stage, care_database):
    print(f"\nRecommended activities for a {stage}:")
    for activity in care_database.get(stage, []):
        print(f"- {activity}")

# -------------------------------
# LIBRARY FEATURES
# -------------------------------
def get_random_tip(stage, care_database):
    tips = care_database.get(stage, [])
    return random.choice(tips) if tips else "No tips available."


def log_activity(stage):
    try:
        with open(LOG_FILE, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - Checked advice for a {stage}\n")
    except Exception as e:
        print("Logging error:", e)

# -------------------------------
# AUTOMATION FEATURE (MILESTONE 7)
# -------------------------------
def analyze_log():
    """
    Reads the activity log and generates a usage report.
    Demonstrates automation using file operations.
    """
    stage_count = {"puppy": 0, "adult": 0, "senior": 0}

    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()

        for line in lines:
            if "puppy" in line:
                stage_count["puppy"] += 1
            elif "adult" in line:
                stage_count["adult"] += 1
            elif "senior" in line:
                stage_count["senior"] += 1

        total = sum(stage_count.values())

        if total == 0:
            print("No data available yet.")
            return

        most_common = max(stage_count, key=stage_count.get)

        print("\n--- Usage Report ---")
        print(f"Total checks: {total}")
        print(f"Most common life stage: {most_common}")
        print("Breakdown:")
        for stage, count in stage_count.items():
            print(f"{stage.capitalize()}: {count}")

        with open("report.txt", "w") as report:
            report.write("Pet Care Assistant Report\n")
            report.write(f"Total checks: {total}\n")
            report.write(f"Most common stage: {most_common}\n")
            for stage, count in stage_count.items():
                report.write(f"{stage}: {count}\n")

        print("Report saved to report.txt")

    except FileNotFoundError:
        print("No log file found yet. Use the program first.")

# -------------------------------
# OOP CLASS
# -------------------------------
class Dog:
    def __init__(self, age, activity_level):
        self.age = age
        self.activity_level = activity_level

    def get_basic_advice(self):
        if self.age < 2 and self.activity_level == "high":
            return "Your dog is young and energetic. Make sure they get plenty of exercise!"
        elif 2 <= self.age <= 7 and self.activity_level == "medium":
            return "Your dog is an adult with moderate energy. Regular walks are recommended."
        else:
            return "Your dog may benefit from a calmer routine and regular vet checkups."

    def get_life_stage(self):
        return get_life_stage(self.age)

    def extra_care_tips(self):
        return extra_care_tips(self.get_life_stage())

# -------------------------------
# MAIN PROGRAM
# -------------------------------
print("Welcome to the Pet Care Assistant (Final Version)")

care_database = load_data()

while True:
    print("\nMenu:")
    print("1. Check dog care advice")
    print("2. View usage report")
    print("3. Exit")

    option = input("Choose an option (1-3): ")

    if option == "1":
        dog_age = get_valid_age()
        activity_level = get_valid_activity_level()

        my_dog = Dog(dog_age, activity_level)

        print("\n" + my_dog.get_basic_advice())

        stage = my_dog.get_life_stage()
        print("Life Stage:", stage)
        print("Additional Advice:", my_dog.extra_care_tips())

        display_stage_activities(stage, care_database)

        print("Bonus Tip:", get_random_tip(stage, care_database))

        log_activity(stage)
        save_data(care_database)

    elif option == "2":
        analyze_log()

    elif option == "3":
        print("Thank you for using the Pet Care Assistant!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")