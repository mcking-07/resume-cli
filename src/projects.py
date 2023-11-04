from termcolor import colored
from src.utils import read_json

def display_projects():
  json_path = './data/projects.json'
  data = read_json(json_path)

  for index, project in enumerate(data['Projects'], start = 1):
    print(f"\n{colored(f'Project #{index}', 'blue', attrs=['bold'])}")

    for key, value in project.items():
      if isinstance(value, list):
        print(f"{colored(key, 'yellow')}:")
        for item in value:
          print(f"- {colored(item, 'green')}")
      else:
        print(f"{colored(key, 'yellow')}: {colored(value, 'magenta')}")
  return
