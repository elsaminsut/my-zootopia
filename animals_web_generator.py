import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    # print(f"Name: {animal.get("name")}")
    # print(f"Diet: {animal["characteristics"].get("diet")}")
    # print(f"Location: {animal.get("locations")[0]}")
    if animal.get("name"):
        print(f"Name: {animal.get("name")}")
    if animal["characteristics"].get("diet"):
        print(f"Diet: {animal["characteristics"].get("diet")}")
    if animal.get("locations"):
        print(f"Location: {animal.get("locations")[0]}")
    if animal["characteristics"].get("type"):
        print(f"Type: {animal["characteristics"]["type"]}")
    print()
