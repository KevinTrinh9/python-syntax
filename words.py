def print_upper_words(words):
    """Print out each word on a separate line, but in all uppercase."""
    for word in words:
        print(word.upper())
def print_upper_words2(words):
    """Print out each word on a separate line, but in all uppercase, if it starts with the letter 'E' or 'e'."""
    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper())
def print_upper_words3(words, must_start_with):
    """Print out each word on a seprate line, but in all uppercase, if it starts with a given letter."""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break