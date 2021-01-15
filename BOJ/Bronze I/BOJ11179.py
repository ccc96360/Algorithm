#BOJ11179 2진수 뒤집기 20210115
def binToDec(s):
    ret = 0
    cnt = 0
    for i in reversed(s):
        if i == "1": ret += 2 ** cnt
        cnt += 1        
    return ret
def decToBin(n):
    ret = ""
    while n != 0:
        ret += "1" if n % 2 == 1 else "0"
        n //= 2
        
    return "".join(reversed(ret))

def main():
    n = int(input())
    print(binToDec("".join(reversed(decToBin(n)))))
    
if __name__ == '__main__':
    main()