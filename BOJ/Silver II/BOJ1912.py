#BOJ1912 연속합 20210223
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int, input().rstrip().split()))
    sum_ = [li[0]]
    for i in range(1,n):
        sum_.append(li[i]+sum_[i-1])
    curMin = res = sum_[0]
    for i in range(1,n):
        res = max(max(sum_[i],sum_[i]-curMin), res)
        curMin = min(curMin,sum_[i])
    print(res)
if __name__ == '__main__':
    main()