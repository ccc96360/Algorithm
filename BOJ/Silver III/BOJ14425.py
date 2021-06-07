#BOJ14425 문자열 집합 20210607
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    set_ = set([input().rstrip() for _ in range(n)])
    s = [input().rstrip() for _ in range(m)]
    print(len(list(filter(lambda x: x in set_, s))))
if __name__ == '__main__':
    main()