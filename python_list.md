# 리스트

- 변수에 값을 저장할 때 '[ ]' 로 묶어주면 리스트가 되며 각 값은 ',' 로 구분
```python
lst = [1, 2, 3, 4, 10]
```

- 여러 가지 자료형 저장 가능
```python
lst = [1, '파이썬!', True, 23.45]
```

- 빈 리스트 만들기
```python
lst = []
lst = list()
```

- range 이용
```python
lst = list(range(5))

print(lst)

[0, 1, 2, 3, 4]


lst_2 = list(range(1, 6))

print(lst_2)

[1, 2, 3, 4, 5]
```

- 문자열 넣기
```python
print(list('python'))

['p', 'y', 't', 'h', 'o', 'n']
```

- 리스트 언패킹
```python
lst = [1, 2, 3]
n1, n2, n3 = lst

print(n1, n2, n3)

1 2 3
```
