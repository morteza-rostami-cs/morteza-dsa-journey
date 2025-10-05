"""
# let's code a number guessing game:

game_state = {
  "running": True # main menu loop
  "history: [] # a list of game_stats dict
}

def start_new_game():
  print("starting a new game")

  # create a new game -> with score and everything
  game_record = {
    "id": "someId",
    "score": 0,
    "hints": 0,
    "guesses": 0,
  }

def quit_game():
  print("exiting the game.\n")
  game_state['running'] = False

main_menu = {
  '1': ("new game", start_new_game), 
  'q': ("quit", quit_game),
}

def render_main_menu():
  print("=== main menu ===\n")

  # loop and render options
  for key, (name, _) in main_menu.items():
    print(f"{key}. {name}")

def handle_main_menu():

  # get the input 
  choice = input("> ")

  # input validation 
  if choice not in main_menu: 
    print("invalid input , please try again!")
    return 

  # call the action
  _, action = main_menu[choice]
  action()

def main_menu_loop():
  # main menu loop
  while game_state["running"]:
    # render the main menu
    render_main_menu()

    # handle the menu
    handle_main_menu()

def main():

  # handle main menu 
  main_menu_loop()

"""