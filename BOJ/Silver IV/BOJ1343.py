#BOJ1343 폴리오미노 20210206  
import sys
input = sys.stdin.readline

def main():
    a = "AAAA";b = "BB"
    s = input().rstrip()
    li = s.split(".")
    res = ""
    for s in li:
        n = len(s)
        res += "."
        if n % 2 == 0:
            res += a * (n // 4)
            if n % 4 != 0: res += b
        else:
            return print(-1)
    print(res[1:])

if __name__ == '__main__':
    main()