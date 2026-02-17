import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    output = ""
    output += '<li class="cards__item">'
    if animal_obj.get("name"):
        output += f"<div class='card__title'>{animal_obj.get("name")}</div>\n"
    output += "<p class='card__text'>"
    if animal_obj["characteristics"].get("diet"):
        output += f"<strong>Diet:</strong> {animal_obj["characteristics"].get("diet")}<br/>\n"
    if animal_obj.get("locations"):
        output += f"<strong>Location:</strong> {animal_obj.get("locations")[0]}<br/>\n"
    if animal_obj["characteristics"].get("type"):
        output += f"<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n\n"
    output += '</p>'
    output += '</li>'
    return output


def read_html(filename):
    html_file = open(filename, "r", encoding="utf-8")
    return html_file.read()


def write_to_html(filename, html_text):
    with open(filename, "w") as f:
      f.write(html_text)


def main():
    animals_data = load_data('animals_data.json')
    source_code = read_html("animals_template.html")

    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    source_code_with_animals = source_code.replace("__REPLACE_ANIMALS_INFO__", output)

    write_to_html("animals.html", source_code_with_animals)


if __name__ == "__main__":
    main()