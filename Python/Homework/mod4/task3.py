def nod(a, b):
    return a if b == 0 else nod(b, a % b)

a, b = map(int, input().split())
print(nod(a, b))