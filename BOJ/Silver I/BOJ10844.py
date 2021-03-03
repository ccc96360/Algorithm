#BOJ10844 쉬운 계단 수 20210303
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    prev = [0,0] + [1]*9 + [0]
    cur = [0,0] + [0] * 9 + [0]
    for i in range(1,n):
        for j in range(1,11):
            cur[j] = prev[j-1]+prev[j+1]
        for j in range(1,11):
            prev[j] = cur[j]
    print(sum(prev)%1000000000)
if __name__ == '__main__':
    main()