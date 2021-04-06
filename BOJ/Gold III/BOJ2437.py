#BOJ2437 저울 20210406
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = sorted(map(int,input().rstrip().split()))
    sum_ = 0
    for v in li:
        if v > sum_ + 1:
            break
        else:
            sum_ += v
    print(sum_+1)        
if __name__ == '__main__':
    main()