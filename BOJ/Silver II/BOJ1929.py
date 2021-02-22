#BOJ1929 소수 구하기 20210222
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    isPrime = [False] + [True for _ in range(1000000)]
    isPrime[1] = False
    for i in range(2, 1001):
        if isPrime[i]:
            for j in range(i*2, 1000001, i):
                isPrime[j] = False
    for i in range(n,m+1):
        if isPrime[i]: print(i)
if __name__ == '__main__':
    main()