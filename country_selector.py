#!/usr/bin/env python3

import random

# List of countries from which we'll randomly select 7
countries = [
    "Japan", "Brazil", "Kenya", "Canada", "Norway", 
    "Australia", "India", "Mexico", "Egypt", 
    "Germany", "Thailand", "South Korea", "Italy"
]

# Randomly select 7 countries
selected_countries = random.sample(countries, 7)

# Display countries with their indices
print("Please select a country by entering its number:")
for i, country in enumerate(selected_countries, 1):
    print(f"{i}. {country}")

# Get user input
while True:
    try:
        choice = int(input("\nYour choice (1-7): "))
        if 1 <= choice <= 7:
            break
        else:
            print("Please enter a number between 1 and 7.")
    except ValueError:
        print("Please enter a valid number.")

# Print the selected country
print(f"\nYou selected: {selected_countries[choice - 1]}") 