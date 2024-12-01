import csv
from collections import Counter

with open("./data.txt", "r") as file:
    reader = csv.reader(file, delimiter=" ", skipinitialspace=True)
    list1 = []
    list2 = []

    for line in reader:
        list1.append(int(line[0]))
        list2.append(int(line[1]))


count = Counter(list1)

print(sum([count[i] * i for i in list2]))
