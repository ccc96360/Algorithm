import sys
INF = sys.maxsize
def rotate(li, l, r, mn):
    lr, lc = l
    rr, rc = r

    tmp = li[lr][rc]
    for i in range(rc,lc,-1):
        li[lr][i] = li[lr][i-1]
        mn = min(li[lr][i], mn)

    tmp2 = li[rr][rc]
    for i in range(rr, lr, -1):
        li[i][rc] = li[i-1][rc]
        mn = min(li[i][rc], mn)
    mn = min(tmp, mn)
    li[lr+1][rc] = tmp

    tmp = li[rr][lc]
    for i in range(lc,rc):
        li[rr][i] = li[rr][i+1]
        mn = min(li[rr][i], mn)
    mn = min(tmp2, mn)
    li[rr][rc-1] = tmp2

    for i in range(lr, rr):
        li[i][lc] = li[i+1][lc]
        mn = min(li[i][lc], mn)
    mn = min(tmp, mn)
    li[rr-1][lc] = tmp

    return mn


def solution(rows, columns, queries):
    answer = []
    li = [[i+j*columns for i in range(1,columns+1)] for j in range(rows)]
    li = [[j+i*columns for j in range(1,columns+1)] for i in range(rows)]
    for v in queries:
        lr,lc,rr,rc = map(lambda x: x-1, v)
        mn = INF
        answer.append(rotate(li, (lr, lc), (rr, rc), mn))
        for v2 in li:
            print(v2)

    return answer

def main():
    rows = 6
    columns = 6
    queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
    print(solution(rows, columns, queries))
if __name__ == '__main__':
    main()