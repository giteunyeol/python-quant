#case1, case2에 10과 20을 할당하고 둘을 더한값을 printf;
# 변수명 = 숫자 >> 변수명에 숫자 할당 
#print에서 

case1 = 10
case2 = 20
print(case1 + case2)

#파이썬은 double형이 존재하지 않음.
#type 함수 : 데이터의 형태를 확인해줌
#type (1) : int형을 반환, type(1.0) : float형을 반환
print(type(1))

#자료형도 선언 필요 x 
#사칙연산을 int a = 3; int b = 6; int answer = a + b;로 하는게 아니라 a = 3 , b = 6, answer = a + b로 가능 ,,,
a = 3 
b = 6
answer = a + b
print("answer") 

# 심지어 컴파일 했을때 \n도 자동으로 해줌
# ** : 제곱 ex) 2 ** 3 : 2의 3제곱
# // 나눗셈의 몫을 반환(c언어에서 기본 나누기), %는 같음
print(2 ** 3)
print(3 / 2)

#문자열을 만드는 방법 4가지 (단일문자와 문자열을 큰/작은 따옴표로 구분하지 않음)
# "a"   /////   'a'   ////////      """a"""      //////   '''a'''   
# 입력상태에서 줄을 바꾸면서 할당하고 싶을때 3개씩 사용

#문자열이 합쳐짐...
a = "hi i am"
b = " eunyeol"
print(a + b) 

#문자열에 곱셈도 가능
name = "eunyeol "
print(name * 3)

#f"~~~"을 하면 문자열 생성 가능
#{변수 이름}
학번 = "20"
년도 = "2024년"
이름 = "양은열"
print(f"현재 {년도}에 {학번} {이름}은 학생입니다.")

#len(변수 이름) : 문자열의 길이 
print(년도)

#replace 함수
# (변수이름).replace ('바꾸고 싶은 것', '바꿀 것')
time = '4시 33분'
print(time)
time = time.replace('33', '34')
print(time)

# 나누는 함수 : split 
#변수명.split('기준으로 나눌 것')
time = time.split(' ')
print(time)

#index : c언어와 동일
#범위 인덱스 : 변수명:[a : b] 변수의 a~b까지 리턴
temp = "microeconomics"
print(temp[0 : 5])

#변수명 [ , , , ] 식으로 인덱스 선언 가능
#배열 안에 배열 선언 가능 ex) [ 'a', 'b', [...]]
#list도 연산 가능
color = ['red', 'orange', 'yellow', '...' ]
print(color)

#append 함수. 마지막에 데이터 추가) 변수이름.append(추가하고싶은 데이터)
color.append('purple')
print(color)

#extend함수, 묶음으로 넣을때(직접)
#ex)변수명.extend([2, 3])

#list 수정 : c와 동일(새로운 값을 할당해줌)
#ex)
# ****list를 선언할때 대괄호로 해야함, 그냥 선언하면 튜플로 선언(변경 불가)
number = [1, 2, 3, 4, 5]
print(number)
number[2] = 100
print(number)
# del함수, del 변수명[인덱스 번호] >> 삭제
del number[2]
print(number)

#remove함수, 값을 가진 첫번째 변수 제거 변수.remove
number.remove(5)
print(number)

##------- del 함수는 인덱스를 기준으로 제거, remove함수는 값을 기준으로 제거-----

#pop 함수 : 마지막의 값을 빼버림 // 변수이름.pop()
number.pop()
print(number)

#sort 함수 : 리스트를 정렬.
number = [1234, 1235324 ,56435 ,325453 ,2345234 ,76857, 1234, 5647]
number.sort()
print(number)

#튜플 : 소괄호로 선언, **변경 불가
temp = ('a', 's', 't')
print(type(temp))

#dictionary, 직접 값을 하나씩 할당해줘야함.
example = {'key1' : 1, 'key2' : 2, 'key3' : 3} # 1 ~ 3까지 각각 숫자 할당
print(example)

#set(집합)
#중복 x, 순서 x
# set1 = set([1,2,3])은 맞는 표현이지만, set2 = set("banana")는 순서가 존재하지 않기때문에 틀린 표현

number1 = set([2, 4, 6, 8, 10])
number2 = set([2, 3, 5, 7, 11])

#합집합 : union
print(number1.union(number2))
#교집합 : intersection
print(number1.intersection(number2))
#차집합 : difference
print(number1.difference(number2))

#불리언 : T / F  파이썬에서 == : 양쪽값이 같은지 비교, !=: 다른지 비교
print(1 == 1)
print(1 != 1)
#bool(0)은 false, 0을 제외한 나머지 숫자는 true
#bool() 에서 괄호 안에 값이 없으면 false, 값이 있으면 true.

#datetime. import 함수로 불러옴
import datetime
now = datetime.datetime.now()
print(now)

#변수.year , month, ...모두 작동 가능
print(now.weekday()) #요일
print(now.date()) # 날짜
print(now.time()) # 시간

#strftime : 시간 > 문자열 //// strptime: 문자열 > 시간