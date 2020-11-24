import sys
import heapq
sys.stdin = open('2930.txt')

class ReverseLessThan(object):
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return str(self.value)

def heappush(heap, item):
    reverse = ReverseLessThan(item)
    heapq.heappush(heap, reverse)

def heappop(heap):
    reverse = heapq.heappop(heap)
    return reverse.value

for t in range(1, int(input()) + 1):
    n = int(input())
    heap = []
    print('#{}'.format(t), end = '')
    for i in range(n):
        s = list(map(int, input().split()))
        if s[0] == 1:
            heappush(heap, s[1])
        else:
            if heap:
                print(' {}'.format(heappop(heap)), end='')
            else:
                print(' -1', end='')
    print()