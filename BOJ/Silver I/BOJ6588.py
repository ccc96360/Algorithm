#BOJ6588 골드바흐의 추측 20210310
import sys
from math import sqrt
input = sys.stdin.readline

def main():
    n = 1000000
    isPrime = [False, False] + [True] * (n-1)
    for i in range(2,int(sqrt(n+1))):
        if not isPrime[i]: continue
        for j in range(i+i, n+1, i):
            isPrime[j] = False
    primes = []
    for i in range(2,n+1):
        if isPrime[i]: primes.append(i)
    res = []
    while True:
        n = int(input())
        if n == 0: break
        for a in primes:
            b = n - a
            if isPrime[b]:
                res.append("{0} = {1} + {2}".format(n,a,b))
                break
            if a > b:
                res.append("Goldbach's conjecture is wrong.")
                break
    print(*res,sep='\n')

if __name__ == '__main__':
    main()