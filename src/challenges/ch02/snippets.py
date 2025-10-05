
"""
# advanced: number guessing game in python:

# difficulty modes
# scoring system
# leaderboard at the end

"""

main_menu_options = {
  'new_game': "new_game",
  'exit': "exit",
}

def main():
  """ entry point of the program  """
  # game loop 
  while True:

    # render main menu
    print("=== Main menu ===\n")
    print(list(main_menu_options))
    print('new_game' in main_menu_options)

    break

if __name__ == "__main__":
  main()



"""
# number guessing game in python:

# advanced
# difficulty 
# scoring system
# leaderboard

"""

main_menu_options = {
  "new_game": "new_game",
  # add more options ----
  "exit": "exit",
}

def main():
  """ entry point of our game """
  
  # main game loop 
  while True:
    
    # render main menu
    print("==== main menu ====\n")
    for index, (key, value) in enumerate(main_menu_options.items()):
      print(f"{index}. {value}")

    break

if __name__ == "__main__":
  main()

# this is just for figuring things out and this is nice to know and you should understand this , if you don't understand this then we have a problem with each other!! so god helps us in this pass!

game_state = {"running": True}

def quit_game():
    print("quit the game!")
    game_state["running"] = False

def main():
    while game_state["running"]:
        render_main_menu()
        handle_main_menu()

"""
# number guessing game in python:
"""

def start_new_game():
  print("starting a new game!")

def quit_game():
  print("quit the game!")

# dict for main menu options
main_menu = {
  "1": ("New Game", start_new_game),
  'q': ("Quit", quit_game)
}

def render_main_menu():
  print("=== Main Menu ===\n")
  # new game and exit -> more
  for key, (name, _) in main_menu.items():
    print(f"{key}. {name}") # 1. new game

def handle_main_menu():
  """ get user input and handle choice """
  choice = input(">")

  # validate input -> 1 , q
  if choice not in main_menu: # dic keys
    print("Invalid option, try again!\n")
    return 
  
  #choice is valid
  # ("New Game", start_new_game)
  _, action = main_menu[choice]
  # call the action
  action()
  
def main():
  """ entry point of the program """
  
  # game loop 
  while True:
    # render our main menu
    render_main_menu()

    # input and handle choice
    handle_main_menu()

    break

if __name__ == "__main__":
  main()

#====================