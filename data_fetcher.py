from dotenv import load_dotenv


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    load_dotenv()
    API_KEY = "yY8qBpaiLxW3dHO+YUz11w==F6MLY74mPJbh1T91"
    animal_name = input("Please enter an animal: ")
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    data = fetch_data(animal_name)
    return data
