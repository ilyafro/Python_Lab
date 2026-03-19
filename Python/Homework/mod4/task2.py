a, n = map(int, input().split())
if (n % 2 == 0):
    print((a ** 2) ** (n/2))
else:
    print(a * (a ** (n-1)))
