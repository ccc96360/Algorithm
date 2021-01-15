#BOJ2033 반올림 20210115
def main():
    n = int(input())
    tmp = 1
    cnt = 0
    while n>10:
        cnt += 1
        mod = n % 10
        n = n // 10
        if mod >= 5 : n += 1
    print(n*(10**cnt))

if __name__ == '__main__':
    main()