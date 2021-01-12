#BOJ1388 바닥 장식 20210112
def main():
    n,m = map(int, input().split(" "))
    li = [input() for _ in range(n)]
    res = 0
    for i in range(n):
        k = 0; cnt = 0
        for j in range(m):
            if li[i][j] == "-":
                k = j
                cnt = 1
                break
        flag = False
        for j in range(k,m):
            if li[i][j] == "|":
                flag =True
            if flag and li[i][j] == "-":
                cnt += 1
                flag = False
        res += cnt
    for i in range(m):
        k = 0; cnt = 0
        for j in range(n):
            if li[j][i] == "|":
                k = j
                cnt = 1
                break
        flag = False
        for j in range(k,n):
            if li[j][i] == "-":
                flag = True
            if flag and li[j][i] == "|":
                cnt += 1
                flag = False
        res += cnt
    print(res)
            
if __name__ == '__main__':
    main()