#BOJ1476 날짜 계산 20210119 
def main():
    e, s, m = map(int, input().split(" "))
    ans = 1
    if e == 15: e = 0
    if s == 28: s = 0
    if m == 19: m = 0
    while not(ans % 15 == e and ans % 28 == s and ans % 19 == m): ans += 1
    print(ans)
if __name__ == '__main__':
    main()