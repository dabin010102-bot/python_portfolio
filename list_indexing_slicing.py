Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #리스트 인덱싱#
>>> a = [1,2,3]
>>> a
[1, 2, 3]
>>> a[0]
1
>>> a[0]+a[2]
4
>>> a[-1]
3
>>> a[1,2,3,['a','b','c']]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a[1,2,3,['a','b','c']]
TypeError: list indices must be integers or slices, not tuple
>>> a = [1,2,3,['a','b','c']]
>>> a[0]
1
>>> a[-1]
['a', 'b', 'c']
>>> a[3]
['a', 'b', 'c']
>>> a[-1][0]
'a'
>>> a[-1][1]
'b'
>>> a[-1][2]
'c'
>>> #3중 리스트 인덱싱#
>>> a= [1,2,['a','b',['Life','is']]]
>>> a[2][2][2]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a[2][2][2]
IndexError: list index out of range
>>> a[2][2][0]
'Life'
>>> 
\
>>> #리스트의 슬라이싱#
>>> a = [1,2,3,4,5]
>>> a[0:2]
[1, 2]
>>> 
>>> a = "12345
SyntaxError: unterminated string literal (detected at line 1)
>>> a = "12345"
>>> a[0:2]
'12'
>>> a = [1,2,3,4,5]
>>> b = a[:2]
>>> b
[1, 2]
>>> c=a[2:]
>>> c
[3, 4, 5]
>>> 
>>> #1분코딩 a = [1,2,3,4,5] 리스트에서 슬라이싱 기법 사용해서 리스트[2,3]만들기#
>>> 
>>> a = [1,2,3,4,5]
>>> a[1:3]
[2, 3]
>>> 
>>> #중첩 리스트 슬라이싱#
>>> ㅁ = [1,2,3,['a','b','c'],4,5]
>>> a[2:5]
[3, 4, 5]
>>> a = [1,2,3,['a','b','c'],4,5]
>>> a[2:5]
[3, ['a', 'b', 'c'], 4]
>>> a[3][:2]
['a', 'b']
