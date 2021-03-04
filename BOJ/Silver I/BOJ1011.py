#BOJ1011 Fly me to the Alpha Centauri 20210304
import sys
from math import floor, sqrt
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        x,y = map(int, input().rstrip().split())
        dif = y-x
        res = dif
        if dif > 3:
            n = int(sqrt(dif))
            res = 2 * n + (-1 if dif == n ** 2 else 0 if n ** 2 < dif <= n**2+n else 1)
        print(res)
if __name__ == '__main__':
    main()