s = input().strip()

k = -1
# находим запятую для разделения чисел
for i in range(len(s)):
    if s[i] == ',':
        q = i
        break

a_str = ""
for i in range(q):
    if s[i] != ' ':
        a_str += s[i]

b_str = ""
for i in range(q + 1, len(s)):
    if s[i] != ' ':
        b_str += s[i]

a = int(a_str)
b = int(b_str)

res = a % b

print(res)