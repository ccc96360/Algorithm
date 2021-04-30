#BOJ11401 이항 계수3 20210430
import sys
input = sys.stdin.readline

P = 1000000007
def pow(v,n):
    if n == 1:
        return v
    if n == 0:
        return 1
    nv = pow(v,n//2)
    nv = nv ** 2
    if n % 2 == 1: nv *= v
    return nv % P

def main():
    n,k = map(int,input().rstrip().split())
    a = b = c = 1
    tmp = 1 
    for i in range(n+1):
        if i > 0: tmp = (tmp*i) % P
        if i == k:
            b = tmp
        if i == n - k:
            c = tmp
        if i == n:
            a = tmp    
    print((a*pow((b*c),P-2))%P)
if __name__ == '__main__':
    main()