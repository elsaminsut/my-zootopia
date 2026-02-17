import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

output = ""
for animal in animals_data:
    output += '<li class="cards__item">'
    if animal.get("name"):
        output += f"<div class='card__title'>{animal.get("name")}</div>\n"
    output += "<p class='card__text'>"
    if animal["characteristics"].get("diet"):
        output += f"<strong>Diet:</strong> {animal["characteristics"].get("diet")}<br/>\n"
    if animal.get("locations"):
        output += f"<strong>Location:</strong> {animal.get("locations")[0]}<br/>\n"
    if animal["characteristics"].get("type"):
        output += f"<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n\n"
    output += '</p>'
    output += '</li>'

html_file = open("animals_template.html", "r", encoding="utf-8")
source_code = html_file.read()
source_code_with_animals = source_code.replace("__REPLACE_ANIMALS_INFO__", output)
with open("animals.html", "w") as f:
  f.write(source_code_with_animals)
