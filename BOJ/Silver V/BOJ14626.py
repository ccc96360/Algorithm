#BOJ14626 ISBN 20210121  
def main():
    isbn = input()
    odd = True; sum = 0
    isOdd = False
    for i in range(len(isbn)):
        s = isbn[i]
        if s == "*":
            isOdd = odd
            odd = not odd
            continue
        sum += int(s) if odd else int(s) * 3
        odd = not odd 
    for i in range(0,10):
        tmp = sum + i if isOdd else sum + i * 3
        if tmp % 10 == 0: res = i
    print(res)
if __name__ == '__main__':
    main()