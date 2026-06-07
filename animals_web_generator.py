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
    """Creates styled HTML cards for all animals."""
    output = ""

    for animal in animals_data:
        output += '<li class="cards__item">\n'

        if "name" in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'

        output += '  <p class="card__text">\n'

        characteristics = animal.get("characteristics", {})

        if "diet" in characteristics:
            output += (
                f"    <strong>Diet:</strong> "
                f"{characteristics['diet']}<br/>\n"
            )

        if "locations" in animal and len(animal["locations"]) > 0:
            output += (
                f"    <strong>Location:</strong> "
                f"{animal['locations'][0]}<br/>\n"
            )

        if "type" in characteristics:
            output += (
                f"    <strong>Type:</strong> "
                f"{characteristics['type']}<br/>\n"
            )

        output += "  </p>\n"
        output += "</li>\n"

    return output


def main():
    animals_data = load_data("animals_data.json")
    html_template = load_html_template("animals_template.html")

    animals_info = generate_animals_info(animals_data)

    final_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_info
    )

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("animals.html generated successfully!")


if __name__ == "__main__":
    main()