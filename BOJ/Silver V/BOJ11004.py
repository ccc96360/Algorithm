#BOJ11004 K번째 수  20210127
def main():
    n,k = map(int, input().split(" "))
    li = list(map(int, input().split(" ")))
    li.sort()
    print(li[k-1])
if __name__ == '__main__':
    main()