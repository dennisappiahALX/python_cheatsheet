point = {"x": 6, "y": 4}

if "a" in point:
    print(point["a"])
print(point.get("a", 0))

for key, value in point.items():
    print(key, value)

users = {'Hans': 'active', 'Eleonore': 'inactive', '景太郎': 'active'}


active_users = dict(filter(lambda status: status[1] == 'active', users.items()))
print(active_users)