#BOJ1120 문자열 20210201  
import sys
input = sys.stdin.readline

def main():
    a,b = input().rstrip().split(" ")
    n = len(a)
    m = len(b)
    min = 51
    for i in range(0, m - n + 1):
        cnt = 0
        for j in range(i, i + n):
            if a[j-i] != b[j]: cnt += 1
        if min > cnt: min = cnt
    print(min)

if __name__ == '__main__':
    main()