def main():
    m = int(input())
    cups = [1, 2, 3]
    for i in range(m):
        a,b = map(int, input().split(" "))
        tmp = cups[a-1]
        cups[a-1] = cups[b-1]
        cups[b-1] = tmp
    for i in range(3):
        if cups[i] == 1:
            print(i+1)

if __name__ == '__main__':
    main()
