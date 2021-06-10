#BOJ2872 우리집엔 도서관이 있어 20210610
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [int(input()) for _ in range(n)]
    dic = {}
    for i in range(n):
        dic[li[i]] = i

    cnt = 1
    for i in range(n, 1, -1):
        if dic[i] > dic[i-1]:
            cnt += 1 
        else:
            break
    print(n-cnt)
if __name__ == '__main__':
    main()