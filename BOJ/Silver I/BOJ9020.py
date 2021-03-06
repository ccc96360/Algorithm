#BOJ9020 골드바흐의 추측 20210306
import sys
from math import sqrt
input = sys.stdin.readline

def main():
    n = 10000
    isPrime = [False,False] + [True for _ in range(n)]
    for i in range(2, int(sqrt(n+1))):
        if not isPrime[i] : continue
        for j in range(i*2, n+1, i):
            isPrime[j] = False
    primes = []
    for i in range(n+1):
        if isPrime[i]: primes.append(i)
    for _ in range(int(input())):
        a = int(input())
        min_ = 10000
        res = []
        for v in primes:
            if v >= a: break
            b = a - v
            if isPrime[b]:
                if min_ > abs(v-b):
                    res = [v,b]
                    min_ = abs(v-b)
        res.sort()
        print(*res)
        
if __name__ == '__main__':
    main()