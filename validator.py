import re

COMMON_WORDS: set[str] = {
    "password",
    "admin",
    "welcome",
    "qwerty",
    "letmein",
    "login",
    "user",
    "guest",
    "hello",
    "secret",
}

LOWER_RE = re.compile(r"[a-z]")
UPPER_RE = re.compile(r"[A-Z]")
DIGIT_RE = re.compile(r"[0-9]")
SYMBOL_RE = re.compile(r"[^a-zA-Z0-9]")


def _require_str(password):
    """Ensure the password is a string."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string")


def _require_valid_n(n):
    """Ensure n is an integer greater than or equal to 2."""
    if type(n) is not int or n < 2:
        raise ValueError("n must be an integer >= 2")


def check_length(password):
    """Validate the password and return its length."""
    _require_str(password)
    if password == "":
        raise ValueError("Password cannot be empty")

    return len(password)


def detect_char_types(password):
    """Detect the character types present in the password."""
    _require_str(password)
    types = set()

    for char in password:
        if "a" <= char <= "z":
            types.add("lower")
        elif "A" <= char <= "Z":
            types.add("upper")
        elif "0" <= char <= "9":
            types.add("digit")
        else:
            types.add("symbol")

    return types


def analyze_basic(password):
    """Return the password length and its character types."""
    length = check_length(password)
    types = detect_char_types(password)
    return {"length": length, "types": types}


def detect_char_types_regex(password):
    """Detect password character types using regular expressions."""
    _require_str(password)
    types = set()

    if LOWER_RE.search(password):
        types.add("lower")
    if UPPER_RE.search(password):
        types.add("upper")
    if DIGIT_RE.search(password):
        types.add("digit")
    if SYMBOL_RE.search(password):
        types.add("symbol")

    return types


def has_repeat(password, n=3):
    """Check whether the password contains n consecutive repeated characters."""
    _require_str(password)
    _require_valid_n(n)

    pattern = rf"(.)\1{{{n - 1}}}"
    return re.search(pattern, password, re.DOTALL) is not None


def has_sequence(password, n=4):
    """Check for ascending or descending ASCII alphanumeric sequences."""
    _require_str(password)
    _require_valid_n(n)

    password = password.lower()

    for i in range(len(password) - n + 1):
        piece = password[i:i + n]

        if not (piece.isascii() and piece.isalnum()):
            continue

        ascending = all(
            ord(piece[j]) == ord(piece[j - 1]) + 1
            for j in range(1, n)
        )
        descending = all(
            ord(piece[j]) == ord(piece[j - 1]) - 1
            for j in range(1, n)
        )

        if ascending or descending:
            return True

    return False


def has_common_words(password):
    """Check whether the password contains any common weak words."""
    _require_str(password)

    password = password.lower()
    return any(word in password for word in COMMON_WORDS)


def assess_password(password):
    """Assess password strength and return its level and reasons."""
    info = analyze_basic(password)
    length = info["length"]
    types = info["types"]

    weak_reasons = []

    if length < 8:
        weak_reasons.append("Password is too short (minimum 8 characters)")
    if len(types) == 1:
        weak_reasons.append("Password uses only 1 type of character")
    if has_repeat(password):
        weak_reasons.append("Password has repeating characters")
    if has_sequence(password):
        weak_reasons.append("Password has a sequence (e.g. 1234 or abcd)")
    if has_common_words(password):
        weak_reasons.append("Password contains common words")

    if weak_reasons:
        level = "Weak"
        reasons = weak_reasons

    elif length >= 12 and len(types) >= 3:
        level = "Strong"
        reasons = [
            "Sufficient length (at least 12 characters)",
            "Uses at least 3 character types",
        ]

    else:
        level = "Medium"
        reasons = []

        if length < 12:
            reasons.append("Fewer than 12 characters")

        if len(types) < 3:
            reasons.append("Fewer than 3 character types")

    return {"level": level, "reasons": reasons}