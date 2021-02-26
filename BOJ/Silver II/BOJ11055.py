#BOJ11055 가장 큰 증가 부분 수열 20210226
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int, input().split()))
    sum_ = [0 for _ in range(n)]
    for i in range(n):
        max_ = 0
        for j in range(i):
            if sum_[j] > max_ and li[j] < li[i]:
                max_ = sum_[j]
        sum_[i] = max_ + li[i]
    print(max(sum_))
if __name__ == '__main__':
    main()