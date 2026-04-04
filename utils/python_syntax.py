# ====================================
# .isdigit()
# 파이썬의 문자열 메서드
# 문자열이 숫자로만 이루어져 있는지를 검사
# 맞으면 True, 틀리면 False
# ====================================

print("123".isdigit())   # True
print("12a3".isdigit())  # False
print("abc".isdigit())   # False
print("".isdigit())      # False

# if not x.isdigit():
# x가 숫자가 아니라면

# x = int(input()) 이렇게 바로 쓰면 "abc" 입력시 에러발생
# 그래서 안전하게
x = input()

if x.isdigit():
    x = int(x)
    
# isdigit은 정수만 허용한다 . - 은 숫자로 보지 않음

# 확장방법
# 1. try-except
try:
    x = int(input())
except ValueError:
    print("숫자 입력하세요")
# 에러 처리 핵심 패턴
    
# 2. 음수까지 허용하려면
x = input()

if x.lstrip("-").isdigit():
    print("정수 가능")
# .lstrip() 문자열 왼쪽 혹은 특정 문자를 제거하는 함수

# ====================================
# generator 표현식 (제너레이터)
# ====================================

# (c in directions for c in sannpo)
# 하나씩 검사 결과를 만들어 낸다
gen = (x for x in range(3))

# 함수형태의 제너레이터

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)
print (next(gen))

# ====================================
# all()
# all(반복 가능한 것)
# 전부 True면 True, 하나라도 False면 False
# ====================================

all([True, True, True])   # True
all([True, False, True])  # False

# ====================================
# async / await
# 기다리는 작업을 효율적으로 처리하는 문법으로서
# 오래걸리는 작업(네트워크, 파일 등)을 기다리는 동안
# 다른 일을 함. 비동기 처리
# ====================================

async def f():
    await something()

# ====================================
# 리스트 컴프리핸션
# for문을 한 줄로 줄여서 리스트를 만드는 문법
# ====================================

nums = [i for i in range(5)]

nums = [i * 2 for i in range(5)]

nums = [i for i in range(10) if i % 2 == 0]