#BOJ1003 피보나치 함수 20210210 
import sys
input = sys.stdin.readline

def main():
    li = [(1,0), (0,1)]
    for i in range(2,41):
        li.append((li[i-2][0]+li[i-1][0], li[i-2][1]+li[i-1][1]))
    for _ in range(int(input().rstrip())):
        print(*li[int(input().rstrip())])
if __name__ == '__main__':
    main()