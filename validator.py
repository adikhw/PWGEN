import string

def check_length(password):
    if type(password) is not str:
        raise ValueError("Password must be a string")
    if password == "":
        raise ValueError("Password cannot be empty")
    
    return len(password)

def detect_char_types(password):
    types = set()

    for char in password:
        if char in string.ascii_lowercase: 
            types.add("lower")
        elif char in string.ascii_uppercase:
            types.add("upper")
        elif char in string.digits:
            types.add("digit")
        elif char in string.punctuation:
            types.add("symbol")

    return types

def analyze_basic(password):
    length = check_length(password)
    types = detect_char_types(password)
    return {"length", length, "types:", types}

