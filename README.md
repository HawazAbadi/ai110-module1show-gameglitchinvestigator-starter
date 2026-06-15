# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. **Start the app** with `.venv/bin/python -m streamlit run app.py` and open `http://localhost:8501` in the browser.
2. **Pick a difficulty** in the sidebar (e.g. Normal), which sets the number range (1–100) and the number of attempts allowed.
3. **Make a guess** by typing a number into the input box and clicking **Submit Guess 🚀**. The game replies with a hint — **📉 Go LOWER!** if the guess was too high, or **📈 Go HIGHER!** if it was too low.
4. **Follow the hints** to narrow in on the secret. Open the **Developer Debug Info** expander to confirm the secret now stays the same on every submit (it no longer changes) and the hints point the correct direction.
5. **Win the game** by guessing the secret — the app shows 🎉 balloons, reveals the secret, and displays the final score.
6. **Click New Game 🔁** to reset the secret, score, attempts, and history, then play again at any difficulty.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ .venv/bin/python -m pytest tests/ -v
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.0.3, pluggy-1.6.0
collected 3 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 33%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 66%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [100%]

============================== 3 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
