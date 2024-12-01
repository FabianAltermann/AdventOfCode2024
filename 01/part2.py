import csv
from collections import Counter


def main() -> None:
    with open("./data.txt", "r") as file:
        reader = csv.reader(file, delimiter=" ", skipinitialspace=True)
        list1 = []
        list2 = []

        for line in reader:
            list1.append(int(line[0]))
            list2.append(int(line[1]))

    count = Counter(list1)

    print(sum([count[i] * i for i in list2]))


if __name__ == "__main__":
    main()
