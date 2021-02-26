#BOJ1541 잃어버린 괄호 20210226
import sys
input = sys.stdin.readline

def main():
    s = input().rstrip()
    li = s.split("-")
    n = len(li)
    for i in range(n):
        v = li[i]
        if v.find("+") != -1:
            li[i] = sum(list(map(int, v.split("+"))))
        else: li[i] = int(li[i])
    res = li[0] - sum(li[1:])
    print(res)
if __name__ == '__main__':
    main()