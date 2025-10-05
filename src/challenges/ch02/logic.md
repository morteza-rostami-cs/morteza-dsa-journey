<!--

# advanced number guessing game:

#player:
  - name
  - score ->overall score throughout all the games
  - history of each game: (some stats)
    - number of guesses
    - hints used
    - final score

# main menu:
  - new game
    -- create a player -> basically enter your name
    -- start game
  - exit

# program starts -> loop
# generate a random number between 1 to 1000
# range is not fixed:
  - with each new game -> picks a new upper bound between -> 100 to 5000

# display the range to player

# dynamic difficulty level:

  - easy mode: 30 guesses , hints available
  - medium mode:
    -- so basically: you get enough chances -> as if you would solve this with binary search, meaning half the search space each time: 1000 / 2 = 500 and 500 / 20 = 250 and so on ....
    -- so: thinking smart is encouraged, but at the same time we give player enough choices to mathematically be able to solve the problem.
    -- you get log2(range) eg: if: between 1 to 100 -> log2(1000) = 9.97 or 10 guesses
    -- so: for a random number between 1 to 1000 -> you should be able to solve the problem -> in 10 guesses -> if you use smart binary search -> but if you pick randomly you probably can't.

  - hard mode:
    -- the same trick: we use log2() to determine the number of guesses player has
    -- but: each time you make a wrong guess -> secret number shifts by +-3 points
    -- although: secret_number has to stay within the range.

# hint system: -> easy mode only
  - after 3 wrong guesses -> program give a range hint -> eg: between 200 and 400
  - after 5 wrong guesses , the program gives an odd even hint.

# scoring system:
  - start with 1000 points
  - lose 50 points for each wrong guess
  - bonus +200 if you win without using hint
  - if you run out of guess or points reach 0 -> you lose

# leader board:
  - store player name and score in a file -> leaderboard.txt
  - display the top 5 scores at the end of each game

#================================

# player =>

def create_player():

  # get input for player name

  # validate: string, not empty, also max_length = 30

  # create a player dict
  player = {
    "name": name,
    "games_played": 0,
    "total_score": 0
  }

  return player

game_history = [] # list of dicts

def record_game(score:int, hints: int, guesses: int):
  # create a game record
  game_record = {
    id: uuid,
    score: score,
    hints_used: hints,
    guesses_used: guesses,
    won: won
  }

  game_history.append(game_record)

  # update player:
    player.score += score
    player.game_played += 1


 -->
