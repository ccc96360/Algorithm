#BOJ11659 구간 합 구하기 4 20210221
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().rstrip().split())
    li = list(map(int, input().rstrip().split()))
    sumI =[0]
    sum_ = 0
    for v in li:
        sum_ += v
        sumI.append(sum_)
    for _ in range(m):
        a,b = map(int, input().rstrip().split())
        print(sumI[b] - sumI[a-1])
if __name__ == '__main__':
    main()