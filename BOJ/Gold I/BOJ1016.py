#BOJ1016 제곱ㄴㄴ수 20210426
import sys
input = sys.stdin.readline

def main():
    mn,mx = map(int,input().rstrip().split())
    squares = []
    v = 2
    while v ** 2 <= mx:
        squares.append(v**2)
        v += 1
    yes = set()
    for v in squares:
        t = mn // v
        t = (v * t) if mn % v == 0 else (v * (t+1))
        while t <= mx:
            yes.add(t)
            t += v
    print(mx - mn + 1 - len(yes))
if __name__ == '__main__':
    main()