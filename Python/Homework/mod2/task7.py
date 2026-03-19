s = input().strip()
res = 0

q = -1
# находим запятую для разделения чисел
for i in range(len(s)):
    if s[i] == ',':
        q = i
        b = s[i+1]
        break

a_str = ""
for i in range(q):
    if s[i] != ' ':
        a_str += s[i]

for char in a_str:
    if char == b:
        res = res + 1
    else:
        print(res)
        break