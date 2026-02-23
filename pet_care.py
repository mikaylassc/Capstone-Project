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
while True:
    choice = input("Would you like additional life stage advice? (yes/no): ").lower()
    
    if choice == "yes":
        age_input = int(input("Enter the dog's age again: "))
        
        stage = get_life_stage(age_input)   # calling function 1
        tips = extra_care_tips(stage)       # calling function 2
        
        print("Life Stage:", stage)
        print("Additional Advice:", tips)
        
    else:
        print("Thank you for using the Pet Care Assistant!")
        break