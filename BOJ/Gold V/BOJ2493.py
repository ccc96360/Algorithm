#BOJ2493 탑 20210321
import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    li = list(map(int,input().rstrip().split()))
    res = [0] * n
    taller = [[li[0],1]]
    for i in range(1,n):
        while taller and taller[-1][0] < li[i]:
            taller.pop()
        if not taller or taller[-1][0] > li[i]:
            if taller : res[i] = taller[-1][1]
            taller.append([li[i],i+1])
    print(*res)
if __name__ == '__main__':
    main()