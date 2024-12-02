from itertools import pairwise


def string2list(s: str) -> list:
    return list(map(int, s.split(" ")))


def calc_difference(l: list) -> list:
    return [y - x for (x, y) in pairwise(l)]


def check_safe(difference: list) -> bool:
    if (
        all(map(lambda x: x < 0, difference)) or all(map(lambda x: x > 0, difference))
    ) and all(map(lambda x: x >= 1 and x <= 3, map(abs, difference))):
        return True
    else:
        return False


safe = 0
with open("./data.txt", "r") as file:
    for line in file:
        report = string2list(line)
        difference = calc_difference(report)
        if check_safe(difference):
            safe += 1
        else:
            for i, _ in enumerate(report):
                report_copy = report.copy()
                print(report)
                report_copy.pop(i)
                print(report_copy)
                if check_safe(calc_difference(report_copy)):
                    safe += 1
                    break

print(safe)
