print("Welcome to the Interactive Personal Data Collector!")

name = input("Please enter your name: ")
age_str = input("Please enter your age: ")
height_str = input("Please enter your height in meters: ")
fav_num_str = input("Please enter your favourite number: ")

age = int(age_str)
height = float(height_str)
fav_num = int(fav_num_str)

birth_year = 2026 - age

print("\nThank you! Here is the information we collected:\n")

print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {fav_num} (Type: {type(fav_num)}, Memory Address: {id(fav_num)})")

print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")

print("\nThank you for using the Personal Data Collector. Goodbye!")