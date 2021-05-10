#BOJ1464 뒤집기 3 20210510
import sys
input = sys.stdin.readline

def main():
    s = input().rstrip()
    n = len(s)
    ans = s[0]
    for i in range(n-1):
        if ans[i] < s[i+1]:
            ans = s[i+1] + ans
        else:
            ans = ans + s[i+1] 
    print("".join(reversed(ans)))
if __name__ == '__main__':
    main()
