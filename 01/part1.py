import csv


def main() -> None:
    with open("./data.txt", "r") as file:
        reader = csv.reader(file, delimiter=" ", skipinitialspace=True)
        list1 = []
        list2 = []

        for line in reader:
            list1.append(int(line[0]))
            list2.append(int(line[1]))

    list1.sort()
    list2.sort()

    result_list = [abs(list2[i] - list1[i]) for i in range(len(list1))]

    print(sum(result_list))


if __name__ == "__main__":
    main()
