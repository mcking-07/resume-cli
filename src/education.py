from termcolor import colored
from src.utils import read_json

def display_education():
  json_path = './data/education.json'
  data = read_json(json_path)

  for index, education_info in enumerate(data['Education'], start = 1):
    print(f"\n{colored(f'Education #{index}', 'blue', attrs=['bold'])}")

    for key, value in education_info.items():
      print(f"{colored(key, 'yellow')}: {colored(value, 'green')}")
