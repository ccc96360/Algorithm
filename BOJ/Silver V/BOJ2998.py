#BOJ2998 8진수 20210124 
def main():
    mapp = {
        "000" : 0,
        "001" : 1,
        "010" : 2,
        "011" : 3,
        "100" : 4,
        "101" : 5,
        "110" : 6,
        "111" : 7,
    }
    n = input()
    i = 3 - (len(n) % 3)
    n = "".join(["0"]*i) + n
    res = ""
    idx = 0; size = len(n)
    while idx < size:
        res += str(mapp[n[idx:idx+3]])
        idx += 3
    print(int(res))
if __name__ == '__main__':
    main()