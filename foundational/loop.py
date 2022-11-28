for number in range(5):
    print(number * "*")


# NestedLoops
for n in range(4):
    for x in range(4):
        print(x, end=" ")
    print()

for i in range(5):
    for x in range(i):
        print(x, end=" ")
    print()


for i in range(5):
    for x in range(1, i):
        print(x, end=" ")
    print()


items = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [x for x in items if x % 2 == 0]

even_num = list(filter(lambda item: item % 2 == 0, items))
print(even_num)
print(even_numbers)
