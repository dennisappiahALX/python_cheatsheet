from pprint import  pprint
sentence = "This is a common interview question"
char_count = {}

for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# pprint(char_count, width= 1)

char_count_sorted = sorted(char_count.items(),
                           key=lambda val: val[1],
                           reverse=True)
pprint(char_count_sorted)
print(char_count_sorted[0])