s = sorted(map(int, input().split()))
a = any(s[i] == s[i + 1] for i in range(len(s) - 1))
print(a)