#BOJ10610 30 20210127
def main():
    n = input()
    n = sorted(n, reverse=True)
    sum = 0
    for i in n : sum += int(i)
    if sum % 3 == 0 and n[-1] == "0":
        print("".join(n))
    else:
        print(-1)
if __name__ == '__main__':
    main()