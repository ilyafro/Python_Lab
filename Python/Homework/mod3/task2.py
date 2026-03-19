s = input().strip()
n = int(s) if s.isdigit() and s != "0" else 0
print(f"{bin(n)[2:]}, {oct(n)[2:]}, {hex(n)[2:].upper()}" if n > 0 else "Неверный ввод")