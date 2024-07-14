import math, timer


def calculateLog():
    powOf10s = []
    for i in range(0,30):
        powOf10s.append(((pow(10, pow(2,-i)))))
    
    확인횟수 = 0
    정확횟수 = 0
    
    구할로그값 = 1
    while True:
        확인횟수 += 1
        구할로그값 = round(구할로그값 + 0.01, 2)
        나눠질값 = 구할로그값
        로그곱지수목록 = []
        while True:
            for index, powOf10 in enumerate(powOf10s):
                if powOf10 <= 나눠질값:
                    나눠질값 /= powOf10
                    로그곱지수목록.append(round(1/pow(2, index), 8))
                    break
            if 나눠질값 <= powOf10s[-1]:
                break
        로그결과 = round(sum(로그곱지수목록), 4)
        if 로그결과 == round(math.log10(구할로그값), 4):
            정확횟수 += 1
        print(f"log {구할로그값} : {로그결과}")
        if 구할로그값 >= 9.99:
            break
    print(f"정확도 : {round(정확횟수/확인횟수*100, 1)}")

if __name__ == "__main__":
    print(timer.timer(calculateLog, []))






'''
1. 10의 1승, 10의 1/2승, 10의 1/4승 ... 10의 1/1024승을 구한다
2. 알고 있는 값은 10^(2의 거듭제곱)이므로, 10^x가 2인 x를 구하기 위해서는, 1에서 계산한 값들의 곱으로 숫자 2를 표현해야 한다.
3. 2보다 작은 값들 중, 최댓값으로 2를 나누고, 그 해당하는 값을 최대에 해당하는 작은 값으로 나누며 계속해서 반복한다.
4. 과정 1에서 구한 값들로 표현할 수 없을 때, 그 해당 숫자는 1/1024 * k인 비례값으로 계산한다.
'''