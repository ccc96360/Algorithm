#BOJ1744 수 묶기 20210515
import sys
input = sys.stdin.readline

def calc(li):
    ret = 0
    while li and li[-1] == 1:
        ret += li.pop()
    tmp, cnt = 1,0
    for v in li:
        tmp *= v
        cnt += 1
        if cnt == 2:
            cnt = 0
            ret += tmp
            tmp = 1
    if len(li) % 2 == 1: ret += li[-1]
    return ret

def main():
    n = int(input())
    li = [int(input()) for _ in range(n)]
    li.sort()
    minus = []
    plus = []
    for v in li:
        tmp = minus if v <= 0 else plus
        tmp.append(v)
    plus.reverse()
    ans = calc(minus) + calc(plus)
    print(ans)

if __name__ == '__main__':
    main()