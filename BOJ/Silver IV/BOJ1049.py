#BOJ1049 기타줄 20210202
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().rstrip().split(" "))
    a = b = 1001
    for _ in range(m):
        tmp1,tmp2 = map(int, input().rstrip().split(" "))
        a = min(a, tmp1)
        b = min(b, tmp2)
    if a >= b * 6:
        print(n*b)
    else:
        if n % 6 == 0:
            print(a * (n//6))
        else:
            if a * ((n//6) + 1) < a * (n//6) + b * (n % 6):
                print(a * ((n//6) + 1))
            else:
                print(a * (n//6) + b * (n % 6))
if __name__ == '__main__':
    main()