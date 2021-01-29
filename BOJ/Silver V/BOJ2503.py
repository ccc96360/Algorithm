#BOJ2503 숫자 야구 20210129 
import sys
from itertools import permutations
input = sys.stdin.readline

def judge(a,b):
    s = 0
    ball = 0
    a = str(a)
    b = str(b)
    for i in range(3):
        for j in range(3):
            if b[i] == a[j]:
                if i == j:
                    s += 1
                else:
                    ball += 1
            
    return s,ball
def main():
    num = ["1","2","3","4","5","6","7","8","9"]
    c = list(map("".join, permutations(num,3)))
    c = list(map(int,c))
    while c[0] < 100: del c[0]
    li = []
    for _ in range(int(input())):
        n, s, b = map(int, input().split(" "))
        tmpSet = set()
        for i in c:
            ts,tb = judge(i,n)
            if s == ts and b == tb:
                tmpSet.add(i)
        li.append(tmpSet)
    res = li[0]
    for i in range(1, len(li)):
        res = res & li[i]
    print(len(res))
if __name__ == '__main__':
    main()