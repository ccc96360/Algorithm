def main():
    n = int(input())
    arr = [input() for _ in range(n)]
    res = ""
    for i in range(len(arr[0])):
        tmp = arr[0][i]
        flag = True
        for j in arr:
            if j[i] != tmp:
                flag =False
                break
        res += tmp if flag else "?"
    print(res)

if __name__ == '__main__':
    main()
