#BOJ11729 하노이 탑 이동 순서 20210223
import sys
input = sys.stdin.readline

res = []
def hanoi(n, start, sub, dst):
    if(n == 1):
        res.append([start, dst])
    else:
        hanoi(n-1, start, dst, sub)
        res.append([start, dst])
        hanoi(n-1, sub, start, dst)
def main():
    n = int(input())
    hanoi(n, 1, 2, 3)
    print(len(res))
    for v in res: print(*v)
if __name__ == '__main__':
    main()