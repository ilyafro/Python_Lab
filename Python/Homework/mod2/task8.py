s = input().strip()
s += " "
res = ""
l = range(len(s))
for i in l:
    if s[i] == ' ':
        res+= s[i-1]

print(res)