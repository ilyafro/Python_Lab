s = input().strip()

# разделяем числа, ищем пробелы
i1 = -1
i2 = -1
for i in range(len(s)):
    if s[i] == ' ':
        if i1 == -1:
            i1 = i
        else:
            i2 = i
            break

a = int(s[:i1])
b = int(s[i1+1:i2])
c = int(s[i2+1:])

if (a <= b <= c):
    print(b)
elif (c <= b <= a):
    print(b)
elif (b <= a <= c):
    print(a)
elif (c <= a <= b):
    print(a)
else:
    print(c)
