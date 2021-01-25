#BOJ1181 단어 정렬  20210125
def main():
    n = int(input())
    li = [input() for _ in range(n)]
    li = sorted(li, key = lambda x : (len(x), x))
    dic = {}
    for i in li:
        if not (i in dic):
            print(i)
            dic[i] = 0
if __name__ == '__main__':
    main()