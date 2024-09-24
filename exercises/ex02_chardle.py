"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730812663"


def input_word() -> str:
    word = input("Enter a 5-character word: ")  # asks for a word
    if len(word) == 5:  # ensures the word is 5 characters only
        return word
    else:
        print("Error: Word must contain 5 Characters")
        exit()  # exits the code
        return word


def input_letter() -> str:
    letter = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character")
        exit()
        return letter


def contains_char(word: str, letter: str) -> None:
    index = 0
    count_char = 0
    print("Searching for " + letter + " in " + word)
    while index < len(word):
        if word[index] == letter:
            print(
                letter + " found at index " + str(index)
            )  # str used to convert ineteger into str
            count_char = count_char + 1
        index = (
            index + 1
        )  # increases the value so that the while loop is not stuck in an infinite loop
    if (
        count_char == 0
    ):  # checks the number of instances that count_char has been called
        print("No instances of " + letter + " found in " + word)
    elif count_char == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count_char) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(
        word=input_word(), letter=input_letter()
    )  # parameters written as other functions to assgn their values in them


if __name__ == "__main__":
    main()
