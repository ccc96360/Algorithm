#BOJ17298 오큰수 20210514
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int, input().rstrip().split()))

    stack = []
    res = [-1] * n
    for i in range(n):
        while stack and li[stack[-1]] < li[i]:
            idx = stack.pop()
            res[idx] = li[i]
        stack.append(i)
    print(*res)

if __name__ == '__main__':
    main()