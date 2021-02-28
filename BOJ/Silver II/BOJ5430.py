#BOJ5430 AC 20210228
import sys
from collections import deque
input = sys.stdin.readline

FRONT = 1
BACK = -1
def main():
    for _ in range(int(input())):
        cmd = input().rstrip()
        n = int(input())
        if n == 0:
            __=input()
            print("[]" if cmd.find("D") == -1 else "error")
            continue
        li = list(map(int,input().rstrip()[1:-1].split(",")))
        q=deque(li)
        switch = lambda x:  x * -1
        dir = FRONT
        err = False
        for c in cmd:
            try:
                if c == 'R':
                    dir = switch(dir)
                else:
                    if dir == FRONT:
                        q.popleft()
                    else:
                        q.pop()
            except IndexError:
                print("error")
                err = True
                break
        if not err:
            if dir == BACK:
                q.reverse()
            print("["+",".join(list(map(str,q)))+"]")

if __name__ == '__main__':
    main()