"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Capstone Project: Pet Care Assistant
"""
# This programs provides advice on pet care based on the dog's age and activity level.

print("Welcome to the Pet Care Assistant!")

# Ask the user for input
dog_age = int(input("Enter your dog's age in years: "))
activity_level = input("Is your dog low, medium, or high energy? ").lower()

# Decide what advice to give
if dog_age < 2 and activity_level == "high":
    print("Your dog is young and energetic. Make sure they get plenty of exercise!")
elif dog_age >= 2 and dog_age <= 7 and activity_level == "medium":
    print("Your dog is an adult with moderate energy. Regular walks are recommended.")
else:
    print("Your dog may benefit from a calmer routine and regular vet checkups.")

"""
Milestone 2 Enhancements: Loops and Functions (Part 2: Capstone Project) 

In this section, I expanded the original Pet Care Assistant program by introducing loops/functions and repetition control.

1. I defined two functions:
   - get_life_stage(age): Determines whether the dog is a puppy, adult, or senior based on age.
   - extra_care_tips(stage): Returns additional care recommendations based on the life stage.

2. Both functions use parameters and return values, improving organization and reducing repetition.

3. I implemented a while loop to allow the user to continue receiving advice without restarting the program. 
The loop runs until the user chooses to exit.

These additions improve readability, modularity, and overall program functionality while preserving the original milestone logic.
"""

    # Function 1: Determines life stage of the dog
def get_life_stage(age):
    if age < 2:
        return "puppy"
    elif 2 <= age <= 7:
        return "adult"
    else:
        return "senior"

# Function 2: Gives additional care tips
def extra_care_tips(stage):
    if stage == "puppy":
        return "Puppies benefit from training and socialization."
    elif stage == "adult":
        return "Adult dogs need consistent exercise and a balanced diet."
    else:
        return "Senior dogs may need joint support and more frequent vet visits."
    # Loop to allow the user to check multiple dogs

"""
Milestone 3 Additions: Strings and Data Structures (Modules 6–8)

I expanded the Pet Care Assistant by adding strings, lists, dictionaries, and iteration to manage pet care information more effectively.

1. I created a dictionary called care_database that stores recommended activities and care tips for each life stage (puppy, adult, senior).

2. Each life stage stores a list of recommended activities. Lists allow multiple pieces of related information to be grouped together.

3. I created a function called display_stage_activities(stage) that retrieves the list of activities from the dictionary and iterates through it using a for loop.

4. String formatting is used when displaying information so that the output is easier to read for the user.

