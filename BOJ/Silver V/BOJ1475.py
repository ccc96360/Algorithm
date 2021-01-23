#BOJ1475 방번호 20210123
from math import ceil
def main():
    n = input()
    dic = {str(i) : 0 for i in range(0,10)}
    for s in n:
        dic[s] += 1
    max = 0
    for k,v in dic.items():
        if k == "6" or k == "9": continue
        if v > max:
            max = v
    sn = int(ceil((dic["6"] + dic["9"]) / 2))
    print(max if max > sn else sn)
if __name__ == '__main__':
    main()