import math
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ySum = mSum = 0
    for i in range(n):
        ySum += math.ceil(arr[i]/30) * 10 if arr[i] % 30 != 0 else 10 + math.ceil(arr[i]/30) * 10
        mSum += math.ceil(arr[i]/60) * 15 if arr[i] % 60 != 0 else 15 + math.ceil(arr[i]/60) * 15
    print("Y {0}".format(ySum) if ySum < mSum else "M {0}".format(mSum) if ySum > mSum else "Y M {0}".format(ySum))
if __name__ == '__main__':
    main()