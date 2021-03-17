# 인수(인자)의 형식



1. 가변 인수(위치 가변 인수)

   - 인수의 이름 앞에 * 기호를 붙이면 여러 개의 인수가 올 수 있음.
   - 가변인수는 인수 목록의 마지막에 와야 하며 2개 이상 있으면 안됨.

   ```python
   def intsum(*num):
     sum = 0
     for n in num:
       sum += n
     return n
   
   
   print(intsum(1, 2, 3))
   print(intsum(1, 2, 4, 5, 6, 6))
   ```

   

2. 키워드 인수

   - 순서와 무관하게 인수를 전달.
   - 인수의 이름을 지정해 대입 형식으로 전달.

   ```python
   def store(begin, end, step):
     print(begin, '사과')
     print(end, '배')
     print(step, '감')
     return begin + end + step
   
     
   print(store(begin=3, end=2, step=10))
   ```

   

3. 키워드 가변 인수
   - 키워드 인수를 가변 개수 전달. 인수 목록에 ** 기호를 붙임.
   - 키워드 인수를 전달하면 인수의 이름과 값의 쌍을 딕셔너리 형태로 전달.
   - 인수의 전달 순서가 상관 없음.
   
   ```python
   def store(**args):
     begin = args['begin']
     end = args['end']
     step = args['step']
     
     return begin + end + step
   
   print(store(begin=3, end=2, step=10))
   ```



4. 위치 가변 인수, 키워드 가변 인수
   - 동시에 사용 가능.
   - 위치 인수가 먼저 오고 키워드 인수가 뒤에 옴.
   - 위치 가변 인수는 임의의 값을 tuple로 저장.
   - 키워드 가변 인수는 임의의 값을 dictionary로 저장.