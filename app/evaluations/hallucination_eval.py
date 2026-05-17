def check_hallucination(response):

    if "fake" in response:
        return True

    return False