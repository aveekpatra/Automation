#!/usr/bin/env python3

import random
import os
import shutil

def main():
    """Main function to display menu and handle user choices."""
    print("\n===== Casino Website Starter Tool =====\n")
    print("Select an option:")
    print("1. Configure Starter Template")
    print("2. Download Images")
    print("3. Error Checking")
    print("4. Clean Up")
    
    while True:
        try:
            choice = int(input("\nYour choice (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    if choice == 1:
        configure_template()
    elif choice == 2:
        download_images()
    elif choice == 3:
        error_checking()
    elif choice == 4:
        cleanup()

def configure_template():
    """Configure starter template by selecting a country and copying related files."""
    # List of countries from which we'll randomly select 7
    countries = [
        "Denmark", "France", "Portugal", "UK/IR"
    ]

    # Randomly select countries (up to 7, but limited by the actual number available)
    selected_countries = random.sample(countries, min(7, len(countries)))

    # Display countries with their indices
    print("Please select a country by entering its number:")
    for i, country in enumerate(selected_countries, 1):
        print(f"{i}. {country}")

    # Get user input
    while True:
        try:
            choice = int(input("\nYour choice (1-7): "))
            if 1 <= choice <= len(selected_countries):
                break
            else:
                print(f"Please enter a number between 1 and {len(selected_countries)}.")
        except ValueError:
            print("Please enter a valid number.")

    # Get the selected country
    selected_country = selected_countries[choice - 1]
    print(f"\nYou selected: {selected_country}")

    # Define source and destination paths for footer
    current_dir = os.path.dirname(os.path.abspath(__file__))
    footer_source_dir = os.path.join(current_dir, "folder-web", "MASTER", "footer", selected_country)
    footer_dest_dir = os.path.join(current_dir, "folder-web", "static", "footer")

    # Ensure the footer destination directory exists
    os.makedirs(footer_dest_dir, exist_ok=True)

    # Copy all files from footer source to footer destination
    if os.path.exists(footer_source_dir):
        print(f"\nCopying footer files from {footer_source_dir} to {footer_dest_dir}...")
        # First, remove existing files in the destination directory
        for item in os.listdir(footer_dest_dir):
            item_path = os.path.join(footer_dest_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        
        # Copy new files from the selected country
        for item in os.listdir(footer_source_dir):
            source_item = os.path.join(footer_source_dir, item)
            dest_item = os.path.join(footer_dest_dir, item)
            if os.path.isfile(source_item):
                shutil.copy2(source_item, dest_item)
                print(f"Copied footer file: {item}")
            elif os.path.isdir(source_item):
                shutil.copytree(source_item, dest_item)
                print(f"Copied footer directory: {item}")
        
        print("\nFooter files copied successfully!")
    else:
        print(f"\nError: Footer source directory {footer_source_dir} does not exist.")

    # Define source and destination paths for offers
    offers_source_dir = os.path.join(current_dir, "folder-web", "MASTER", "offers", selected_country)
    offers_dest_dir = os.path.join(current_dir, "folder-web", "static", "offers")

    # Ensure the offers destination directory exists
    os.makedirs(offers_dest_dir, exist_ok=True)

    # Copy all files from offers source to offers destination
    if os.path.exists(offers_source_dir):
        print(f"\nCopying offers files from {offers_source_dir} to {offers_dest_dir}...")
        # First, remove existing files in the destination directory
        for item in os.listdir(offers_dest_dir):
            item_path = os.path.join(offers_dest_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        
        # Copy new files from the selected country
        for item in os.listdir(offers_source_dir):
            source_item = os.path.join(offers_source_dir, item)
            dest_item = os.path.join(offers_dest_dir, item)
            if os.path.isfile(source_item):
                shutil.copy2(source_item, dest_item)
                print(f"Copied offers file: {item}")
            elif os.path.isdir(source_item):
                shutil.copytree(source_item, dest_item)
                print(f"Copied offers directory: {item}")
        
        print("\nOffers files copied successfully!")
    else:
        print(f"\nError: Offers source directory {offers_source_dir} does not exist.")

def download_images():
    """Placeholder function for downloading images."""
    print("Download images option selected. This feature is not yet implemented.")

def error_checking():
    """Placeholder function for error checking."""
    print("Error checking option selected. This feature is not yet implemented.")

def cleanup():
    """Placeholder function for cleanup."""
    print("Cleanup option selected. This feature is not yet implemented.")

if __name__ == "__main__":
    main() 