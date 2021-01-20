#BOJ9627 문장 20210120
mDict = {
    0 : "",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    100 : "onehundred",
    200 : "twohundred",
    300 : "threehundred",
    400 : "fourhundred",
    500 : "fivehundred",
    600 : "sixhundred",
    700 : "sevenhundred",
    800 : "eighthundred",
    900 : "ninehundred"
}
def main():
    size = 0; res = ""; li = []
    for __ in range(int(input())):
        s = input()
        li.append(s)
        if s != "$":
            size += len(s)
    for i in range(1, 1000):
        if i <= 20:
            if i == len(mDict[i]) + size:
                res = mDict[i]
                break
        elif i < 100:
            a = i // 10 * 10
            b = i % 10
            if i == len(mDict[a]) + len(mDict[b]) + size:
                res = mDict[a] + mDict[b]
                break
        elif i < 1000:
            a = i // 100 * 100
            b = (i % 100) // 10 * 10 if i % 100 > 20 else i % 100
            c = i % 10 if i % 100 > 20 else 0
            if i == len(mDict[a]) + len(mDict[b]) + len(mDict[c]) + size:
                res = mDict[a] + mDict[b] + mDict[c]
                break
    print(" ".join(li).replace("$",res))
if __name__ == '__main__':
    main()