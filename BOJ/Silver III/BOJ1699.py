#BOJ1699 제곱수의 합 20210219
import sys
input = sys.stdin.readline

def main():
    dic = {}
    n = 1
    while n ** 2 <= 100000:
        dic[n**2] = 1
        n += 1
    bases = []
    for i in range(1,100001):
        if i in dic:
            bases.append(i)
            continue
        min_ = 100000; base = 0
        for v in bases:
            if min_ > dic[i-v]:
                min_ = dic[i-v]
                base = v
        dic[i] = dic[base]+dic[i-base]
    print(dic[int(input())])
if __name__ == '__main__':
    main()