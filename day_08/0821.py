three_d_list = [
    [[1, 2, 3],[4, 5, 6]],
    [[7, 8, 9],[10, 11, 12]],
    [[13, 14, 15],[16, 17, 18]]
]

for first in three_d_list:
    for two in first:
        for three in two:
            print(three, end=" ")
    print()

for first in range(len(three_d_list)):
    for two in range(len(three_d_list[first])):
        for z in range(len(three_d_list[first][two])):
            print(three_d_list[first][two][z], end=" ")