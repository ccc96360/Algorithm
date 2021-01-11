import datetime

def main():
    y, m, d = map(int, input().split(" "))
    date = datetime.date(y, m ,d)
    y, m, d = map(int, input().split(" "))
    date2 = datetime.date(y, m ,d)
    res = str(date2-date).split(" ")
    if date2.year-date.year>=1000 and date2.month - date.month>=0 and date2.day - date.day >= 0:
        print("gg")
    else:
        print("D-", res[0], sep = "")
if __name__ == '__main__':
    main()