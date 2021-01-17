#BOJ8979  올림픽 20210117
from operator import itemgetter

def main():
    n, target = map(int, input().split(" "))
    li = [list(map(int, input().split(" "))) for _ in range(n)]
    li.sort(key = itemgetter(1,2,3), reverse= True)
    rank = 1
    g = li[0][1]
    s = li[0][2]
    b = li[0][3]
    cnt = 1
    for i in range(1, n):
        gold = li[i][1]
        silver = li[i][2]
        bronze = li[i][3] 
        if g == gold:
            if s == silver:
                if b != bronze:
                    rank += cnt
                    b = bronze
                else: cnt += 1
            elif s != silver:
                rank += cnt
                s,b = silver,bronze
                cnt = 1
        elif g != gold:
            g,s,b = gold,silver,bronze
            rank += cnt
            cnt = 1
        if li[i][0] == target: break
    print(rank if li[0][0] != target else 1)

                
        
if __name__ == '__main__':
    main()