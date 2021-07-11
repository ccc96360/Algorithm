#BOJ2568 전깃줄 - 2 20210503
import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    n = int(input())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    li.sort(key = lambda x : x[0])
    dic = {a:0 for a,b in li}
    res = [li[0][1]]
    size = 1
    for a,b in li:
        if b > res[-1]:
            res.append(b)
            size += 1
            dic[a] = size - 1
        else:
            idx = bisect_left(res, b)
            res[idx] = b
            dic[a] = idx

    res = sorted(dic.items(), key = lambda x : x[0])
    res.reverse()
    ans = []
    for a,v in res:
        if v == size-1:
            size -= 1
        else:
            ans.append(a)

    ans.sort()
    print(len(ans))
    for v in ans:
        print(v)

if __name__ == '__main__':
    main()