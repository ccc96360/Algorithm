#BOJ2096 내려가기 20210329
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a,b,c = map(int,input().rstrip().split())
    max_a,max_b,max_c = a,b,c
    min_a,min_b,min_c = a,b,c
    for _ in range(n-1):
        a,b,c = map(int, input().rstrip().split())
        mx_a, mn_a = max(max_a, max_b) + a, min(min_a,min_b) + a
        mx_b, mn_b = max(max(max_a, max_b), max_c)+ b, min(min(min_a,min_b), min_c)+ b
        mx_c, mn_c = max(max_b, max_c) + c, min(min_b,min_c) + c
        max_a, max_b, max_c, min_a, min_b, min_c = mx_a, mx_b, mx_c, mn_a, mn_b, mn_c
    print(max(max(max_a, max_b), max_c), end=" ")
    print(min(min(min_a, min_b), min_c))
if __name__ == '__main__':
    main()