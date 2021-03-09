#BOJ1629 곱셈 20210309
import sys
input = sys.stdin.readline

def f(a,b,c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        tmp = f(a,b//2,c)
        return (tmp ** 2) % c
    elif b % 2 != 0:
        tmp = f(a,(b-1)//2,c)
        return (a * tmp ** 2) % c
def main():
    a,b,c = map(int, input().rstrip().split())
    print(f(a,b,c))
if __name__ == '__main__':
    main()