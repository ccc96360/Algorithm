#BOJ1644 소수의 연속합 20210401
import sys
from math import sqrt
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())
    isPrime = [False, False] + [True for _ in range(n)]
    for i in range(2,int(sqrt(n))+1):
        for j in range(i+i, n+2, i):
            isPrime[j] = False
    primes = []
    for i in range(n+1): 
        if isPrime[i]: primes.append(i)
    q = deque()
    sum = res = 0
    for v in primes:
        while sum + v > n:
            sum -= q.popleft()
        q.append(v)
        sum += v
        if sum == n: res += 1
    print(res)

if __name__ == '__main__':
    main()