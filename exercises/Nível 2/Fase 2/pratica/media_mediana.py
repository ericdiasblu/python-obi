a, b = map(int, input().split())

res = None
for c in range(-10**6, 10**6 + 1):
    nums = [a, b, c]
    nums.sort()
    media = (a + b + c) / 3
    mediana = nums[1]
    if media == mediana:
        res = c
        break

print(res)