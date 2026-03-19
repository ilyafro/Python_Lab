s = input().strip()
one = 0
zero = 0
for char in s:
    if char == '1':
      one = one + 1
    else:
        zero = zero + 1

if one == zero:
    print("yes")
else:
    print("no")