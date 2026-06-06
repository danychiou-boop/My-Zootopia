import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_html_template(file_path):
    """Loads the HTML template."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_animals_info(animals_data):
    """Creates a string containing all animal information."""
    output = ""

    for animal in animals_data:
        if "name" in animal:
            output += f"Name: {animal['name']}<br>\n"

        if (
            "characteristics" in animal
            and "diet" in animal["characteristics"]
        ):
            output += (
                f"Diet: {animal['characteristics']['diet']}<br>\n"
            )

        if "locations" in animal and len(animal["locations"]) > 0:
            output += f"Location: {animal['locations'][0]}<br>\n"

        if (
            "characteristics" in animal
            and "type" in animal["characteristics"]
        ):
            output += (
                f"Type: {animal['characteristics']['type']}<br>\n"
            )

        output += "<br>\n"

    return output


def main():
    animals_data = load_data("animals_data.json")

    html_template = load_html_template(
        "animals_template.html"
    )

    animals_info = generate_animals_info(
        animals_data
    )

    final_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_info
    )

    with open(
        "animals.html",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(final_html)

    print("animals.html generated successfully!")


if __name__ == "__main__":
    main()