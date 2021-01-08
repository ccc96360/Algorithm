def decToBin(a):
    if a == 0: return "0"
    ret = ""
    while a != 0:
        ret = str(a%2) + ret
        a = a//2
    return ret

def binToDec(a):
    n = len(a) - 1
    ret = 0
    for i in a:
        if i == "1":
            ret += 2 ** n
        n -= 1
    return ret

def main():
    a,b = input().split(" ")
    print(decToBin(binToDec(a) + binToDec(b)))
if __name__ == '__main__':
    main()