#BOJ12015 가장 긴 증가하는 부분 수열2 20210415
import sys
import bisect 
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int,input().rstrip().split()))
    res = [li[0]]
    for v in li:
        if v > res[-1]:
            res.append(v)
        else:
            idx = bisect.bisect_left(res,v)
            res[idx] = v
    print(len(res))
if __name__ == '__main__':
    main()