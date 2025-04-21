import json


def load_data(file_path):
    """ Loads a JSON file
        Args:
            file_path (str): The path to the JSON file to be loaded.
        Returns:
            dict or list: The parsed JSON content, depending on the structure of the file.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animals_data():
    """
        Loads animal data from the default 'animals_data.json' file.
        Returns:
            list: A list of animal dictionaries loaded from the JSON file.
    """
    return load_data('animals_data.json')


def serialize_animal(animal):
    """
    Converts a single animal dictionary into an HTML list item string.

    Args:
        animal (dict): A dictionary containing information about an animal.
                       Expected keys include:
                         - 'name' (str)
                         - 'locations' (list of str, optional)
                         - 'characteristics' (dict) with keys like 'diet', 'type',
                           'skin_type', and 'top_speed'.

    Returns:
        str: A string of HTML markup representing the animal's information as a list item.
    """
    locations_list = animal.get('locations', [])
    locations = ", ".join(locations_list) if isinstance(locations_list, list) else 'Unknown'
    animal_type = animal['characteristics'].get('type', ' - ')
    animal_skin_type = animal['characteristics'].get('skin_type', ' - ')
    animal_top_speed = animal['characteristics'].get('top_speed', 'Unknown')
    return f"""
          <li class="cards__item">
              <div class="card__title">{animal['name']}</div>
              <div class="card__text">
                  <ul>
                      <li><strong>Diet:</strong> {animal['characteristics']['diet']}</li>
                      <li><strong>Location:</strong> {locations}</li>
                      <li><strong>Type:</strong> {animal_type}</li>
                      <li><strong>skin_type:</strong> {animal_skin_type}</li>
                      <li><strong>Top_speed:</strong> {animal_top_speed}</li>

                  </ul>    
              </div>
          </li>
      """


def filter_list(user_filter):
    """
    Filters a list of animals based on a given skin type and generates an HTML file.

    This function loads a dataset of animals and filters those whose skin type matches
    the provided `user_filter`. It converts the filtered animals into HTML entries,
    replaces a placeholder in an HTML template with these entries, and writes the
    final content to a file named 'animals.html'.

    Parameters:
        user_filter (str): The desired skin type to filter by (e.g., 'fur', 'scales', 'skin').
                           If set to 'all', no filtering is applied and all animals are included.

    """
    animal_entries = []
    animals_dataset = get_animals_data()
    for animal in animals_dataset:
        skin_type = animal.get('characteristics', {}).get('skin_type')
        if skin_type == user_filter or user_filter == "all":
            animal_entries.append(serialize_animal(animal))

    animals_html = "\n".join(animal_entries)

    with open('animals_template.html', 'r', encoding='utf-8') as f:
        html_template = f.read()

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(final_html)


def show_skin_type():
    """
    Retrieves a set of unique skin types from the animal dataset.
    This function accesses a dataset of animals, extracts the 'skin_type'
    value from each animal's 'characteristics' (if present), and returns a set of all
    unique skin types found.

    Returns:
        set: A set containing the unique skin types of all animals in the dataset.
    """
    animal_skin_type = set()
    animals_dataset = get_animals_data()
    for animal in animals_dataset:
        skin_type = animal.get('characteristics', {}).get('skin_type')
        if skin_type:
            animal_skin_type.add(skin_type)
    return animal_skin_type



