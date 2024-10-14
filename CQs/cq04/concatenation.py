"""concatenation of words"""

__author__: str = "730812663"


def concat(word1: str, word2: str) -> str:
    concat_words = word1 + word2
    return concat_words


word1 = "happy"
word2 = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
