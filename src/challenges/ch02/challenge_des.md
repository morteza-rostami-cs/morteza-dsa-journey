Got it ✅ Here’s a more advanced **Number Guessing Game Challenge** description for you (no code, just the rules):

---

## 🔢 Number Guessing Game – Advanced Challenge

### Rules & Mechanics:

1. **Hidden Number Range**

   - The program randomly selects a number between `1` and `1000`.
   - The range is not fixed — before each new game, the program randomly decides the upper bound (between `100` and `5000`) and reveals it to the player.

2. **Dynamic Difficulty Levels**

   - **Easy Mode**: Unlimited guesses, hints available.
   - **Medium Mode**: Maximum `log2(range)` guesses (rounded). No hints.
   - **Hard Mode**: Maximum `log2(range)` guesses, but the number changes slightly after every wrong guess (e.g., it increases or decreases by up to `±3`).

3. **Hints System (Easy Mode only)**

   - After 3 wrong guesses, the program gives a **range hint** (e.g., "The number is between 200 and 400").
   - After 5 wrong guesses, the program gives an **odd/even hint**.

4. **Scoring System**

   - Start with `1000 points`.
   - Lose `50 points` for each wrong guess.
   - Bonus `+200 points` if you win without using hints.
   - If you run out of guesses (or points reach 0), you lose.

5. **Leaderboard (optional)**

   - Store player name and score in a file (`leaderboard.txt`).
   - Display the top 5 scores at the end of each game.

---

### 🎯 Challenge Goal:

- Implement this game in Python with **clean code and modular design** (functions or classes).
- Support all difficulty levels.
- Track and update a persistent leaderboard across multiple game sessions.
- Make the game replayable without restarting the program.

---

Do you want me to push it **even harder** (e.g., multiplayer mode, AI opponent, or probability-based hint system)?
