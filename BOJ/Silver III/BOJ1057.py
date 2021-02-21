#BOJ1057 토너먼트 20210221
import sys
input = sys.stdin.readline

def main():
    n, lim, kim = map(int, input().rstrip().split())
    li = [i+1 for i in range(n)]
    round = 0; meet = False
    while not meet:
        round += 1
        li2 = []
        n = len(li)
        for i in range(0,n,2):
            if i == n-1: li2.append(li[i]) 
            elif li[i] == lim and li[i+1] == kim:
                meet = True
                break
            elif li[i+1] == lim and li[i] == kim:
                meet = True
                break
            elif lim in [li[i],li[i+1]]:
                li2.append(lim)
            elif kim in [li[i],li[i+1]]:
                li2.append(kim)
            else:
                li2.append(li[i])
        li = li2
    print(round)

if __name__ == '__main__':
    main()