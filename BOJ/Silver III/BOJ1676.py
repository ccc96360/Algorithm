#BOJ1676 팩토리얼 0의 개수 20210219
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    print(n//5 + n // 25 + n//125)
if __name__ == '__main__':
    main()