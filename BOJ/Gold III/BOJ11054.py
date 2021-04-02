#BOJ11054 가장 긴 바이토닉 부분 수열 20210402
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int, input().rstrip().split()))
    inc = [1] * n
    dec = [1] * n
    for i in range(n):
        num = li[i]
        big = 0
        small = 0
        for j in range(i):
            if li[j] < num:
                big = max(big,inc[j])
            elif li[j] > num:
                small = max(max(inc[j],dec[j]), small)
        inc[i] = big + 1
        dec[i] = small + 1
    print(max(max(inc),max(dec)))
if __name__ == '__main__':
    main()