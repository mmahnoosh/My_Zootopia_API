from colorama import Fore

import animal_funktions
import data_fetcher


def get_user_input():
    """
    Prompts the user to enter the name of an animal.

    Displays a formatted header using the `colorama` library for better readability,
    then waits for user input. The entered string is returned to the caller.

    Returns:
        str: The name of the animal entered by the user.
    """

    print(Fore.LIGHTYELLOW_EX + "=================================== Animals"
                                " ==========================================")

    user_input = input("Enter the name of an animal: ")
    return user_input


def main():
    """
    Coordinates the generation of the final HTML page based on user input.

    Workflow:
        - Prompts the user to enter the name of an animal.
        - Loads corresponding animal data from a JSON file.
        - Generates an HTML block for the animal.
        - Replaces a placeholder in the HTML template with the generated content.
        - Writes the final HTML to an output file.
    """

    user_input = get_user_input()
    data = data_fetcher.fetch_data(user_input)
    output = animal_funktions.generate_animal_html(data, user_input)
    new_data = animal_funktions.replace_html(output)
    animal_funktions.write_html_file(new_data)


if __name__ == "__main__":
    main()
