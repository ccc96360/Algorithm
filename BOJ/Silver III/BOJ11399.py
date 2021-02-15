#BOJ11399 ATM 20210215
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = sorted(map(int, input().rstrip().split(" ")))
    res = 0
    for v in li:
        res += v * n
        n -= 1
    print(res)
if __name__ == '__main__':
    main()