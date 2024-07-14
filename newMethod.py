import math, timer

def calculateLog():
    count = 1
    while True:
        count = round(count+0.01, 4)
        a0 = 10
        a1 = count
        nList = []

        for i in range(10):
            i = 0
            while True:
                if pow(a1, i) <= a0 and pow(a1, i+1) >= a0:
                    nList.append(i)
                    break
                i += 1
            temp = a0
            a0 = a1
            a1 = temp/pow(a1, i)

        temp = 1/nList[-1]
        for i in range(2, len(nList)+1):
            result = 1/(temp + nList[-i])
            temp = result
        print(f"log {count} : {round(result, 4)}")
        if count >= 9.99:
            break
        
print(timer.timer(calculateLog, []))