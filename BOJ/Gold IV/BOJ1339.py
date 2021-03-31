#BOJ1339 단어 수학 20210331
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [list(input().rstrip()) for _ in range(n)]
    li.sort(key= lambda x: len(x), reverse=True)
    weight = {}
    for v in li:
        size = len(v)
        for s in v:
            if s not in weight:
                weight[s] = 10**(size-1)
            else:
                weight[s] += 10**(size-1)
            size -= 1
    weight = sorted(weight.items(), reverse=True, key = lambda x: x[1])
    num = 9
    dic = {}
    for s,_ in weight:
        if s not in dic:
            dic[s] = num
            num -= 1
    sum = 0
    for i in range(n):
        li[i] = list(map(lambda x: str(dic[x]), li[i]))
        sum += int("".join(li[i]))
    print(sum)
if __name__ == '__main__':
    main()