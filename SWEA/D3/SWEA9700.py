import sys
sys.stdin = open('SWEA9700.txt')

for t in range(1, int(input()) + 1):
    p, q = map(float, input().split())
    s1 = s2 = 0
    s1 = (1 - p) * q
    s2 = p * (1 - q) * q

    if s1 < s2:
        print('#{} YES'.format(t))
    else:
        print('#{} NO'.format(t))
