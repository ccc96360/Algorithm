#BOJ 1453 피시방 알바 20210112
def main():
    n = int(input())
    li = map(int, input().split(" "))
    canSeat = {i : True for i in range(1,101)}
    refuse = 0
    for i in li:
        if canSeat[i]:
            canSeat[i] = False
        else:
            refuse += 1
    print(refuse)
if __name__ == '__main__':
    main()