#BOJ1205 등수 구하기 20210202
import sys
input = sys.stdin.readline

def main():
    n, score, p = map(int, input().rstrip().split(" "))
    if n > 0:
        li = list(map(int, input().rstrip().split(" ")))
        rank = 1
        for i in range(len(li)):
            if li[i] > score:
                rank += 1
            else:
                break
        print(-1 if n == p and li[n-1] >= score else rank)
    else:
        print(1)
if __name__ == '__main__':
    main()