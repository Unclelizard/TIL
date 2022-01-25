# Keyword argument vs Positional argument



함수 호출

1. 정의된 순서대로 값을 넘겨준다

   ```
   add(1,2)
   ```

2. 정의된 이름(파라미터)를 키워드로 해서하나씩 직접 넘겨준다.

   ```
   add(x=1, y=2)
   ```

함수 정의

1. 아무것도 안하기

   ```
   def add(x,y):
   	pass
   ```

2. 기본 값 설정(호출하는 입장에서 해당 파라미터는 선택)

   ```
   def add(x, y=10):
   	pass
   ```

3. 정의되지 않은 갯수

   1. 나열(시퀀스)

      ```
      def add(*args):
      	pass
      	#내부에서 args 튜플로 동작
      ```

   2. Key -value

      ```
      def func(**kwargs):
      	pass
      ```

   

   