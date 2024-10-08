'''
CodeUp 1577:
    이 문제는 절댓값 함수를 구현하는 문제입니다.
    다음 조건을 참고해서 함수를 선언하고 호출하여 절댓값을 구해보시오.
    함수명: myabs
    매개변수: 정수형 1개
    리턴값: 정수형 1개
    함수 내용: 매개값에 대한 절댓값을 반환하는 함수 구현

    ↓ 입력 예시 ↓
    -1

    ↓ 출력 예시 ↓
    1
'''
def myabs(n):
    if n<0:
        return -n
    return n
n = int(input())
print(myabs(n))
