s = input().strip()

result = ""
for char in s:
    if char == '+' or ('0' <= char <= '9'):
        result += char

print(result)