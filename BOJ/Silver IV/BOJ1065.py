#BOJ1065 한수 20210130
import sys
input = sys.stdin.readline

def judge(n):
    m = str(n)
    a = int(m[1]) - int(m[0])
    for i in range(len(m)):
        if i <= 1 : continue
        if int(m[i]) - int(m[i-1]) != a:
            return False
    return True

def main():
    n = int(input()); cnt = 0
    for i in range(1,n+1):
        if i < 100: cnt += 1
        elif judge(i): cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()