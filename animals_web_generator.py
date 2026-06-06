import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main():
    animals_data = load_data("animals_data.json")

    for animal in animals_data:
        if "name" in animal:
            print(f"Name: {animal['name']}")

        if "characteristics" in animal:
            characteristics = animal["characteristics"]

            if "diet" in characteristics:
                print(f"Diet: {characteristics['diet']}")

            if "type" in characteristics:
                print(f"Type: {characteristics['type']}")

        if "locations" in animal and len(animal["locations"]) > 0:
            print(f"Location: {animal['locations'][0]}")

        print()


if __name__ == "__main__":
    main()