from wordle_yx2910 import validate_guess, check_guess

def test_validate_guess():
    '''
    Test the validate _guess function with various inputs.
    
    TODO: Students should implementthis test function with:
    - Valid guesses (correct length, lowercase, alphabetic)
    - Invalid guesses (wrong length, uppercase, non-alphabetic)
    - Edge cases (empty string, None, non-string inputs)
    '''
    # TODO: Implement your test cases here
from wordle_yx2910 import validate_guess

def test_validate_guess_variants():
    """validate_guess: legal, illegal test"""

    # legal：length=5、all small letters, only alphabetic characters
    for w in ["crane", "olive", "spoon"]:
        assert validate_guess(w, 5) is True

    # illegal：length not right / capitalized / contains non-alphabetic / pure digits
    bad_inputs = [
        "cat",        # too short
        "bananas",    # too long
        "WORLD",      # all uppercase
        "Phone",      # capitalized
        "p4per",      # contains number
        "co-op",      # contains hyphen
        "12345",      # pure digits
    ]
    for w in bad_inputs:
        assert validate_guess(w, 5) is False

    # 边界：empty string / None / non-string inputs
    for w in ["", None, [], {}, 3.14]:
        assert validate_guess(w, 5) is False


from wordle_yx2910 import check_guess

def test_check_guess_variants():
    """check_guess: legal, illegal test"""

    # all green（perfectly matched）
    out = check_guess("crane", "crane")
    assert out == [
        ("c", "green"),
        ("r", "green"),
        ("a", "green"),
        ("n", "green"),
        ("e", "green"),
    ]

    # all gray（no letters matched）
    out = check_guess("crane", "tulip")  # crane has no overlap
    assert out == [
        ("t", "gray"),
        ("u", "gray"),
        ("l", "gray"),
        ("i", "gray"),
        ("p", "gray"),
    ]

    # mixed（green+yellow+grey)
    # secret = c r a n e
    # guess  = t r a c e  ->  t(gray), r(green), a(green), c(yellow), e(green)
    out = check_guess("crane", "trace")
    assert out == [
        ("t", "gray"),
        ("r", "green"),
        ("a", "green"),
        ("c", "yellow"),
        ("e", "green"),
    ]

    # if length mismatch -> return to empty set
    assert check_guess("crane", "cranes") == []
  


