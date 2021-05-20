#BOJ2600 구슬게임 20210520
import sys
input = sys.stdin.readline

dp = []
def play(turn, k1, k2, b):
    global dp
    if dp[k1][k2][turn] >= 0: return dp[k1][k2][turn]
    if k1+k2 == 0:
        dp[k1][k2][turn] = 0
        return 0
    for v in b:
        if v <= k1 and not play(1-turn, k1-v, k2, b):
            dp[k1][k2][turn] = 1
            return 1
        if v <= k2 and not play(1-turn, k1, k2-v, b):
            dp[k1][k2][turn] = 1
            return 1
    dp[k1][k2][turn] = 0
    return 0
def main():
    global dp
    b = list(map(int,input().rstrip().split()))
    for _ in range(5):
        k1,k2 = map(int,input().rstrip().split())
        dp = [[[-1] * 2  for _ in range(501)] for _ in range(501)]
        print("A" if play(1, k1, k2, b) else "B")
if __name__ == '__main__':
    main()