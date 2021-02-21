#BOJ10974 모든 순열 20210221
import sys
from itertools import permutations
input = sys.stdin.readline

def main():
    li = [i+1 for i in range(int(input().rstrip()))]
    for v in list(permutations(li)):
        print(*v)

if __name__ == '__main__':
    main()