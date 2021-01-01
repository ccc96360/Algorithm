def main():
    while True:
        str = input()
        n = [int(i) for i in str]
        if n[0] == 0:
            break
        res = 1
        for i in n:
            if i == 1:
                res += 3
            elif i == 0:
                res += 5
            else:
                res += 4
        print(res)
        
if __name__ == '__main__':
    main()

# N자리 정수를 쪼개서 각각 리스트에 넣는 방법
#       str = input()
#       n = [int(i) for i in str]