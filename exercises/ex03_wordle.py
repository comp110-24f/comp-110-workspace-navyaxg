"""Wordle"""

__author__: str = "730812663"

word = ""


def input_guess(secret_word_len: int) -> str:
    global word  # word made global to be used in main function
    word = input(f"Enter a {secret_word_len} character word: ")
    while len(word) != secret_word_len:
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """find characters in the input word"""
    assert len(char_guess) == 1
    index = 0
    check_chars = False
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            check_chars = (
                True  # changes to true when the character is found in the input
            )
        index = index + 1
    return check_chars


def emojified(user_guess: str, secret_word: str) -> str:
    """compare two strings and print boxes for different scenarios"""
    assert len(user_guess) == len(
        secret_word
    )  # assert used to esnure user word length is same as secret word length
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    index = 0
    boxes = ""
    while index < len(user_guess):
        if user_guess[index] == secret_word[index]:
            boxes = boxes + green_box  # changes box value by adding green box
        elif contains_char(secret_word, user_guess[index]):
            boxes = boxes + yellow_box
        else:
            boxes = boxes + white_box
        index = index + 1
    return boxes


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    characters = len(secret)
    while turn <= 6 and word != secret:
        print(f"=== Turn {turn}/6 ===")
        print(
            emojified(input_guess(characters), secret)
        )  # input_guess called here to ask for user input every turn
        turn = turn + 1
    if secret == word:
        print(f"You won in {turn-1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
