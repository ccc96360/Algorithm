#BOJ1107 리모컨 20210317
import sys
input = sys.stdin.readline

def canMake(channel,nums):
    channel = str(channel)
    for v in channel:
        if v not in nums:
            return False
    return True


def main():
    n = input().rstrip()
    m = int(input())
    nums = set(["0","1","2","3","4","5","6","7","8","9"])
    for v in input().rstrip().split():
        nums.remove(v)
    n = int(n)
    min_ = abs(n - 100)
    for v in range(1000000):
        if canMake(v, nums):
            min_ = min(min_, abs(v - n) + len(str(v)))
    print(min_)
if __name__ == '__main__':
    main()