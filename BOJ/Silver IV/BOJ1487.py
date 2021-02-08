#BOJ1487 물건팔기 20210208 
import sys
input = sys.stdin.readline

def main():
    li = sorted([list(map(int, input().rstrip().split())) for _ in range(int(input().rstrip()))], key=lambda x : x[0])
    n = len(li)
    maxProfit = -1
    res = 0
    for i in range(0,n):
        price = li[i][0]
        profit = 0
        for j in range(i,n):
            tmp = price - li[j][1] 
            if tmp > 0 : profit += tmp
        if profit > maxProfit:
            maxProfit = profit
            res = price             
    print(res if maxProfit > 0 else 0)
if __name__ == '__main__':
    main()
