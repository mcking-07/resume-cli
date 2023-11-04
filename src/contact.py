from termcolor import colored
from src.utils import read_json

def display_contact():
  json_path = './data/contact.json'
  data = read_json(json_path)

  print(f"\n{colored('Contact Me At', 'blue', attrs=['bold'])}")

  for key, value in data['Contact'].items():
    if isinstance(value, list):
      print(f"{colored(key, 'yellow')}:")
      for item in value:
        print(f"- {colored(item, 'green')}")
    else:
      print(f"{colored(key, 'yellow')}: {colored(value, 'green')}")
