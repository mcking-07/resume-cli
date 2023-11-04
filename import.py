from src.utils import read_json, write_json

json_path = './data/resume.json'
data = read_json(json_path)

modules = ["About", "Experience", "Education", "Skills", "Projects", "Contact"]

for module in modules:
  if module in data:
    output_file_path = f"./data/{module.lower()}.json"
    write_json(output_file_path, { module: data[module] })
