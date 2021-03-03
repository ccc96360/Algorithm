#BOJ2156 포도주 시식 20210303
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [int(input()) for _ in range(n)]
    dp = [0] + [li[0]]
    if n > 2:
        dp.append(li[1]+li[0])
        for i in range(2,n):
            dp.append(max(max(dp[-1],dp[-2]+li[i]),dp[-3]+li[i]+li[i-1]))
        print(dp[-1])
    else:
        print(sum(li))
if __name__ == '__main__':
    main()