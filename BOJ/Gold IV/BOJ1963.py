#BOJ1963 소수 경로 20210331
import sys
from math import sqrt
from collections import deque
input = sys.stdin.readline

def changeDigitN(n, num, changeNum):
    li = list(str(num))
    li[n] = str(changeNum)
    return int("".join(li))

def main():
    isPrime = [False,False] + [True for _ in range(9999)]
    for i in range(2,int(sqrt(10000))):
        for j in range(i+i, 10001, i):
            isPrime[j] = False
    primes = {}
    for i in range(2,10001):
        if isPrime[i]: primes[i] = 0

    s,e = map(int,input().rstrip().split())
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        if v == e:
            return print(primes[v])
        for digit in range(4):
            for n in range(10):
                tmp = changeDigitN(digit, v, n)
                if tmp >= 1000 and isPrime[tmp] and tmp != s:
                    if primes[tmp] == 0:
                        primes[tmp] = primes[v] + 1
                        q.append(tmp)    
    print("Impossible")
if __name__ == '__main__':
    for _ in range(int(input())):
        main()
    