"""
problem_004

온라인 서비스에서 사용될 닉네임이 필요하다
닉네임의 길이는 4자 이상, 8자 이하 (4미만일 경우 o를 길이가 4가될때까지 이어붙이고,
8보다 클 경우에는 8번째 문자까지만 사용)
닉네임에 소문자 l과 w, 대문자 O와 W는 사용할 수 없다
이외의 영어 대소문자와 숫자는 모두 사용가능
(l는 I로 변환, w는 vv로 변환, W는 VV로 변환, O는 숫자0로 변환)

제한사항 : 1 <= 입력받은 닉네임 <= 10
입력받은 닉네임은 영어 대소문자, 숫자로만 이루어져있다.
"""

# 사용자로부터 닉네임을 입력받는다 (whlie문으로 1보다 작거나 10보다 클 경우에는 재입력 출력,
# 영어 대소문자, 숫자 이외의 문자가 입력될 경우도 동일)
while True :
    nickname = input("닉네임을 입력하세요(영문, 숫자만 가능) : ")
    if  1 > len(nickname):
        print("1글자 이상의 닉네임을 작성")
        continue
    elif len(nickname) > 10:
        print ("닉네임은 10글자를 초과할 수 없습니다")
        continue
    else:
        break
# 무한 반복문
# while True:
#     # 만약 닉네임이 4보다 작다면
#     if len(nickname) < 4:                memo - 반복문 때문에 실행할 때마다 에러
#         # 이름 뒤에 o 추가
#         nickname + "o"
#         # 닉네임이 == 4라면
#         if len(nickname) == 4:
#             # 반복 중지
#             break
# while True:
#     # 그게 아니라 만약 닉네임이 8보다 크다면
#     if len(nickname) > 8:
#         # 인덱스 8번부터 마지막까지 삭제
#         del nickname [8:]
#         # 반복 종료
#         break

# 닉네임 변환시 변환된 값을 저장하기 위한 토탈함수 생성 
total = nickname

print (nickname)
# 닉네임으로 입력될 시 변환되어야하는 문자와 대응되도록 x 딕셔너리 생성
x = {
    'l' : 'I', 'w' : 'vv', 'W' : 'VV', 'O' : '0'
}
# 입력받은 닉네임을 순서열로 하는 for문 생성
for k, v in x.items():
    # 만약 입력받은 닉네임에 l가 있다면
    if k == 'l':
        # 닉네임에서 l를 i로 치환
        total = nickname.replace('l', 'i')  #memo - 닉네임 변환된 것을 저장하며 진행되도록 수정
    # 그게 아니라 만약 w가 있다면
    elif k == 'w':
        # 닉네임에서 w를 vv로 치환
         nickname.replace('w', 'vv')
    # 그게 아니라 만약 W가 있다면
    elif k == 'W':
        # W를 VV로 치환
         nickname.replace('W', 'VV')
    # 그게 아니라 만약 O가 있다면
    elif k == 'O':
        # O를 0로 치환
         nickname.replace('O', '0')
# 최종값을 출력
print (f"닉네임 : {nickname}")
