'''
Q)  다음 리스트에서 찾고자 하는 데이터를 입력 받아
    해당 데이터가 리스트의 몇 번째에 있는지 찾아 출력하시오.

    ↓ 실행화면1 ↓
    찾을 데이터 입력: 7
    4번째 데이터입니다.

    ↓ 실행화면2 ↓
    찾을 데이터 입력: 3
    8번째 데이터입니다.
'''
k = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
search = int(input('찾을 데이터 입력: '))
n = len(k) # 10개

# 1. 반복문
for i in range(n): # i <- 0~9 : 리스트의 인덱스
    if k[i] == search:
        print(f'{i+1}번째 데이터 입니다.')
        break

# 2. 리스트 함수
print(f'{k.index(search)+1}번째 데이터 입니다.')
