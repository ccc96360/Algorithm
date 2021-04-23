#BOJ10253 헨리 20210423
import sys
from math import gcd
input = sys.stdin.readline

def minus(a,b, j,m):
    return a*m - b*j, b*m

def main():
    a,b = map(int,input().rstrip().split())
    while a != 1:
        j = 1
        m = (b // a) + 1
        a,b = minus(a,b,j,m)
        t = gcd(a,b)
        a //= t
        b //= t
    print(b)
if __name__ == '__main__':
    for _ in range(int(input())):
        main()