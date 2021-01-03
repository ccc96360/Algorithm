def main():
    m = int(input())
    ballCup = 1
    cupLocs = [1,2,3]
    for i in range(m):
        x,y = map(int, input().split())
        tmp = cupLocs[x-1]
        cupLocs[x-1] = cupLocs[y-1]
        cupLocs[y-1] = tmp
        print(cupLocs)
    idx = 0
    for i in range(3):
        if cupLocs[i] == 1:
            idx = i
    print(idx+1)
if __name__ == '__main__':
    main()