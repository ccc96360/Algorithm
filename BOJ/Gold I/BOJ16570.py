#BOJ16570 앞뒤가 맞는 수열 20210427
import sys
input = sys.stdin.readline

def getPi(li, n):
    pi = [0] * n
    j = 0
    for i in range(1,n):
        while j > 0 and li[i] != li[j]: j = pi[j-1]
        if li[i] == li[j]:
            j += 1
            pi[i] = j
    return pi
def main():
    n = int(input())
    li = list(map(int,input().rstrip().split()))
    li.reverse()
    pi = getPi(li,n)
    mx = max(pi)
    if mx == 0:
        print(-1)
    else:
        print(mx, pi.count(mx))
if __name__ == '__main__':
    main()