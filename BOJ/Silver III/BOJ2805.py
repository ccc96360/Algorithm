#BOJ2805 나무 자르기 20210217
import sys
input = sys.stdin.readline

def main():
    n,m = map(int,input().rstrip().split(" "))
    li = sorted(map(int, input().rstrip().split(" ")))
    f = 0; l = li[-1]
    mid = (f+l)//2
    res = 0
    while f <= l:
        mid = (f+l)//2
        s = sum([v-mid if v > mid else 0 for v in li])
        if s >= m:
            f = mid + 1
            res = max(res,mid)
        else:
            l = mid - 1
    print(res)
if __name__ == '__main__':
    main()