numbers = list(map(int, input().split()))
K = int(input())

res = [x for x in numbers if x % K == 0]

print(numbers)
print(res)