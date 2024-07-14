import math, timer


def calculateLog():
    count = 1
    while True:
        count = round(count+0.01, 2)
        print(f'log {count} : {round(math.log(count),4)}')
        if count >= 10:
            break
        
print(timer.timer(calculateLog, []))