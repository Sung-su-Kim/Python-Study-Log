"""
problem_001

우주 여행 중, 미확인 행성에 불시착하게 되었다.
이 행성은 나이를 알파벳으로 말한다.
예를 들어 a는 0, b는 1, c는 2 ... j는 9이다.
나이가 매개변수로 주어질 때, 이 행성 식으로 나이를 출력
조건 : 나이는 자연수, 알파벳은 소문자만 사용, 입력된 나이는 1000미만
"""

# 사용자로부터 나이를 입력받아 age 리스트에 저장한다
age = list(input("나이를 입력하세요 : "))
# 알파벳과 숫자가 각각 대응되도록 x 딕셔너리를 추가한다
x = {
    "0" : "a", "1" : "b", "2" : "c", "3" : "d", "4" : "e",
    "5" : "f", "6" : "g", "7" : "h", "8" : "i", "9" : "j"
}
# 최종 결과를 담은 total 리스트를 초기값으로 저장한다
total = []

# 나이의 자릿수를 고려하여 출력하기 위해 age길이는 num에 저장한다
num = len(age)

# for문의 순서열을 x로 하여 만든다
for k,v in x.items():
    # if문의 조건을 age의 0번 인덱싱이 x에 있을 경우로 설정
    if age[0] == k:    
        # x값의 벨류를 total에 저장한다
        total.append(v)
        # 딕셔너리의 순서열의 흐름을 고려하여 반복문을 중단시킨다
        break

# 나이가 두자리일 경우를 가정하여 if문 생성
if num > 1:
    # for문의 순서열을 x로 하여 만든다
    for k,v in x.items():
        # if문의 조건을 1번 인덱싱이 있을 경우로 저장한다
        if age[1] == k:
            # x값의 벨류를 total에 저장한다
            total.append(v)
            # 반복문을 종료한다
            break

# 나이가 세자리일 경우를 가정하여 if문 생성
if num > 2:
    # for문의 순서열을 x로 하여 만든다
    for k,v in x.items():
        # if문의 조건을 2번 인덱싱이 있을 경우로 저장한다
        if age[2] == k:
            # x값의 벨류를 total에 저장한다
            total.append(v)
            # 반복문을 종료한다
            break

# 나이가 네자리일 경우를 가정하여 if문 생성
if num > 3:
    # for문의 순서열을 x로 하여 만든다
    for k,v in x.items():
        # if문의 조건을 3번 인덱싱이 있을 경우로 저장한다
        if age[3] == k:
            # x값의 벨류를 total에 저장한다
            total.append(v)
            # 반복문을 종료한다
            break

# 최종값인 total을 이어붙여 문자열로 출력한다
chat = ''.join (total)
print (f"당신의 나이는 : {chat}")