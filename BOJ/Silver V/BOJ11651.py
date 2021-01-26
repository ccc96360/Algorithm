#BOJ11651 좌표 정렬하기2 20210126 
def main():
    li = [list(map(int, input().split(" "))) for _ in range(int(input()))]
    li = sorted(li, key = lambda x : (x[1],x[0]))
    for i in range(len(li)) : print(li[i][0],li[i][1])
if __name__ == '__main__':
    main()