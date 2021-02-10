#BOJ9095 1,2,3 더하기 20210210 
import sys
input = sys.stdin.readline

def main():
    for __ in range(int(input().rstrip())):
        li = [0,1,2,4]
        n = int(input().rstrip())
        for i in range(1,n+1):
            if i < 4: continue
            li.append(li[i-1] + li[i-2] + li[i-3])
        print(li[n])
if __name__ == '__main__':
    main()