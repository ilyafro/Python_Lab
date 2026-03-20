N = int(input())
num = list(range(N,N*N+1))

roots = [x**0.5 for x in num]

print(num)
print(roots)