#BOJ5555 반지 20210121
def main():
    s = input(); res = 0
    for _ in range(int(input())):
        tmp = input() * 2
        if tmp.find(s) != - 1: res += 1
    print(res)
if __name__ == '__main__': 
    main()