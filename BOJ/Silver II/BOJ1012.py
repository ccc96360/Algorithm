#BOJ1012 유기농 배추 20210223
import sys
from collections import deque
input = sys.stdin.readline

def main():
    for __ in range(int(input())):
        n,m,k = map(int, input().split())
        dic = {}
        for _ in range(k):
            a,b = map(int,input().split())
            dic[(a,b)] = False
        res = 0
        x = [0,0,-1,1]
        y = [-1,1,0,0]
        for key,val in dic.items():
            if dic[key] : continue
            q = deque([key])
            res += 1
            while q:
                tmp = q.popleft()
                if dic[tmp]: continue
                dic[tmp] = True
                for i in range(4):
                    tmp2 = (tmp[0] + x[i], tmp[1] + y[i])
                    if tmp2 in dic:
                        q.append(tmp2)
        print(res)
if __name__ == '__main__':
    main()