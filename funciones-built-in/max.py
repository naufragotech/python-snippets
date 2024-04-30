# Cómo usar la función max
# l1 = [3, 2, 1, 4, 5]
# print(max(l1))

# l2 = ["z", "c", "a"]
# print(max(l2))

l3 = [3, 3, 3, 1, 5, 5]
print(max(l3, key=lambda x: l3.count(x)))
