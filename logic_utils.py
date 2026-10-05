def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
  
    if difficulty == "Easy":
        return (1, 50)
    elif difficulty == "Normal":
        return (1, 100)
    elif difficulty == "Hard":
        return (1, 200)
    return (1, 100)


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """

    # Replaced NotImplementedError with try/except parsing to catch invalid inputs safely.
    try:
        guess_int = int(raw)
        return True, guess_int, None
    except ValueError:
        return False, None, "Please enter a valid integer."
def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome string.

    outcome examples: "Win", "Too High", "Too Low"
    """

    # Fixed the hint logic so it correctly tells players when they are too high or too low.
    if guess == secret:
        return "Win"
    elif guess > secret:
        return "Too High"
    else:
        return "Too Low"

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""

    # Calculates score updates depending on whether the user won or needs another hint.
    if outcome == "Win":
        return current_score + 10
    return max(0, current_score - 5)