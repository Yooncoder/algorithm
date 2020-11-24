n = int(input())
n_list = list(map(int, input().split()))
m = int((n - 1) / 2)

print(sorted(n_list)[m])