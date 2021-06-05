def getRank(num):
    return [6,6,5,4,3,2,1][num]

def solution(lottos, win_nums):
    winNum = set(win_nums)
    mnCnt = len(list(filter(lambda x: x in winNum, lottos)))
    mxCnt = mnCnt + lottos.count(0)
    return list(map(getRank, [mxCnt, mnCnt]))

def main():
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))
if __name__ == '__main__':
    main()