#BOJ1914 하노이 탑 20210608
import sys
input = sys.stdin.readline

ans = 0
p = True
def hanoi(n, src, dst, sub):
    global ans
    if n == 1:
        print(src,dst)
        return
    hanoi(n-1, src, sub, dst)
    print(src,dst)
    ans += 1
    hanoi(n-1, sub, dst, src)
def main():
    global p
    n = int(input())
    print(2**n-1)
    if n <= 20: hanoi(n, 1, 3, 2)
if __name__ == '__main__':
    main()