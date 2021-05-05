#BOJ13904 과제 20210505
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    li.sort(key = lambda x : x[0])
    days = [0] * 1001
    for day, score in li:
        if days[day] == 0:
            days[day] = score
        else:
            mn = 101
            idx = day
            for i in range(1,day+1):
                if mn > days[i]:
                    mn = days[i]
                    idx = i
            if mn < score:
                days[idx] = score
    print(sum(days))

if __name__ == '__main__':
    main()