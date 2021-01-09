def main():
    arr = input().split(" ")
    res = len(arr) if arr[0] != '' and arr[-1] != '' else len(arr) - 1 if not (arr[0] == '' and arr[-1] == '') else len(arr) - 2 
    print(res)    
if __name__ == '__main__':
    main() 
