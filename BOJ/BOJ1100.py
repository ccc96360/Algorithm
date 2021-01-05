WHITE = 0
BLACK = 1
def main():
    res = 0
    for i in range(8):
        curState = WHITE if i % 2 == 0 else BLACK
        str = input()
        for s in str:
            if curState == WHITE and s == "F":
                res += 1
            curState = WHITE if curState == BLACK else BLACK
    print(res)

if __name__ == '__main__':
    main()