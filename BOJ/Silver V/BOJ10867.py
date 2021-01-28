#BOJ10867 중복 빼고 정렬하기 20210128
import sys
input = sys.stdin.readline

def main():
    n = input()
    li = list(set(map(int, input().split(" "))))
    li.sort()
    print(*li)

if __name__ == '__main__':
    main()