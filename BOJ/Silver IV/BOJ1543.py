#BOJ1543 문서 검색 20210208 
import sys
input = sys.stdin.readline

def main():
    s = input().rstrip()
    t = input().rstrip()
    s = s.split(t)
    print(len(s)-1)
if __name__ == '__main__':
    main()