'''arr_list = [23,42,44,2,6,2,4,2,3]

def my_list(arr_list):
    total = 0
    for i in arr_list:
        total += i

    return total

print(my_list(arr_list))'''


def test_scope():
    var = 1
    global x
    x = 123
    print(f"{x}")

x = 5
print(x)
test_scope()