#BOJ14500 테트로미노 20210314
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().rstrip().split())
    li = [list(map(int , input().rstrip().split())) for _ in range(n)]
    max_ = 0
    for i in range(n):
        for j in range(m):
            #length = 4
            if 0 <= j+3 < m:
                max_ = max(max_, li[i][j] + li[i][j+1] + li[i][j+2] + li[i][j+3])
            if 0 <= j-3 < m:
                max_ = max(max_, li[i][j] + li[i][j-1] + li[i][j-2] + li[i][j-3])       
            #length = 3
            if 0 <= j + 2 < m:
                base = li[i][j] + li[i][j+1] + li[i][j+2]
                for k in range(3):
                    if 0 <= i + 1 < n:
                        max_ = max(max_, base + li[i+1][j+k])
                    if 0 <= i - 1 < n:
                        max_ = max(max_, base + li[i-1][j+k])
            if 0 <= j - 2 < m:
                base = li[i][j] + li[i][j-1] + li[i][j-2]
                for k in range(3):
                    if 0 <= i + 1 < n:
                        max_ = max(max_, base + li[i+1][j-k])
                    if 0 <= i - 1 < n:
                        max_ = max(max_, base + li[i-1][j-k])
            #length = 2
            if 0 <= j + 1 < m:
                base = li[i][j] + li[i][j+1]
                if 0 <= i + 1 < n:
                    max_ = max(max_, base + li[i+1][j] + li[i+1][j+1])
                    if 0 <= j - 1 < m:
                        max_ = max(max_, base + li[i+1][j-1] + li[i+1][j])
                    if 0 <= j + 2 < m:
                        max_ = max(max_, base + li[i+1][j+1] + li[i+1][j+2])
                if 0 <= i - 1 < n:
                    max_ = max(max_, base + li[i-1][j] + li[i-1][j+1])
                    if 0 <= j - 1 < m:
                        max_ = max(max_, base + li[i-1][j-1] + li[i-1][j])
                    if 0 <= j + 2 < m:
                        max_ = max(max_, base + li[i-1][j+1] + li[i-1][j+2])
                if 0 <= i + 2 < n:
                    for k in range(2):
                        max_ = max(max_, base + li[i+1][j+k] + li[i+2][j+k])
                if 0 <= i - 2 < n:
                    for k in range(2):
                        max_ = max(max_, base + li[i-1][j+k] + li[i-2][j+k])
            if 0 <= j - 1 < m:
                base = li[i][j] + li[i][j-1]
                if 0 <= i + 1 < n:
                    max_ = max(max_, base + li[i+1][j] + li[i+1][j-1])
                    if 0 <= j + 1 < m:
                        max_ = max(max_, base + li[i+1][j+1] + li[i+1][j])
                    if 0 <= j - 2 < m:
                        max_ = max(max_, base + li[i+1][j-1] + li[i+1][j-2])
                if 0 <= i - 1 < n:
                    max_ = max(max_, base + li[i-1][j] + li[i-1][j-1])
                    if 0 <= j + 1 < m:
                        max_ = max(max_, base + li[i-1][j+1] + li[i-1][j])
                    if 0 <= j - 2 < m:
                        max_ = max(max_, base + li[i-1][j-1] + li[i-1][j-2])
                if 0 <= i + 2 < n:
                    for k in range(2):
                        max_ = max(max_, base + li[i+1][j-k] + li[i+2][j-k])
                if 0 <= i - 2 < n:
                    for k in range(2):
                        max_ = max(max_, base + li[i-1][j-k] + li[i-2][j-k])

            #length = 1
            if 0 <= i + 2 < n:
                base = li[i][j] + li [i+1][j]
                if 0 <= j + 1 < m:
                    max_ = max(max_, base + li[i+1][j+1] + li[i+2][j+1])
                    max_ = max(max_, base + li[i+1][j+1] + li[i+2][j])
                if 0 <= j - 1 < m:
                    max_ = max(max_, base + li[i+1][j-1] + li[i+2][j-1])
                    max_ = max(max_, base + li[i+1][j-1] + li[i+2][j])
            if 0 <= i - 2 < n:
                base = li[i][j] + li [i-1][j]
                if 0 <= j + 1 < m:
                    max_ = max(max_, base + li[i-1][j+1] + li[i-2][j+1])
                    max_ = max(max_, base + li[i-1][j+1] + li[i-2][j])
                if 0 <= j - 1 < m:
                    max_ = max(max_, base + li[i-1][j-1] + li[i-2][j-1])
                    max_ = max(max_, base + li[i-1][j-1] + li[i-2][j])
            if 0 <= i + 3 < n:
                max_ = max(max_ , li[i][j] + li[i+1][j] + li[i+2][j] + li[i+3][j])
            if 0 <= i - 3 < n:
                max_ = max(max_ , li[i][j] + li[i-1][j] + li[i-2][j] + li[i-3][j])
    print(max_)  
if __name__ == '__main__':
    main()