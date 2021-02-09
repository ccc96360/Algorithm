#BOJ1817 집 챙기는 숌 20210209
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().rstrip().split(" "))
    li = []
    if n != 0 : li = list(map(int, input().rstrip().split(" ")))
    w = 0; res = 0
    for i in li:
        if w + i > m:
            res += 1
            w = 0
        w += i
    if w > 0 : res += 1
    print(res)
if __name__ == '__main__':
    main()