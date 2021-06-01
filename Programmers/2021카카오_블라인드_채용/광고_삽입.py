def timeToSec(time):
    h,m,s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s

def itos(n):
    return ("%2d" % n).replace(" ", "0")

def secToTime(sec):
    h = sec // 3600
    sec %= 3600
    m = sec // 60
    sec %= 60
    return "{0}:{1}:{2}".format(itos(h), itos(m), itos(sec))

def solution(play_time, adv_time, logs):
    playTime = timeToSec(play_time)
    advTime = timeToSec(adv_time)
    views = [0] * (playTime + 1)
    for v in logs:
        s,e = map(timeToSec, v.split("-"))
        views[s] += 1
        views[e] -= 1
    
    for i in range(playTime):
        views[i+1] = views[i] + views[i+1] 

    cummulativeViews = [0] * (playTime + 1)
    cummulativeViews[0] = views[0]
    for i in range(playTime):
        cummulativeViews[i+1] = views[i+1] + cummulativeViews[i]
    
    mx = 0
    answer = ""
    for i in range(playTime-advTime+1):
        tmp = cummulativeViews[i+advTime-1] - cummulativeViews[i] + views[i]
        if mx < tmp:
            mx = tmp
            answer = secToTime(i)
    print(cummulativeViews[timeToSec("00:59:59")],cummulativeViews[timeToSec("25:59:59")])
    print(cummulativeViews[timeToSec("01:00:00")],cummulativeViews[timeToSec("26:00:00")])
    return answer

def main():
    play_time = "99:59:59"
    adv_tim = 	"25:00:00"
    logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    print(solution(play_time, adv_tim, logs))
if __name__ == '__main__':
    main()