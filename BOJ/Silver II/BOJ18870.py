#BOJ18870 좌표 압축 20210326
import sys
from copy import deepcopy
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int, input().rstrip().split()))
    li2 = deepcopy(li)
    li.sort()
    res = {}
    cnt = 0
    for i in range(n):
        if li[i] not in res:
            res[li[i]] = cnt
            cnt += 1
    for v in li2:
        print(res[v],end=" ")

if __name__ == '__main__':
    main()