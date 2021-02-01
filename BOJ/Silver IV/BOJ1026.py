#BOJ1026 보물 20210201 
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().rstrip().split(" ")))
    b = list(map(int, input().rstrip().split(" ")))
    a.sort(reverse=True)
    b.sort()
    res = 0
    for i in range(n):
        res += a[i] * b[i]
    print(res)

if __name__ == '__main__':
    main()