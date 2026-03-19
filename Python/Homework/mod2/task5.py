s = input().strip()

word = ""
for char in s:
    if char == '.':
        print(word)
        word = ""
    else:
        word += char

print(word)