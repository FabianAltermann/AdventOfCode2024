from itertools import pairwise


def string2list(s: str) -> list:
    return list(map(int, s.split(" ")))


def calc_difference(report: list) -> list:
    return [y - x for (x, y) in pairwise(report)]


def check_safe(difference: list) -> bool:
    if (
        all(map(lambda x: x < 0, difference)) or all(map(lambda x: x > 0, difference))
    ) and all(map(lambda x: x >= 1 and x <= 3, map(abs, difference))):
        return True
    else:
        return False


def main():
    safe = 0
    with open("./data.txt", "r") as file:
        for line in file:
            report = string2list(line)
            difference = calc_difference(report)
            if check_safe(difference):
                safe += 1

    print(safe)


if __name__ == "__main__":
    main()
