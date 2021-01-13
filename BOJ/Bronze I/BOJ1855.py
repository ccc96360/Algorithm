#BOJ1855 암호 20210113  
def main():
    k = int(input())
    str = input()
    r = len(str) // k
    li = [[""]*k for _ in range(r)]
    i = 0; j = 0
    for s in str:
        li[i][j] = s
        if i % 2 == 0:
            if j == k - 1:
                i += 1
            else:
                j += 1
        else:
            if j == 0:
                i += 1
            else:
                j -= 1
    res = ""
    for j in range(k):
        for i in range(r):
            res += li[i][j]
    print(res)
if __name__ == '__main__':
    main()