#BOJ11062 카드 게임 20210520
import sys
input = sys.stdin.readline
li = []
dp = []
def maxScore(turn, s, e):
    global dp
    if s > e:
        return 0
    if dp[s][e] != -1:
        return dp[s][e]
    if turn:
        ret = max(li[s] + maxScore(not turn, s+1, e), li[e] + maxScore(not turn, s, e-1))
    else:
        ret = min(maxScore(not turn, s+1, e), maxScore(not turn, s, e-1))
    dp[s][e] = ret
    return ret

def main():
    global li,dp
    n = int(input())
    li = list(map(int, input().rstrip().split()))
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    print(maxScore(True, 0, n-1))
if __name__ == '__main__':
    for _ in range(int(input())):
        main()