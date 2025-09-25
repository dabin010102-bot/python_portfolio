# ===============================
# Day3: 튜플, 딕셔너리, 집합, 불 자료형 실습
# ===============================

# 1️⃣ 튜플 인덱싱 & 슬라이싱
defects = ('A', 'B', 'C', 'A', 'B')

# 두 번째 요소와 마지막 요소 출력
print("두 번째 요소:", defects[1])   # B
print("마지막 요소:", defects[-1])   # B

# 처음 3개 불량 코드만 슬라이싱
print("처음 3개 불량 코드:", defects[:3])  # ('A', 'B', 'C')


# 2️⃣ 딕셔너리 연습 - 불량 제품별 개수
qc_data = {'A': 3, 'B': 5, 'C': 2}

# 새로운 불량코드 'D':4 추가
qc_data['D'] = 4
print("불량 데이터 추가:", qc_data)  # {'A':3, 'B':5, 'C':2, 'D':4}

# 'B' 불량 개수 출력
print("B 불량 개수:", qc_data['B'])  # 5

# 'C' 불량 제거
del qc_data['C']
print("C 불량 제거 후 데이터:", qc_data)  # {'A':3, 'B':5, 'D':4}


# 3️⃣ 집합 - 중복 불량 제거
defect_list = ['A', 'A', 'B', 'C', 'B', 'D', 'A']

# 집합으로 중복 제거
unique_defects = set(defect_list)
print("오늘 발생한 불량 코드(중복 제거):", unique_defects)  # {'A','B','C','D'}


# 4️⃣ 불 자료형 (B 불량 존재 여부 확인)
# defects 리스트 예시
defects_today = ['A', 'C', 'D']

# 'B' 불량 발생 여부
b_exists = 'B' in defects_today
print("B 불량 발생 여부:", b_exists)  # False
