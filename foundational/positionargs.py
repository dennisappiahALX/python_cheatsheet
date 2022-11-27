def add(*numbers):
    print(numbers)

    total = 1
    for number in numbers:
        total += number

    return total


print(add(4, 5, 6, 7))


def save_user(**user):
    print(user)


save_user(id=1, name="Kofi")
