#BOJ1292 쉽게 푸는 문제 20210204  
import sys
input = sys.stdin.readline

def main():
    cnt = 0
    li = []
    num = 1
    while cnt < 1000:
        for i in range(num):
            li.append(num)
            cnt += 1
            if cnt >= 1000: break
        num += 1
    a,b = map(int,input().rstrip().split(" "))
    print(sum(li[a-1:b]))
if __name__ == '__main__':
    main()