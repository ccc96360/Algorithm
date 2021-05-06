#BOJ12904 A와 B 20210506
import sys
input = sys.stdin.readline

def main():
    s = list(input().rstrip())
    t = list(input().rstrip())

    while t:
        if s == t:
            return print(1)
        else:
            p = t.pop()
            if p == "B":
                t.reverse()
    print(0)

if __name__ == '__main__':
    main()