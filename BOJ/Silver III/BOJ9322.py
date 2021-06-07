#BOJ9322 철벽 보안 알고리즘 20210607
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    pub1 = list(input().rstrip().split())
    pub2 = list(input().rstrip().split())
    dic = {pub1[i] : i for i in range(n)}
    dic2 = {pub2[i] : i for i in range(n)}
    secret = list(input().rstrip().split())
    res = [0] * n
    for k,v in dic.items():
        to = v
        from_ = dic2[k]
        res[to] = secret[from_]
    print(*res)
if __name__ == '__main__':
    for _ in range(int(input())):
        main()