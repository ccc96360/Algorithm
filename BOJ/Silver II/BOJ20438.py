#BOJ20438 출석체크 20210608
import sys
input = sys.stdin.readline

def main():
    n,k,q,m = map(int, input().rstrip().split())
    sleeping = set(map(int, input().rstrip().split()))
    attendance = list(map(int, input().rstrip().split()))
    canAttenDance = set()
    subSum = [0] * (n+3)
    for v in attendance:
        if v in sleeping: continue
        for nv in range(v, n+3, v):
            if nv not in sleeping: canAttenDance.add(nv)

    for v in range(3, n+3):
        subSum[v] += subSum[v-1]
        if v in canAttenDance: subSum[v] += 1

    for _ in range(m):
        s,e = map(int, input().rstrip().split())
        t = e-s+1
        print(t - (subSum[e]-subSum[s-1]))
if __name__ == '__main__':
    main()