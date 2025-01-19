# Step 1: Import Necessary Libraries
# Import the following modules:
# csv to read and process the CSV file.
# requests to make HTTP requests for checking website statuses.
# HTTPStatus from the http module to interpret status codes.
# UserAgent from the fake_useragent library to generate user-agent strings.

import csv
import requests
from http import HTTPStatus
from fake_useragent import UserAgent

# Step 2: Define the get_websites Function
# Purpose: To load website URLs from a CSV file and return them as a list of strings.
# Accept the CSV file path (csv_path) as a parameter.
# Initialize an empty list (websites).
# Open the CSV file in read mode.
# Use the csv.reader to iterate through each row in the file:
# Check if the URL in row[1] starts with https://.
# If not, prepend https:// to the URL.
# Append the properly formatted URL to the websites list.
# Return the list of websites.

def get_websites(csv_path: str) -> list[str]:

    websites: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])

    return websites

# Step 3: Define the get_user_agent Function
# Purpose: To generate a random user-agent string for the HTTP requests.
# Create an instance of the UserAgent class.
# Return a chrome user-agent string from the UserAgent instance.

def get_user_agent() -> str:

    ua = UserAgent()
    return ua.chrome

# Step 4: Define the get_status_description Function
# Purpose: To convert HTTP status codes into a human-readable description.
# Accept a status code (status_code) as a parameter.
# Loop through all values in the HTTPStatus enumeration:
# If the status code matches the current enumeration value, create a descriptive string including:
# The status code.
# The status name.
# A brief description of the status.
# Return the description.
# If no match is found, return a default string indicating an unknown status code.

def get_status_description(status_code: int) -> str:
    """Uses the status code to return a readable description"""

    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description

    return '(???) Unknown status code...'

# Step 5: Define the check_website Function
# Purpose: To fetch the HTTP status code for a website and print the result.
# Accept website (URL string) and user_agent as parameters.
# Use requests.get to make an HTTP request to the website:
# Set the User-Agent header in the request using the provided user_agent.
# Retrieve the HTTP status code from the response.
# Use the get_status_description function to get the readable status description.
# Print the website URL and the status description.
# Handle exceptions with a try-except block and print an error message if the request fails.

def check_website(website: str, user_agent: str):
    """Gets that status code for a website and prints the result"""
    try:
        code: int = requests.get(website, headers={'User-Agent': user_agent}).status_code
        print(website, get_status_description(code))
    except Exception:
        print(f'**Could not get information for website: "{website}"')

# Step 6: Define the main Function
# Purpose: To serve as the entry point for the script.
# Call the get_websites function, passing the file path of the CSV file containing website URLs. Store the returned list in sites.
# Call the get_user_agent function to generate a user-agent string. Store it in user_agent.
# Loop through the sites list and:
# Call the check_website function for each URL, passing the URL and the user-agent string.

def main():
    sites: list[str] = get_websites('websites.csv')
    user_agent: str = get_user_agent()

    for i, site in enumerate(sites):
        check_website(site, user_agent)

# Step 7: Set the Script Entry Point
# Use the if __name__ == '__main__': construct to ensure the script runs only when executed directly.
# Call the main function to execute the program.

if __name__ == '__main__':
    main()