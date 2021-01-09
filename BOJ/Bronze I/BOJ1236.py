def main():
    n,m = map(int, input().split(" "))
    arr = [input() for _ in range(n)]
    row = [False for _ in range(n)]
    col = [False for _ in range(m)]
    res = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "X":
                row[i] = True
                col[j] = True
    for i in range(n):
        for j in range(m):
            if not row[i] and not col[j]:
                res += 1
                row[i] = True
                col[j] = True    
            if i == n-1 and not col[j]:
                res += 1
                col[j] = True
        if not row[i]:
            res += 1
            row[i] = True
    print(res)

if __name__ == '__main__':
    main()
