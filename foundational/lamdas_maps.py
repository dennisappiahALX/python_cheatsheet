items = [
    ("product1", 100),
    ("product2", 30),
    ("product 3", 40)
]

# sorting
items.sort(key=lambda item: item[1])
print(items)

# mapping - transforming item list into list of only prices
prices = list(map(lambda item: item[1], items))
print(prices)


# filtering
filtered_price = list(filter(lambda item: item[1] > 30, items))
print(filtered_price)
