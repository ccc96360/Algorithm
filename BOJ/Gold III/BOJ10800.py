#BOJ10800 컬러볼 20210524
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ans = [0] * n
    li = [[i] + list(map(int, input().rstrip().split())) for i in range(n)]
    li.sort(key = lambda x : (x[2],x[1]), reverse = True)
    sumsColor = [0] * (n+1)
    sumsWeight = [0] * 2001
    colorWeightCnt = {}
    totalSum = 0
    for _, color, weight in li:
        sumsColor[color] += weight
        sumsWeight[weight] += weight
        if (color, weight) not in colorWeightCnt:
            colorWeightCnt[(color, weight)] = weight
        else:
            colorWeightCnt[(color, weight)] += weight
        totalSum += weight

    for num, color, weight in li:
        tmp = totalSum - sumsWeight[weight]
        tmp -= sumsColor[color] - colorWeightCnt[(color, weight)]
        ans[num] = tmp

        sumsColor[color] -= weight
        sumsWeight[weight] -= weight
        colorWeightCnt[(color, weight)] -= weight
        totalSum -= weight
    
    for v in ans:
        print(v)
if __name__ == '__main__':
    main()