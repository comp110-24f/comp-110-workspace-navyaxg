"""Calculate number of tea bags, treats and the cost to host a tea party"""

__author__: str = "730812663"


def main_planner(guests: int) -> None:
    """main function"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # prints a concatenated sentence with a string and the return value of the tea_bag function converted to a string
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """to find number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """to find number of treats needed"""
    return int(
        tea_bags(people=people) * 1.5
    )  # it calls tea_bags function and multiplies the value with 1.5 and converts it to an integer


def cost(tea_count: int, treat_count: int) -> float:
    """to find the total cost for the tea party"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # asks for an input from the user for the main planner function and converts it to an integer value
