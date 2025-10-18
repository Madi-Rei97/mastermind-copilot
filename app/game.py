import random
# Wave 1

def generate_code():
    colors = ['R', 'O', 'Y', 'G', 'B', 'P']
    return random.sample(colors, 4)

def validate_guess(guess):
    allowed = {'R', 'O', 'Y', 'G', 'B', 'P'}
    if len(guess) != 4:
        return False
    for letter in guess:
        if str(letter).upper() not in allowed:
            return False
    return True    

def check_code_guessed(guess, code):
    """Return True if guess matches code exactly, False otherwise.

    Both guess and code are expected to be 4-element lists. Comparison is
    case-insensitive for robustness.
    """
    if not (isinstance(guess, list) and isinstance(code, list)):
        return False
    if len(guess) != 4 or len(code) != 4:
        return False

    # Compare element-wise in uppercase to be case-insensitive
    return [str(x).upper() for x in guess] == [str(x).upper() for x in code]

# Wave 2
# Add your Wave 2 functions here

# Wave 3
# Add your Wave 3 functions here
