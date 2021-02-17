#BOJ17390 이건 꼭 풀어야 해! 20210217
import sys
input = sys.stdin.readline

def main():
    n,q = map(int,input().rstrip().split(" "))
    li = sorted(map(int,input().rstrip().split(" ")))
    sum, idx = 0, 1
    sums = [0]
    for v in li:
        sum += v
        sums.append(sum)
    for _ in range(q):
        l,r = map(int,input().rstrip().split())
        print(sums[r]-sums[l-1])
if __name__ == '__main__':
    main()