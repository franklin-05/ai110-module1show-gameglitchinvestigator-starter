# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
While playing the game, I noticed that the hint system is completely broken and untrustworthy
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The input takes numbers beyond the range that is given 
numbers can be negative as well and it will no mark any errors 
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Location
|-------|-------------------|-----------------|------------------------|
|23| | | | Go higher.        Go lower           none.                   App.py
|0 | | | | cant input this int go lower      none                    App.py 'parse.guess()'
|677 ||||| cant in put this  go lower.      none                     app.py
-4.     | should not take input|go lower.   none.                    app.py
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used gemini and claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The suggestions to fix the logic_utils file were correct.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
 Claude decided to create an extra file when i was trying to run the test_game_logic file i did not have hte proper command but claude create an extra file that was totally unnecessary after questioning claude why he created that file and that i hsould be able to run the test without the file claude finally deleted the file. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
 Although the test files passed all of the given test i went ahead and decided to test the game by giving it erronous input it turned out the logic was correct but the bug was not fixed
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
 Ai helped understand why the tests was passing but the bug was not fixed, i asked ai why was the bug not fixed if the code was modified and then we got to the point of friction which in this case was the logic 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
in Streamlit, every time you click a button or interact with the app, the entire Python script reruns from top to bottom. Because of this, normal variables would get reset every time. st.session_state acts like a save file for the app, letting us securely store things like the secret number, current score, and attempt counts so they don't get wiped out during a rerun
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
