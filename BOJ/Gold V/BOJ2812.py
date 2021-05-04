#BOJ2812 크게 만들기 20210504
import sys
input = sys.stdin.readline

def main():
    n,k = map(int,input().rstrip().split())
    li = list(map(int,list(input().rstrip())))
    
    res = []
    delete = cnt = 0
    for i in range(n):
        v = li[i]
        while res and delete < k:
            if res[-1] < v:
                res.pop()
                cnt -= 1
                delete += 1
            else: 
                break
        if cnt < n-k:
            res.append(v)
            cnt += 1
    for v in res:
        print(v, end="")
if __name__ == '__main__':
    main()