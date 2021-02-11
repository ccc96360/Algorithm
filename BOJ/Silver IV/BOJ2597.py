#BOJ2597 줄자접기 20210211
import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    li = [sorted(list(map(int, input().rstrip().split(" ")))) for _ in range(3)]
    l = 0; r = n
    for i in range(3):
        if li[i][0] == li[i][1]: continue
        mid = sum(li[i]) / 2
        if li[i][0] - l <= r - li[i][1]:
            li[i][0] = li[i][1]
            l = mid
            for j in range(i+1,3):
                for k in range(2):
                    if li[j][k] < mid:
                        tmp = mid-li[j][k]
                        li[j][k] = int(mid + tmp)
        else:
            li[i][1] = li[i][0]
            r = mid
            for j in range(i+1,3):
                for k in range(2):    
                    if li[j][k] > mid:
                        tmp = li[j][k]-mid
                        li[j][k] = int(mid - tmp)
    print(r-l)
if __name__ == '__main__':
    main()