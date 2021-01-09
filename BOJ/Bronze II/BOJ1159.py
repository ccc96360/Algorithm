def main():
    n = int(input())
    map = {}
    for i in range(n):
        str = input()
        if str[0] in map:
            map[str[0]] += 1
        else:
            map[str[0]] = 1
    res = ""
    sMap = sorted(map.items())
    for i in sMap:
        if i[1] >= 5:
            res += i[0]
    print(res if len(res) != 0 else "PREDAJA")

if __name__ == '__main__':
    main()
