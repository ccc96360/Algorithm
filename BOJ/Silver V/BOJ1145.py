#BOJ1145 적어도 대부분의 배수 20210116  
def main():
    li = list(map(int, input().split()))
    li.sort()
    s = li[2]
    while True:
        cnt = 0
        for i in li:
            if s%i == 0: cnt += 1
        if cnt >= 3:
            break
        s += 1
    print(s)

if __name__ == '__main__':
    main()