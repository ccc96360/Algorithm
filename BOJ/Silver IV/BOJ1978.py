#BOJ1978 소수 찾기 20210131  
import sys
import math
input = sys.stdin.readline

def main():
    primes = {i : True for i in range(2,1001)}
    n = math.ceil(math.sqrt(1000))
    i = 1
    while i <= n:
        i += 1
        if  i not in primes: continue
        idx = i
        while idx <= 1000:
            idx += i
            if idx not in primes: continue
            del primes[idx]
    n = input()
    cnt = 0
    li = list(map(int, input().rstrip().split(" ")))
    for i in li:
        if i in primes: cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()