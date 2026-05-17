BLOCKED_WORDS = [
    "hack",
    "bypass"
]

def validate_input(query):

    for word in BLOCKED_WORDS:
        if word in query.lower():
            return False

    return True