#BOJ16900 이름 정하기 20210427
import sys
input = sys.stdin.readline

def getPi(s,n):
    pi = [0] * n
    j = 0
    for i in range(1,n):
        while j > 0 and s[i] != s[j]: j = pi[j-1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    return pi

def main():
    s,n = input().rstrip().split()
    n = int(n)
    m = len(s)
    pi = getPi(list(s),m)
    
    print((m-pi[-1]) * (n-1) + m)
if __name__ == '__main__':
    main()