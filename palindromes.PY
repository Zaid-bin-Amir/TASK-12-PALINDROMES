import re


def normalize(text):
    """Lowercase the text and keep only letters and digits."""
    return re.sub(r"[^a-z0-9]", "", text.lower())


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards."""
    cleaned = normalize(text)
    return cleaned == cleaned[::-1]


def run_examples():
    valid = [
        "madam",
        "Racecar",
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "No lemon, no melon",
    ]
    invalid = [
        "hello",
        "Python Programming",
        "This is not a palindrome",
        "OpenAI",
    ]

    print("=== Valid palindromes ===")
    for s in valid:
        print(f"{s!r:45} -> {is_palindrome(s)}")

    print("\n=== Invalid palindromes ===")
    for s in invalid:
        print(f"{s!r:45} -> {is_palindrome(s)}")


def main():
    run_examples()
    print("\n=== Try your own (type 'quit' to exit) ===")
    while True:
        user_input = input("Enter a word or sentence: ")
        if user_input.strip().lower() == "quit":
            print("Goodbye!")
            break
        if not normalize(user_input):
            print("Please enter at least one letter or number.\n")
            continue
        if is_palindrome(user_input):
            print(f"✅ '{user_input}' is a palindrome!\n")
        else:
            print(f"❌ '{user_input}' is not a palindrome.\n")


if __name__ == "__main__":
    main()