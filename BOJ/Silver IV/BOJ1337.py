#BOJ1377 올바른 배열 20210205
import sys
input = sys.stdin.readline

def main():
    li = [int(input().rstrip()) for _ in range(int(input().rstrip()))]
    li.sort()
    dic = {i : True for i in li}
    min_ = 5
    for i in li:
        cnt = 0
        for j in range(i,i+5):
            if j not in dic:
                cnt += 1
        min_ = min(min_,cnt)
    print(min_)
if __name__ == '__main__':
    main()