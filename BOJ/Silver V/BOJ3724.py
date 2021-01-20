#BOJ3724 표 20210120
class BigInteger:
    b = 10000000
    def __init__(self, *args):
        size = len(args); n = int(args[0])
        self.sign = "+" if n >= 0 else "-"
        n = abs(n)
        self.big = int(args[0]) if size == 3 else n // BigInteger.b
        self.small = int(args[1]) if size == 3 else n % BigInteger.b
        if size == 3: self.sign = args[2]
    def __mul__(self, other):
        big = self.big * other.big * BigInteger.b + self.big * other.small + self.small * other.big
        small = self.small * other.small
        big += small // BigInteger.b
        small = small % BigInteger.b
        sign = "+" if self.sign == other.sign else "-" 
        return BigInteger(big, small, sign)
    def __lt__(self, other):
        if self.big == other.big:
            return self.small < other.small
        return self.big < other.big
    def __le__(self, other):
        if self.sign == other.sign:
            if self.sign == "+":
                if self.big == other.big:
                    return self.small <= other.small
                return self.big <= other.big
            else:
                if self.big == other.big:
                    return self.small >= other.small
                return self.big >= other.big
        else:
            return True if self.sign == "-" else False
    def __str__(self):
        ret = str(self.big)
        n = len(str(self.small))    
        zero = "".join(["0"]*((len(str(BigInteger.b)) - n - 1)))
        sign = "" if self.sign == "+" else "-"
        return sign + ret + zero +  str(self.small)
def main():
    for __ in range(int(input().rstrip())):
        m, n  = map(int,input().rstrip().split(" "))
        li = [list(map(BigInteger, input().rstrip().split(" "))) for _ in range(n)]
        max = BigInteger(1)
        ret = 1
        for i in range(n): max = max * li[i][0]
        for i in range(1,m):
            tmp = BigInteger(1)
            for j in range(n): tmp = tmp * li[j][i]
            if max <= tmp:
                max = tmp
                ret = i + 1
        print(ret)
    
if __name__ == '__main__':
    main()