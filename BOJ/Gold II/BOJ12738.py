#BOJ12738 가장 긴 증가하는 부분 수열 3 20210420
import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int,input().rstrip().split()))
    ans = [li[0]]
    for v in li:
        if v > ans[-1]:
            ans.append(v)
        else:
            idx = bisect_left(ans, v)
            ans[idx] = v
    print(len(ans))
if __name__ == '__main__':
    main()