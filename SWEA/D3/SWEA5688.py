for t in range(1, int(input()) + 1):
    sol = round(pow(int(input()), 1/3), 2)
    if sol != int(sol):
        print('#{} {}'.format(t, -1))
    else:
        print('#{} {}'.format(t, int(sol)))