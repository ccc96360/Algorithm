#BOJ1931 회의실 배정 20210224
import sys
input = sys.stdin.readline

def main():
    li = []
    for _ in range(int(input())):
        li.append(list(map(int, input().rstrip().split())))
    li = sorted(li, key=lambda x: (x[1],x[0]))
    min_ =li[0][1]
    cnt = 1
    for i in range(1,len(li)):
        s,e =li[i][0],li[i][1]
        if s >= min_:
            min_ = e
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()