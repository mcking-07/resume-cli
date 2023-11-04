import json

def read_json(file_path):
  with open(file_path) as file:
    content = json.load(file)
  return content

def write_json(file_path, content):
  try:
    with open(file_path, 'w') as file:
      json.dump(content, file, indent = 2)
  except Exception as err:
    print(f"Error writing JSON to file: {str(err)}")
