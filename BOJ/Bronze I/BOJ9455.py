#BOJ9455 박스 20210114
def main():
    for ___ in range(int(input())):
        r,c = map(int, input().split(" "))
        li = []
        for i in range(r):
            l = list(map(int, input().split(" ")))
            li.append(l)
        lev = []
        for i in range(c):
            if li[r-1][i] == 1:
                lev.append(r-2)
            else:
                lev.append(r-1)
        ret = 0
        for i in reversed(range(r-1)):
            for j in range(c):
                if li[i][j] == 1:
                    ret += lev[j] - i
                    lev[j] -= 1
        print(ret)
if __name__ == '__main__':
    main()