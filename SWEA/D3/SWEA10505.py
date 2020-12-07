for t in range(1, int(input()) + 1):
    n = int(input())
    income = list(map(int, input().split()))
    avg_income = sum(income) // n
    sol = list(filter(lambda x: x <= avg_income, income))
    print('#{} {}'.format(t, len(sol)))