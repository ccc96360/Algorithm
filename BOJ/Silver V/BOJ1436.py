#BOJ1436 영화감독 숌 20210126
def main():
    n = int(input())
    cnt = 0; res = ""
    num = 666
    while True:
        if str(num).find("666") != -1:
            cnt += 1
            res = str(num)
        if cnt == n: break
        num += 1
    print(res)
if __name__ == '__main__':
    main()