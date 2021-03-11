#BOJ1309 동물원 20210311
import sys
input = sys.stdin.readline

def main():
    a,b = 1,3
    c = 3
    n = int(input())
    for i in range(2,n+1):
        c = (b*2 + a)%9901
        a = b
        b = c
    print(c)
if __name__ == '__main__':
    main()