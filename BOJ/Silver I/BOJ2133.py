#BOJ2133 타일 채우기 20210308
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [0] + [0,3,0]
    sum = 0
    for i in range(4,n+1):
        if i % 2 == 0:
            a = li[i-2] * li[2] + 2 * sum + 2
            sum += li[i-2]
            li.append(a)
        else:
            li.append(0)
    print(li[n])
if __name__ == '__main__':
    main()