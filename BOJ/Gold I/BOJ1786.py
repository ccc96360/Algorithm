#BOJ1786 찾기 20210427
import sys
input = sys.stdin.readline

def getPi(str,n):
    ret = [0]*n
    j = 0
    for i in range(1,n):
        while j > 0 and str[i] != str[j]: j = ret[j-1]
        if str[i] == str[j]:
            j += 1
            ret[i] = j
    return ret
def main():
    t,p = [list(input()) for _ in range(2)]
    if t[-1] == "\n": t.pop()
    if p[-1] == "\n": p.pop()
    n = len(t)
    m = len(p)
    pi = getPi(p,m)
    i = j = 0
    res = []
    for i in range(n):
        while j > 0 and t[i] != p[j]:
            j = pi[j-1]
        if t[i] == p[j]:
            if j == m-1:
                res.append(i-j)
                j = pi[j]
            else:
                j += 1

    res = list(map(lambda x: x+1, res))
    print(len(res))
    print(*res)
if __name__ == '__main__':
    main()