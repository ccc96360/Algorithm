class Student:
    def __init__(self, gradeList, num):
        self.gradeList = gradeList
        self.num = num
        self.cnt = 0
    def existSameGrade(self, otherSt):
        for i in range(5):
            if self.gradeList[i] == otherSt.gradeList[i]:
                return True
        return False
    def __lt__(self, other):
        return self.cnt > other.cnt

def main():
    n = int(input())
    arr = [Student(input().split(" "), i+1) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if arr[i].existSameGrade(arr[j]):
                arr[i].cnt += 1
    sArr = sorted(arr)
    print(sArr[0].num)

if __name__ == '__main__':
    main()