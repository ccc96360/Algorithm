#BOJ2749 피보나치 수 3 20210415
import sys
input = sys.stdin.readline

def main():
    p = 15 * (10 ** 5)
    n = int(input())
    a,b = 0,1
    for _ in range(1,n%p):
        b,a = (a+b)%1000000,b
    print(b)
if __name__ == '__main__':
    main()