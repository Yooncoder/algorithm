k = int(input())

sol = 0

for i in range(0, 4):
    if k <= 0:
        break
    j = k % 10
    k = int(k / 10)
    sol += j

print(sol)