nums = list(map(int, input().split()))

ravn = True
razn = True

for i in range(1, len(nums)):
    if nums[i] != nums[0]:
        ravn = False
        break

if not ravn:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                razn = False
                break
        if not razn:
            break

if ravn:
    print("Все числа равны")
elif razn:
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")