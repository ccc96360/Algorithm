
LEFT = "left"
RIGHT = "right"

def getDistance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def solution(numbers, hand):
    answer = ''
    rows = {1:0, 2:0, 3:0, 4:1, 5:1, 6:1, 7:2, 8:2, 9:2, 0:3}
    cols = {1:0, 2:1, 3:2, 4:0, 5:1, 6:2, 7:0, 8:1, 9:2, 0:1}
    
    leftThumb = (3, 0)
    rightThumb = (3, 2)
    for v in numbers:
        r,c = rows[v],cols[v]
        tmp = ""
        if v in [1,4,7]:
            tmp = "L"
        elif v in [3,6,9]:
            tmp = "R"
        else:
            ld = getDistance((r,c), leftThumb)
            rd = getDistance((r,c), rightThumb)
            if ld == rd:
                tmp = "L" if hand == LEFT else "R"
            elif ld < rd:
                tmp = "L"
            else:
                tmp = "R"
        answer += tmp
        if tmp == "L":
            leftThumb = (r,c)
        else:
            rightThumb = (r,c)
    return answer