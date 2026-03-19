s = input().strip()
print(''.join(x for x in s if x == '+' or '0' <= x <= '9'))