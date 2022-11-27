prices = [2, 4, 5, 7, 8]

# reverse
print(prices[::-1])

# slicing

print(prices[:3])
print(prices[1:-1])  # 457
print(prices[-1:-3])  # 7,8

# swapping variables
x = 4
y = 8

# z= x
# x=y
# y = z
x, y = y, x

print(f"({x}, {y})")

squared_prices = list(map(lambda x: x * x, prices))
print(squared_prices)

prices_greater_16 = list(filter(lambda x: x > 16, squared_prices))
print(prices_greater_16)

# Generators - to store infinite large data, use generator instead of list
my_list = [1, 3, 6, 10]

generator = (x**2 for x in my_list)

for x in generator:
    print(x)


# Unpacking elements as arguments - taking individual elements of an iterable

first = {"x": 3}
second = {"x": 10, "y": 5}

combined = {**first, **second}
print(combined)
