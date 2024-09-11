"""working with functions"""

__author__ = 730812663


def mimic(message: str) -> str:
    """mimicing function"""
    return message


def main() -> None:
    """prints the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
