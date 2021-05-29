#BOJ4673 셀프 넘버 20210529
def makeNotSelfNumber(n):
    tmp = list(map(int, str(n)))
    return n + sum(tmp)
def main():
    nonSelfNumber = set()
    for i in range(1, 10000):
        n = makeNotSelfNumber(i)
        while n < 10000 and n not in nonSelfNumber:
            nonSelfNumber.add(n)
            n = makeNotSelfNumber(n)
    for i in range(1,10000):
        if i not in nonSelfNumber: print(i)
if __name__ == '__main__':
    main()