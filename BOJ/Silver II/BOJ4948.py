#BOJ4948 베르트랑 공준 20210225
import sys
from math import sqrt
input = sys.stdin.readline

def main():
    maxN = 123456*2
    isPrime = [False,False] + [True for _ in range(maxN)]
    for i in range(2, int(sqrt(maxN+1))):
        if not isPrime[i] : continue
        for j in range(i*2, maxN+1, i):
            isPrime[j] = False
    while True:
        n = int(input())
        if n == 0: break
        cnt = 0
        for i in range(n+1,2*n +1):
            if isPrime[i]: cnt += 1
        print(cnt)
if __name__ == '__main__':
    main()