#BOJ1463 1로 만들기 20210210 
import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    li = [0,0,1,1]
    for i in range(2,n+1):
        if i == 2 or i == 3: continue
        a = b = c = 10**6 + 1
        if i % 2 == 0:
            a = li[i//2]
        if i % 3 == 0:
            b = li[i//3]
        c = li[i - 1]
        v = min(min(a,b),c) + 1
        li.append(v)
    print(li[n])
if __name__ == '__main__':
    main()