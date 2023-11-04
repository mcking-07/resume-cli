from termcolor import colored
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from src.about import display_about
from src.experience import display_experience
from src.education import display_education
from src.skills import display_skills
from src.projects import display_projects
from src.contact import display_contact
from src.exit import display_exit

def display_menu():
  options = {
    "about": display_about,
    "experience": display_experience,
    "education": display_education,
    "skills": display_skills,
    "projects": display_projects,
    "contact": display_contact,
    "exit": display_exit,
  }

  completer = WordCompleter(options.keys(), ignore_case = True)
  session = PromptSession(completer = completer)

  while True:
    print(f"\n{colored(f':::Options:::', 'blue', attrs=['bold'])}\n")
    for option in options:
      print(f"- {colored(f'{option.capitalize()}', 'magenta')}")

    choice = session.prompt(f"\nWhat would you like to know?: ").lower()
    action = options.get(choice, None)

    if callable(action):
      print("\033c")
      action()
      input("\nPress [ENTER] to return to the main menu.")
      print("\033c")
    else:
      print("\033c")
      print(f"\n{colored(f'[Error]', 'red', attrs=['bold'])} Please enter a valid option.")
