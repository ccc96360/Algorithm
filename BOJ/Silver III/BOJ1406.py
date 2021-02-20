#BOJ1406 에디터 20210220
import sys
input = sys.stdin.readline

def main():
    s = input().rstrip()
    l = [s_ for s_ in s]
    r = []
    for __ in range(int(input().rstrip())):
        cmd = input().rstrip().split()
        if cmd[0] == 'L':
            if l:
                r.append(l.pop())
        elif cmd[0] == 'D':
            if r:
                l.append(r.pop())
        elif cmd[0] == 'B':
            if l:
                l.pop()
        elif cmd[0] == 'P':
            l.append(cmd[1])
    r.reverse()
    print("".join(l+r))
if __name__ == '__main__':
    main()