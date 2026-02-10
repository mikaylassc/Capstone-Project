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