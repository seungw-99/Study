'''
Q)  다음처럼 막대그래프를 그려보자.
    무한반복을 진행하다가 -1을 입력하면 프로그램을 종료한다.
    Tip) 막대그래프 표현은 for문을, 무한반복은 while문을 사용해보자.

    ↓ 실행화면 ↓
    숫자를 입력하시오: 5
    *****
    숫자를 입력하시오: 10
    **********
    숫자를 입력하시오: -1
    프로그램을 종료합니다.
'''
while True:
    num = int(input('숫자를 입력하시오: '))
    if num==-1:
        print('프로그램을 종료합니다')
        break
    for i in range(num):
        print('*', end='')
    print()