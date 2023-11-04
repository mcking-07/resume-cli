from termcolor import colored
from src.utils import read_json

highlighted_keys = ['position', 'company']

def display_experience():
  json_path = './data/experience.json'
  data = read_json(json_path)

  for index, experience in enumerate(data['Experiences'], start = 1):
    print(f"\n{colored(f'Experience #{index}', 'blue', attrs=['bold'])}")

    for key, value in experience.items():
      if isinstance(value, list):
        print(f"{colored(key, 'yellow')}:")
        for item in value:
          print(f"- {colored(item, 'green')}")
      elif key.lower() in highlighted_keys:
        print(f"{colored(key, 'yellow')}: {colored(value, 'magenta')}")
      else:
        print(f"{colored(key, 'yellow')}: {colored(value, 'green')}")
