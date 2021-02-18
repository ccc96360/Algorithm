#BOJ1270 전쟁 - 땅따먹기 20210218
import sys
input = sys.stdin.readline

def main():
    for __ in range(int(input().rstrip())):
        li = list(map(int, input().rstrip().split(" ")))
        dic = {}
        half = li[0] // 2
        max = 0
        res = "SYJKGW"
        for i in range(1,li[0]+1):
            team = li[i]
            if team in dic:
                dic[team] += 1
                if dic[team] > half and dic[team] > max :
                    max = dic[team]
                    res = team
            else:
                dic[team] = 1
        print(res)
if __name__ == '__main__':
    main()