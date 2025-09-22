Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# True/False 기본값
print(1 == 1)   # True
print(2 > 1)    # True
print(2 < 1)    # False

# 불(Boolean) 연산
print(bool('python'))   # True
print(bool(''))         # False
print(bool([1,2,3]))    # True
print(bool([]))         # False
print(bool(0))          # False
print(bool(3))          # True

# 리스트 복사

# 1. 단순 할당 (주소 공유)
a = [1,2,3]
b = a
a[1] = 4
print(a)  # [1, 4, 3]
print(b)  # [1, 4, 3] -> b도 같이 변경됨

# 2. [:] 슬라이싱 이용 (주소 분리)
a = [1,2,3]
b = a[:]
a[1] = 4
print(a)  # [1, 4, 3]
print(b)  # [1, 2, 3] -> b는 변하지 않음

# 3. copy 모듈 이용 (주소 분리)
from copy import copy
a = [1,2,3]
b = copy(a)
print(b is a)  # False

# 변수 여러개 할당과 교환
a, b = ('python', 'life')
# [a, b] = ['python', 'life'] 도 가능
a = b = 'python'
a, b = 3, 5
a, b = b, a  # 변수 교환
print(a)  # 5
print(b)  # 3

