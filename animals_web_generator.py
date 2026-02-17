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
    if animal_obj["taxonomy"].get("scientific_name"):
        output += f"<div class='card__subtitle'>{animal_obj["taxonomy"].get("scientific_name")}</div>\n"
    output += "<div class='card__text'>"
    output += "<ul>"
    if animal_obj["characteristics"].get("diet"):
        output += f"<li class='info__item'><strong>Diet:</strong> {animal_obj["characteristics"].get("diet")}</li>\n"
    if animal_obj.get("locations"):
        output += f"<li class='info__item'><strong>Location:</strong> {animal_obj.get("locations")[0]}</li>\n"
    if animal_obj["characteristics"].get("type"):
        output += f"<li class='info__item'><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n"
    if animal_obj["characteristics"].get("temperament"):
        output += f"<li class='info__item'><strong>Temperament:</strong> {animal_obj["characteristics"]["temperament"]}</li>\n"
    output += "</ul>"
    output += '</div>'
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