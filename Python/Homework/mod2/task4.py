s = input().strip()
if s == "":
    print("Неверный ввод")
else:
    v = True
    for ch in s:
        if ch < '0' or ch > '9':
            v = False
            break
    if not v:
        print("Неверный ввод")
    else:
        n = int(s)
        if n <= 0:
            print("Неверный ввод")
        else:
            num = n
            res2 = ""
            while num > 0:
                r = num % 2
                res2 = chr(ord('0') + r) + res2
                num = num // 2

            num = n
            res8 = ""
            while num > 0:
                r = num % 8
                res8 = chr(ord('0') + r) + res8
                num = num // 8

            num = n
            res16 = ""
            digits = "0123456789ABCDEF"
            while num > 0:
                r = num % 16
                res16 = digits[r] + res16
                num = num // 16

            print(f"{res2}, {res8}, {res16}")
