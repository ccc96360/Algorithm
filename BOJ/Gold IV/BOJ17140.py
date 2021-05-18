#BOJ17140 이차원 배열과 연산 20210518
import sys
input = sys.stdin.readline

def transpose(li):
    return list(map(list, zip(*li)))

def preProcess(li):
    dic = {}
    for v in li:
        if v == 0: continue
        if v not in dic:
            dic[v] = 1
        else:
            dic[v] += 1
    ret = list(dic.items())
    ret.sort(key = lambda x : (x[1],x[0]))
    return ret

def opR(li):
    ret = []
    maxColSize = 0 
    for row in li:
        tmp = preProcess(row)
        csize =  0
        tmp2 = []
        for v,cnt in tmp:
            tmp2.extend([v,cnt])
            csize += 2
            if csize >= 100: break
        ret.append(tmp2)
        maxColSize = max(maxColSize, csize)

    for row in ret:
        size = len(row)
        while size < maxColSize:
            size += 1
            row.append(0)
        
    return ret, maxColSize

def opC(li):
    liT = transpose(li)
    liT, rowSize = opR(liT)
    return transpose(liT), rowSize

def main():
    r,c,k = map(lambda x: int(x)-1, input().rstrip().split())
    k += 1
    li = [list(map(int,input().rstrip().split())) for _ in range(3)]
    rSize = cSize = 3
    time = 0
    while time <= 100:
        if 0 <= r < rSize and 0 <= c < cSize:
            if li[r][c] == k:
                return print(time)
        time += 1
        if rSize >= cSize:
            li, cSize = opR(li)
        else:
            li, rSize = opC(li)
    print(-1)
    
if __name__ == '__main__':
    main()