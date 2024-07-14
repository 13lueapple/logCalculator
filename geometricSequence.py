import math, timer

소숫점자릿수 = 3
def calculateLog():
    global 공비
    공비 = 1.0001
    

    def logCalculator(로그몇, 공비):
        지수 = 0
        등비현재항 = 공비
        while True:
            지수 += 1
            등비현재항 *= 공비
            if 등비현재항 >= 로그몇:
                return 지수

    로그10지수 = logCalculator(10, 공비)
    로그몇 = 1
    정확횟수 = 0
    확인횟수 = 0
    while True:
        확인횟수 += 1
        로그몇 = round(로그몇 + 0.01, 2)
        로그결과 = round(logCalculator(로그몇, 공비)/로그10지수, 소숫점자릿수)
        if 로그결과 == round(math.log10(로그몇), 소숫점자릿수):
            정확횟수 += 1
        print(f"log {로그몇} : {로그결과}")
        if 로그몇 >= 10:
            break

    print(f"{round(정확횟수/확인횟수*100, 1)}")
    
print(round(timer.timer(calculateLog, []), 3))
print(공비)
print(소숫점자릿수)