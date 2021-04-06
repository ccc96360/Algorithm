#BOJ1300 K번째 수 20210406
import sys
input = sys.stdin.readline

def nthNum(x,n):
    ret = 0 
    for r in range(1,n+1):
        ret += min(x//r,n)
    return ret
def main():
    n = int(input())
    k = int(input())
    l = 1
    r = n**2
    ans = 0
    while l <= r:
        mid = (r+l) // 2
        offset = nthNum(mid,n)
        if offset >= k:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)
if __name__ == '__main__':
    main()