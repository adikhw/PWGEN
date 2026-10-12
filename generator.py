import secrets, string

MIN_LENGTH = 8
MAX_LENGTH = 64
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"

# Build pools function
def build_pools(use_lower, use_upper, use_digits, use_symbols):
    pools = []

    if use_lower: pools.append(string.ascii_lowercase)
    if use_upper: pools.append(string.ascii_uppercase)
    if use_digits: pools.append(string.digits)
    if use_symbols: pools.append(SYMBOLS)

    return pools

# Generate password function
def generate_password(length, use_lower, use_upper, use_digits, use_symbols):

    if type(length) is not int:
        raise ValueError("Length must be an integer")

    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError("Length must be between 8 and 64")

    pools = build_pools(use_lower, use_upper, use_digits, use_symbols)
    if not pools:
        raise ValueError("Select at least one character type")

    chars = []
    for pool in pools:
        chars.append(secrets.choice(pool))

    all_chars = "".join(pools)
    while len(chars) < length:
        chars.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)

