#BOJ9012 괄호 20210131  
import sys
input = sys.stdin.readline

def main():
    for __ in range(int(input())):
        word = input().rstrip()
        left = 0
        for s in word:
            left += 1 if s == "(" else -1
            if left < 0: break
        print("YES" if left == 0 else "NO")
        
if __name__ == '__main__':
    main()