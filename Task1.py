try:
    input_file = open("input", "r")
except FileNotFoundError:
    print("boooo")

list1 = []
list2 = []

for line in input_file:
    split_line = line.split()
    list1.append(split_line[0])
    list2.append(split_line[1])

print(list1)
print(list2)


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if (swapped == False):
            break


bubble_sort(list1)
bubble_sort(list2)
total_diff = 0
for n in range(len(list1)):
    diff = abs(int(list1[n]) - int(list2[n]))
    total_diff += diff

print(total_diff)