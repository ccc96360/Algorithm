#BOJ2352 반도체 설계 20210408 , 원소까지 찾음
import sys
import bisect
input = sys.stdin.readline

INF = sys.maxsize

def main():
    n = int(input())
    li = list(map(int,input().rstrip().split()))
    dp = [li[0]]
    dpSize = 1
    p = []
    for v in li:
        if dp[-1] < v:
            dp.append(v)
            p.append(dpSize)
            dpSize += 1
        else:
            idx = bisect.bisect_left(dp,v)
            dp[idx] = v
            p.append(idx)
    # print(len(dp)) 만 하면 정답, p리스트 필요없음
    # 진짜 부분 수열 구하기.
    res = []
    for i in range(len(p)-1, -1, -1):
        if p[i] == dpSize-1:
            res.append(li[i])
            dpSize -= 1
    res.reverse()
    print(len(res))
if __name__ == '__main__':
    main()