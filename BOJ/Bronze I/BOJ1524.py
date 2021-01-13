#BOJ1524 세준세비 20210113
def main():
    tc = int(input())
    for ___ in range(tc):
        input()
        n,m = map(int, input().rstrip().split(" "))
        s = list(map(int, input().rstrip().split(" ")))
        b = list(map(int, input().rstrip().split(" ")))
        s.sort(); b.sort()
        i = 0; j = 0
        while True:
            if i == n or j == m:
                winner = "B" if i==n else "S"
                break
            if s[i] < b[j]:
                i += 1
            else:
                j += 1
        print(winner)

if __name__ == '__main__':
    main()