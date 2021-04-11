#BOJ2143 두 배열의 합 20210411
import sys
input = sys.stdin.readline

def getSum(li,n):
    sums = [[] for _ in range(n)]
    for i in range(n):
        sums[i].append(li[i])
        for j in range(i+1,n):
            sums[i].append(sums[i][-1] + li[j])
    ret = []
    for v in sums: ret.extend(v)
    return ret

def main():
    t,n = [int(input()) for _ in range(2)]
    a = list(map(int,input().rstrip().split()))
    m = int(input())
    b = list(map(int,input().rstrip().split()))
    sumA = getSum(a,n)
    sumB = getSum(b,m)
    dicA = {}
    for v in sumA:
        if v not in dicA:
            dicA[v] = 1
        else:
            dicA[v] += 1
    cnt = 0
    for v in sumB:
        if t-v in dicA:
            cnt += dicA[t-v]
    print(cnt)
if __name__ == '__main__':
    main()