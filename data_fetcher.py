import os
import requests
from dotenv import load_dotenv
from colorama import Fore

def fetch_data(animal_name):
    """
    Fetches animal data from an external API by animal name.

    Sends a request to the API Ninjas animal endpoint with the given animal name
    and retrieves matching animal data. If the request is successful, returns
    a list of animal dictionaries; otherwise, prints an error message.

    Args:
        animal_name (str): Name of the animal to search for.

    Returns:
        list: A list of animals, where each animal is a dictionary with keys like
            'name', 'taxonomy', 'locations', and 'characteristics'.
    """
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    try:
        response = requests.get(url, headers={"X-Api-Key": API_KEY})
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            print(f"{Fore.LIGHTRED_EX}Error: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}Error: Something went wrong with the request. Exception: {e}")
        return []