These additions demonstrate meaningful use of data structures and improve the program’s ability to organize and display pet care recommendations.
"""

# Dictionary that stores care recommendations for each life stage
care_database = {
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

# Function that displays recommended activities for the dog's life stage
def display_stage_activities(stage):
    print(f"\nRecommended activities for a {stage}:")  # string formatting

    activities = care_database.get(stage, [])

    # iterate through the list of activities
    for activity in activities:
        print(f"- {activity}")

while True:
    choice = input("Would you like additional life stage advice? (yes/no): ").lower()

    if choice == "yes":
        age_input = int(input("Enter the dog's age again: "))

        stage = get_life_stage(age_input)
        tips = extra_care_tips(stage)

        print("Life Stage:", stage)
        print("Additional Advice:", tips)

        display_stage_activities(stage)   # <-- ADD THIS LINE HERE

    else:
        print("Thank you for using the Pet Care Assistant!")
        break
"""
This program provides advice on pet care based on a dog's age and activity level.
It has been expanded to include:
- Functions and loops 
- Data structures like dictionaries and lists 
- File handling to save and load data (Module 9)
"""
import json  # Used to save and load data from a file

FILE_NAME = "pet_data.json"  # File where pet data will be stored
def load_data():
    """
    Loads saved pet care data from a JSON file.
    If the file does not exist or is corrupted, returns a default database.
    """
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            print("Pet data loaded successfully.")
            return data

    except FileNotFoundError:
        print("No saved data found. Using default care recommendations.")
        return get_default_database()

    except json.JSONDecodeError:
        print("File error. Resetting to default data.")
        return get_default_database()


def save_data(care_database):
    """
    Saves the current care database to a JSON file.
    Prevents data loss between program runs.
    """
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(care_database, file, indent=4)
        print("Pet data saved.")

    except Exception as e:
        print("Error saving data:", e)


def get_default_database():
    """
    Returns the default pet care recommendations.
    This is used if no file exists yet.
    """
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

def get_life_stage(age):
    """Determines whether the dog is a puppy, adult, or senior."""
    if age < 2:
        return "puppy"
    elif 2 <= age <= 7:
        return "adult"
    else:
        return "senior"


def extra_care_tips(stage):
    """Provides additional care advice based on life stage."""
    if stage == "puppy":
        return "Puppies benefit from training and socialization."
    elif stage == "adult":
        return "Adult dogs need consistent exercise and a balanced diet."
    else:
        return "Senior dogs may need joint support and more frequent vet visits."


def display_stage_activities(stage, care_database):
    """
    Displays recommended activities for a given life stage.
    Uses a dictionary and loops (Modules 6–8).
    """
    print(f"\nRecommended activities for a {stage}:")

    activities = care_database.get(stage, [])

    for activity in activities:
        print(f"- {activity}")

# MAIN PROGRAM

print("Welcome to the Pet Care Assistant!")

# Load saved data 
care_database = load_data()

while True:
    # Ask user for input
    dog_age = int(input("\nEnter your dog's age in years: "))
    activity_level = input("Is your dog low, medium, or high energy? ").lower()

    # Basic advice logic (original milestone)
    if dog_age < 2 and activity_level == "high":
        print("Your dog is young and energetic. Make sure they get plenty of exercise!")
    elif 2 <= dog_age <= 7 and activity_level == "medium":
        print("Your dog is an adult with moderate energy. Regular walks are recommended.")
    else:
        print("Your dog may benefit from a calmer routine and regular vet checkups.")

    # Use functions
    stage = get_life_stage(dog_age)
    tips = extra_care_tips(stage)

    print("Life Stage:", stage)
    print("Additional Advice:", tips)

    # Display stored activities
    display_stage_activities(stage, care_database)

    # Save data (even if unchanged, ensures file exists)
    save_data(care_database)

    # Ask user if they want to continue
    choice = input("\nWould you like to check another dog? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you for using the Pet Care Assistant!")
        break

"""
Milestone 5: Object-Oriented Programming
"""
class Dog:
    """
    Represents a dog and provides care advice
    based on age and activity level using OOP.
    """
    def __init__(self, age, activity_level):
        self.age = age
        self.activity_level = activity_level

    def get_basic_advice(self):
        """Returns basic advice based on age and energy."""
        if self.age < 2 and self.activity_level == "high":
            return "Your dog is young and energetic. Make sure they get plenty of exercise!"
        elif 2 <= self.age <= 7 and self.activity_level == "medium":
            return "Your dog is an adult with moderate energy. Regular walks are recommended."
        else:
            return "Your dog may benefit from a calmer routine and regular vet checkups."

    def get_life_stage(self):
        """Determines the dog's life stage."""
        if self.age < 2:
            return "puppy"
        elif 2 <= self.age <= 7:
            return "adult"
        else:
            return "senior"

    def extra_care_tips(self):
        """Provides additional care advice based on life stage."""
        stage = self.get_life_stage()
        if stage == "puppy":
            return "Puppies benefit from training and socialization."
        elif stage == "adult":
            return "Adult dogs need consistent exercise and a balanced diet."
        else:
            return "Senior dogs may need joint support and more frequent vet visits."


# -------------------------------
# OOP Version User Loop
# -------------------------------
print("\n--- OOP Version: Check another dog using the Dog class ---")

while True:
    # Ask user for input
    dog_age = int(input("\nEnter your dog's age in years: "))
    activity_level = input("Is your dog low, medium, or high energy? ").lower()

    # Create a Dog object
    my_dog = Dog(dog_age, activity_level)

    # Display advice using object methods
    print("\n" + my_dog.get_basic_advice())
    stage = my_dog.get_life_stage()
    print("Life Stage:", stage)
    print("Additional Advice:", my_dog.extra_care_tips())

    # Display recommended activities using existing dictionary
    display_stage_activities(stage, care_database)

    # Save current care database (optional, keeps file consistent)
    save_data(care_database)

    # Ask user if they want to continue
    choice = input("\nWould you like to check another dog using the OOP version? (yes/no): ").lower()
    if choice != "yes":
        print("Thank you for using the Pet Care Assistant (OOP version)!")
        break


    