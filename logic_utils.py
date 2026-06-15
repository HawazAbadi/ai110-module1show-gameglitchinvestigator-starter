def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Hard":
        return 1, 200
    # Normal is the default.
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome.

    Returns one of: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def hint_for_outcome(outcome: str):
    """Return the player-facing hint message for an outcome."""
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        # Guess was too high, so the player should go LOWER.
        return "📉 Go LOWER!"
    if outcome == "Too Low":
        # Guess was too low, so the player should go HIGHER.
        return "📈 Go HIGHER!"
    return ""


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    # Any wrong guess costs the same, regardless of which way it was off.
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
