# Day2 연습문제 (품질관리 응용)

# 문제 1. 불량 개수 집계
defect_list = ['A', 'B', 'C', 'A', 'B', 'A', 'C', 'C']
print("A 불량 개수:", defect_list.count('A'))

# 문제 2. 불량 제거 & 신규 불량 추가
defects = ['A', 'A', 'B', 'C']
defects.remove('A')  # 첫 번째 A 제거
defects.extend(['D'])  # D 추가
print("최종 불량 리스트:", defects)

# 문제 3. 불량 무게 계산
products = [
    [2, 0.5],  # 제품1
    [3, 0.7],  # 제품2
    [1, 0.4]   # 제품3
]
total_weight = products[0][0]*products[0][1] + products[1][0]*products[1][1] + products[2][0]*products[2][1]
print("총 불량 무게:", total_weight, "kg")

# 문제 4. 불량 개수 정렬
defect_qty = [12, 5, 8, 3, 10]
defect_qty.sort()
print("오름차순:", defect_qty)
defect_qty.reverse()
print("내림차순:", defect_qty)

# 문제 5. 특정 구간 불량 추출
inspections = [100, 95, 98, 102, 97, 105, 99]
print("3~5번째 검사 결과:", inspections[2:5])
