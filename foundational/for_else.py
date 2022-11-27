successful = False

for number in range(3):
    print("Attempt")
    if successful:
        break
else:
    # only executes if the loop exhausts
    print("Attempted three times and failed")

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

active_users = dict(
    filter(lambda status: status[1] == 'active', users.items()))
print(active_users)
