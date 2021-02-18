#BOJ1904 01타일 20210218
import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    a,b = 1,2
    for _ in range(3,n+1):
        a,b = b%15746, (a+b)%15746
    print(b if n != 1 else 1)
if __name__ == '__main__':
    main()