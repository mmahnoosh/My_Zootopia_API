def serialize_animal(animal):
    """
    Serializes an animal dictionary into an HTML list item.

    Args:
        animal (dict): Contains 'name', optional 'locations', and 'characteristics' like 'diet', 'type', 'skin_type', and 'top_speed'.

    Returns:
        str: HTML string representing the animal.
    """
    locations_list = animal.get('locations', [])
    locations = ", ".join(locations_list) if isinstance(locations_list, list) else 'Unknown'
    characteristics = animal.get('characteristics', {})
    return f"""
          <li class="cards__item">
              <div class="card__title">{animal['name']}</div>
              <div class="card__text">
                  <ul>
                      <li><strong>Diet:</strong> {characteristics.get('diet', ' - ')}</li>
                      <li><strong>Location:</strong> {locations}</li>
                      <li><strong>Type:</strong> {characteristics.get('type', ' - ')}</li>
                      <li><strong>Skin type:</strong> {characteristics.get('skin_type', ' - ')}</li>
                      <li><strong>Top speed:</strong> {characteristics.get('top_speed', 'Unknown')}</li>

                  </ul>    
              </div>
          </li>
      """


def load_html_template(template_path='animals_template.html'):
    """
    Loads the contents of an HTML template file.

    Reads the specified HTML file (default: 'animals_template.html') using UTF-8 encoding
    and returns its content as a string for further processing.

    Args:
        template_path (str, optional): Path to the HTML template file. Defaults to 'animals_template.html'.

    Returns:
        str: The content of the HTML template.
    """

    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_html_file(content, output_path='animals.html'):
    """
    Writes HTML content to a file.

    Saves the given content string into a file using UTF-8 encoding.
    By default, it writes to 'animals.html', but a different output path can be provided.

    Args:
        content (str): The HTML content to write.
        output_path (str, optional): Destination file path. Defaults to 'animals.html'.

    Returns:
        None
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


def generate_animal_html(data, user_input):
    """
    Generates HTML content for a list of animals.

    Iterates over the provided animal data and serializes each animal into an HTML block.
    If no animals are found, returns a message indicating no results for the user's input.

    Args:
        data (list): A list of animal dictionaries.
        user_input (str): The user's search input, used for the 'no animals found' message.

    Returns:
        str: Generated HTML content as a string.
    """
    output = ""
    for animal in data:
        output += serialize_animal(animal)

    if output == "":
        return (f'<div class="card__title">No animals found for '
                f'your search of "{user_input}".</div>')
    return output


def create_animal_html(data, user_input):
    """
    Generates HTML content from a list of animal data.

    Iterates over the provided data, serializes each animal into HTML,
    and returns the complete HTML content. If no animals are found,
    a 'no animals found' message is returned instead.

    Args:
        data (list of dict): Animal data to generate the website content.
        user_input (str): The user's input, used in the 'no animals found' message.

    Returns:
        str: Generated HTML content as a string.
    """
    output = ""

    for animal_obj in data:
        output += serialize_animal(animal_obj)

    if output == "":
        return (f'<div class="card__title">No animals found for '
                f'your search of "{user_input}".</div>')
    return output


def replace_html(animal_data):
    """
    Replaces a placeholder in an HTML template with generated animal data.

    Opens the 'animals_template.html' file, replaces the '__REPLACE_ANIMALS_INFO__'
    placeholder with the provided animal HTML content, and returns the complete HTML code.

    Args:
        animal_data (str): Generated animal HTML content.

    Returns:
        str: Final HTML page content as a string.
    """
    with open("animals_template.html", "r") as f:
        data = f.read()

    new_data = data.replace("__REPLACE_ANIMALS_INFO__", animal_data)
    return new_data
