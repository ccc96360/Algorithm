#BOJ2003 수들의 합 2 20210220
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().rstrip().split())
    li = list(map(int, input().rstrip().split()))
    a = b = cnt = sum_ = 0
    while True:
        if b == n and sum_ < m: break
        if sum_ < m:
            sum_ += li[b]
            b += 1
        else:
            sum_ -= li[a]
            a += 1
        if sum_ == m: cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()