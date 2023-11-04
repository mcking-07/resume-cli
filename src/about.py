from termcolor import colored
from src.utils import read_json

def display_about():
  json_path = './data/about.json'
  data = read_json(json_path)

  print(f"\n{colored('About Me', 'blue', attrs=['bold'])}")

  for item in data['About']:
    print(f"- {colored(item, 'green')}")
