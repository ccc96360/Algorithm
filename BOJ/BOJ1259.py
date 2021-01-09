def main():
    while True:
        s = input()
        if s == "0": break
        print("yes" if s == "".join(reversed(s)) else "no")

if __name__ == '__main__':
    main()