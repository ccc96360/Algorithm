#BOJ1977 완전제곱수 20210114
def main():
    arr = [int(input()) for _ in range(2)]
    li = []
    for i in range(arr[0], arr[1]+1):
        if ((i ** 0.5) * 10) % 10 == 0:
            li.append(i)
    if len(li) == 0:
        return print(-1)
    print(sum(li), li[0], sep = "\n")
if __name__ == '__main__':
    main()