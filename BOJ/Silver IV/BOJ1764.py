#BOJ1764 듣보잡 20210209
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().rstrip().split(" "))
    dic = {}
    for _ in range(n):
        dic[input().rstrip()] = True
    res = []
    for _ in range(m):
        s = input().rstrip()
        if s in dic:
            res.append(s)
    res.sort()
    print(len(res))
    for s in res: print(s)
if __name__ == '__main__':
    main()