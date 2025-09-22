# Day3: 튜플 & 딕셔너리 연습 (실행용 코드)

# --- 튜플 예제 ---
t1 = (1, 2, 'a', 'b')
print("t1[0] =", t1[0])    # 1
print("t1[3] =", t1[3])    # 'b'

# 슬라이싱
t1 = (1, 2, 'a', 'b')
print("t1[1:] =", t1[1:])  # (2, 'a', 'b')

# 더하기, 반복, 길이
t2 = (3, 4)
t3 = t1 + t2
print("t3 =", t3)          # (1,2,'a','b',3,4)

t_repeat = t2 * 3
print("t2 * 3 =", t_repeat)  # (3,4,3,4,3,4)

print("len(t1) =", len(t1))  # 4


# --- 딕셔너리 예제 ---
a = {1: 'a'}
a[2] = 'b'
print("after add:", a)      # {1: 'a', 2: 'b'}

a['name'] = 'pey'
print("after add name:", a)

a[3] = [1, 2, 3]
print("after add list:", a)

# 삭제 (키로 삭제)
del a[1]
print("after del 1:", a)

# key로 value 읽기
grade = {'pey': 10, 'juliet': 99}
print("grade['pey'] =", grade['pey'])
print("grade['juliet'] =", grade['juliet'])

# 같은 key가 여러 번 쓰이면 마지막 값으로 덮어써짐
a = {1: 'a', 1: 'b'}
print("duplicate key ->", a)

# keys, values, items 보기 (보기 쉽게 list로 변환)
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print("keys:", list(a.keys()))
print("values:", list(a.values()))
print("items:", list(a.items()))

# 안전하게 값 얻기: get
print("address get:", a.get('address'))            # None
print("address get default:", a.get('address', '없음'))  # '없음'
