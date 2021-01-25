#BOJ7568 덩치 20210125
def comp(a,b):
    return True if a[0] < b[0] and a[1] < b[1] else False
def main():
    li = []
    n = int(input())
    for _ in range(n): li.append(list(map(int, input().split(" "))))
    res = [1]  * n
    for i in range(0, n):
        for j in range(0,n):
            if j == i : continue
            if comp(li[i], li[j]): res[i] += 1
    for i in res : print(i, end = " ")

if __name__ == '__main__':
    main()