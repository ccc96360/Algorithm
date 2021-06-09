#BOJ1106 호텔 20210609
import sys
input = sys.stdin.readline

def main():
    c, n= map(int, input().rstrip().split())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    m = c + max(list(map(lambda x: x[1], li)))
    dp = [0] + [sys.maxsize] * m

    for cost, customer in li:
        for cur_customer in range(customer, m+1):
            dp[cur_customer] = min(dp[cur_customer], dp[cur_customer - customer] + cost)
    print(min(dp[c:]))
if __name__ == '__main__':
    main()