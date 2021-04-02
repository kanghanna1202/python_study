# sequence 자료형

- 연속적으로 이어져 있는 자료형

![sequence자료형](https://dojang.io/pluginfile.php/13491/mod_page/content/4/011002.png)
- 이미지: https://dojang.io/mod/page/view.php?id=2205

<br>

#### 시퀀스 자료형

- 시퀀스 자료형으로 만든 객체 = 시퀀스 객체
- 시퀀스 객체에 들어있는 각 값 = 요소(element)



#### 시퀀스 자료형의 공통 기능

- 특정 값이 있는지 확인하기(in 연산자)

```python
>>> lst = [1, 2, 3, 4, 5, 6]
>>> 10 in lst
False
>>> 3 in lst
True
>>> 10 not in lst
True
>>> 3 not in lst
False
```

- 객체 연결하기(+ 연산자) - range는 불가능 -> 리스트 또는 튜플로 만들어서 연결

```python
lst_1 = [1, 2, 5, 6]
lst_2 = [4, 7, 8, 9]

print(lst_1 + lst_2)

[1, 2, 5, 6, 4, 7, 8, 9]
```

- 객체 반복하기 - range는 불가능

```python
>>>[2, 3, 4] * 2
[2, 3, 4, 2, 3, 4]
```

- 요소 개수 구하기(len())

```python
lst = [1, 2, 3, 4, 5]

print(len(lst))

5
```

range의 숫자 생성 개수 구하기

```python
>>> len(range(0, 10, 2))
5
```

- 요소 접근하기

```python
>>> lst = [1, 2, 3, 4, 5]
>>> lst[3]
4
>>> lst[-1]
5
>>> lst[-4]
2
```

- 요소 삭제하기(del)

```python
lst = [1, 2, 3, 4]
del lst[2]

print(lst)

[1, 2, 4]
```

- 슬라이스

```python
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> lst[0:5]
[1, 2, 3, 4, 5]
>>> lst[1:3]
[2, 3]
>>> lst[4:7]
[5, 6, 7]
>>> lst[4:-2]
[5, 6, 7, 8]
>>> lst[4:-1]
[5, 6, 7, 8, 9]
>>> lst[2:8:3]
[3, 6]
>>> lst[:5]
[1, 2, 3, 4, 5]
>>> lst[5:]
[6, 7, 8, 9, 10]
>>> lst[:]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

