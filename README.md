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

- On this game you have to guess an number between 1 and 100 and you have a couple of attempts depeding on the level you are in.
- I found a couple of bugs, among them was the hints were not taking place correctly, the input was not working accordingly as well as the logic behind the data type that the game was taking 
- I have fixed the bugs mentioned in the reflection 
## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Open the game in your browser using Streamlit, and check your difficulty setting in the sidebar.
2. Type in a valid whole number. Make sure you aren't entering text, decimals, or numbers lower than 1 (like 0 or negative values).
3. Click submit and watch the hints. They will correctly tell you whether to go higher or lower.
4. Keep making guesses based on those hints until you find the secret number or run out of attempts.
5. If you want to check what's happening behind the scenes, open the Developer Debug Info section to view the hidden secret number and your guess history.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
