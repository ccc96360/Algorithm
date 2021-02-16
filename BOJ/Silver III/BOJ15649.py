#BOJ1874 스택 수열 20210216
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    stack = []
    res = []
    li = [i for i in range(1,n+1)]; idx = 0
    for i in range(n):
        num = int(input())
        if idx < n:
            if li[idx] <= num:
                while li[idx]<=num:
                    stack.append(li[idx])
                    idx += 1
                    res.append("+")
                    if idx == n: break
        if stack:
            if stack[-1] == num:
                res.append("-")
                del stack[-1]
            elif stack[-1] > num:
                res = ["NO"]
                break
    for v in res: print(v)
if __name__ == '__main__':
    main()