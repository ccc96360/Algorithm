import operator
def main():
    s = input().upper()
    mapp = {}
    for i in s:
        if i in mapp:
            mapp[i] += 1
        else:
            mapp[i] = 1
    sMap = sorted(mapp.items(), reverse = True,key = operator.itemgetter(1))
    if len(sMap) == 1:
        print(sMap[0][0])
    else:
        print(sMap[0][0] if sMap[0][1] != sMap[1][1] else "?")

if __name__ == '__main__':
    main()
