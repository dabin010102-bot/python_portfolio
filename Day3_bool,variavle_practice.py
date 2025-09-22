Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#true false 기본값#
1 == 1
True
2>1
True
2<1
False

#불 연산#
bool('python
     
SyntaxError: unterminated string literal (detected at line 1)
bool('python')
     
True

bool('')
     
False
bool([1,2,3])
     
True
bool([])
     
False
bool(0)
     
False
bool(3)
     
True

#리스트 복사#
     
a = [1,2,3]
     
b=a
     
print(b)
     
[1, 2, 3]

a[1]= 4 # 두 번째 요소를 4로 바꿈#
     
b
     
[1, 4, 3]
##b요소도 바뀌었다##
     
#a 변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 하기#
     
#1.[:] 이용
     
a = [1,2,3]
     
b = a[:]
     
a[1]=4
     
a
     
[1, 4, 3]
b
     
[1, 2, 3]
>>> 
>>> #2.copy모듈 이용#
...      
>>> from copy import copy
...      
>>> a= [1,2,3]
...      
>>> b = copy(a)
...      
>>> b is a
...      
False
>>> 
>>> a,b = ('python','life')
...      
>>> (a.b) = 'python','life'
...      
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    (a.b) = 'python','life'
AttributeError: 'str' object has no attribute 'b' and no __dict__ for setting new attributes
>>> [a,b] = ['python','life']
...      
>>> a= b = 'python'
...      
>>> a = 3
...      
>>> b = 5
...      
>>> a,b=b,a
...      
>>> a
...      
5
>>> b
...      
3
