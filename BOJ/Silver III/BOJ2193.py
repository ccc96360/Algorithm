#BOJ2193 이친수 20210215
import sys
input = sys.stdin.readline

def main():
    li = [1,1]
    for i in range(2,90):
        li.append(li[i-1] + li[i-2])
    print(li[int(input()) - 1])
if __name__ == '__main__':
    main()