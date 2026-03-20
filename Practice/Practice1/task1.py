names = input().split()

uni = []

lengths = set()

for name in names:
    length = len(name)
    if length not in lengths:
        lengths.add(length)
        uni.append(name)

print(names)
print(uni)