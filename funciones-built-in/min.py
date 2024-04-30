# Cómo usar la función min
# l1 = [3, 2, 1, 4, 5]
# print(min(l1))

# l2 = ["z", "c", "a"]
# print(min(l2))

l3 = [3, 1, 1, 5, 5]
print(min(l3, key=lambda x: l3.count(x)))
