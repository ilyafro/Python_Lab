def make_palindrome(s):
    bukv = {}
    for char in s:
        bukv[char] = bukv.get(char, 0) + 1

    necetn = []
    for char, count in bukv.items():
        if count % 2 == 1:
            necetn.append(char)

    if len(necetn) > 1:
        return ""

    nachalo = []
    for char in sorted(bukv.keys()):
        nachalo.append(char * (bukv[char] // 2))

    nach = ''.join(nachalo)
    center = necetn[0] if necetn else ''
    palindrome = nach + center + nach[::-1]
    return palindrome

s = input().strip()
result = make_palindrome(s)

print(result)