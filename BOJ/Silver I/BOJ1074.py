#BOJ1074 Z 20210310
import sys
input = sys.stdin.readline


def z(n,p,cnt,dst):
    x = p[0]
    y = p[1]
    if n == 0:
        return cnt
    else:
        mid = (2**n)//2
        loc = 0
        dx = [0,1,0,1]
        dy = [0,0,1,1]
        if x + mid <= dst[0] < x + 2**n and y <= dst[1] < y + mid:
            loc = 1
        elif x <= dst[0] < x + mid and y+mid <= dst[1] < y + 2**n:
            loc = 2
        elif x + mid <= dst[0] < x + 2**n and y+mid <= dst[1] < y + 2**n:
            loc = 3
        cnt += ((2**(n-1))**2) * loc
        x += mid * dx[loc]
        y += mid * dy[loc]
        return z(n-1,(x,y),cnt,dst)        

def main():
    n, r, c = map(int,input().rstrip().split())
    print(z(n,(0,0),0,(c,r)))
if __name__ == '__main__':
    main()