basicNumber = 1.0001

def logCalculator(number, accuracy):
    count = 0
    result = accuracy
    while True:
        count += 1
        result *= accuracy
        if result >= number:
            return count

basic10Count = logCalculator(10, basicNumber)
count = 1
while True:
    count += 0.01
    print(f"log {round(count, 2)} : {logCalculator(round(count, 2), basicNumber)/basic10Count}")
    if count >= 10:
        break