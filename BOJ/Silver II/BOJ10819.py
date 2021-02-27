#BOJ10819 차이를 최대로 20210227
import sys
from itertools import permutations

input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int,input().rstrip().split()))
    max_ = -1
    for v in permutations(li):
        sum_ = 0
        for i in range(1,n):
            sum_ += abs(v[i-1]-v[i])
        max_ = max(max_,sum_)
    print(max_)
if __name__ == '__main__':
    main()