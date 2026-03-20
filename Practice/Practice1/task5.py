prices = list(map(float, input().split()))

K = int(input())
M = int(input())

discount = [x-(x//K*M) for x in prices]

print(prices)
print(discount)