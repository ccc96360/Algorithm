#BOJ1213 펠린드롬 만들기 20210203  
import sys
input = sys.stdin.readline

def main():
    dic = {chr(i) : 0 for i in range(ord("A"), ord("Z")+1)}
    str_ = input().rstrip()
    for s in str_:
        dic[s] += 1
    left = ""; right = ""; center =""
    cnt = 0
    for k,v in dic.items():
        left = left + k * (v//2)
        right = k * (v//2) + right
        if v % 2 != 0:
            cnt += 1 
            if cnt >= 2: return print("I'm Sorry Hansoo")
            center += k
    print(left+center+right)
if __name__ == '__main__':
    main()