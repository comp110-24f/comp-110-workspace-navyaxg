"""practicing while loops to iterate over a string"""

__author__: str = "730812663"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count = count + 1
        index = index + 1
    return count


if __name__ == "__main__":
    print(
        num_instances(
            phrase=input("Please enter a phrase: "),
            search_char=input("Please enter a character: "),
        )
    )
