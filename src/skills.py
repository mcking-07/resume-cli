from termcolor import colored
from src.utils import read_json

def display_skills():
  json_path = './data/skills.json'
  data = read_json(json_path)

  for category, skills in data['Skills'].items():
    print(f"\n{colored(category, 'blue', attrs=['bold'])}:")    
    if isinstance(skills, list):
      for skill in skills:
        print(f"- {colored(skill, 'green')}")
    elif isinstance(skills, dict):
      for sub_category, sub_skills in skills.items():
        print(f"- {colored(sub_category, 'magenta')}:")
        for sub_skill in sub_skills:
          print(f"  - {colored(sub_skill, 'green')}")
