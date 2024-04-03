#자산가격 결정론 과제2

import numpy as np
#정수, 실수, 유니코드, 유니코드
arr3 = np.array([1, 2, 3, 4, 5])   
arr4 = np.array([1, 2, 3.0, 5.0, 12.165])
arr5 = np.array([1, 2, "3", "6", "12"]) 
arr6 = np.array(["안녕하세요 반가워요"]) 

print(arr3, arr3.dtype)
print(arr4, arr4.dtype)
print(arr5, arr5.dtype)
print(arr6, arr6.dtype)

# 1 ~ 3 차원
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 15, 132])                             
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])                
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) 

#각각의 형태 출력
print(arr1.shape)                                    
print(arr2.shape)
print(arr3.shape)

#arange / linspace

사자 = np.arange(15)             
호랑이 = np.arange(-1, 17, 1)
토끼 = np.arange(10, 1, -0.5)   
거북이 = np.linspace(0, 2, 5)   

print("np.arange(15):{}".format(사자))
print("np.arange(-1, 4.5, 1.5):{}".format(호랑이))
print("np.arange(10, 1, -1):{}".format(토끼))
print("np.linspace(0, 2, 5):{}".format(거북이))

#zeros 
경제 = np.zeros(9)                    
경영 = np.zeros((7, 2))               
무역 = np.zeros((2, 2), dtype = bool)  

print(경제)
print(경영)
print(무역)

#random

랜덤1 = np.random.random(8)
랜덤2 = np.random.random((3, 1))
print(랜덤1)
print(랜덤2)

랜덤노말1 = np.random.normal(3, 1, 5)
랜덤노말2 = np.random.normal(10, 3, (3, 3))
print(랜덤노말1)
print(랜덤노말2)

#reshape(형변환)

형변환1 = np.array([1, 2, 3, 4])
형변환2 = np.array([[1, 3], [4, 6]])


print(형변환1.reshape(2, 2)) 
print(형변환2.reshape(-1, 4))  
print(형변환1.reshape(-1, 2)) 

#유니버셜 함수

import timeit

##배열의 크기 : 1000
def 배열덧셈():
    x1 = np.random.random(1000)
    x2 = np.random.random(1000)
    return x1 + x2

# 배열 덧셈 함수를 실행하여 시간 측정
걸린시간 = timeit.timeit(배열덧셈, number=1000)

print(걸린시간)

#배열 연산
x = np.arange(4)
y = np.linspace(1, 10, 4)
print("x  =", x)
print("y  =", y)
print("x * y =", x * y)
print("x / 3 =", x / 2)
print("-x     = ", -x)
print("x ** 3 = ", x ** 2)
print("x % 2  = ", x % 2)

#절댓값
x = np.array([-2, -1, -5, -8, -13, 2])
print("abs(x) =", np.abs(x))

#지수 
x = np.array([1, 2, 3])
print("x =", x)
print("e^x =", np.exp(x))
print("2^x =", np.exp2(x))
print("3^x =", np.power(3, x))
print("5^x =", np.power(5, x))

# 로그
print("ln(x) =", np.log(x)) 
print("log2(x) =", np.log2(x)) 
print("log10(x) =", np.log10(x))

#비교
x = np.array([1,2,3,5,-1])
y = np.array([1,3,-2,8,2])

print("x == y: ", x == y)
print("x > y:", x > y)
print("x>=1:", x>=1)


#브로드 캐스팅
보쌈 = np.array([[1, 2], [3, 4]])
족발 = np.array([-1, -2])
막국수 = np.array([5, 3])
print(보쌈 + 족발 + 막국수)

#인덱싱 / 슬라이싱
korea = [[1, 2], [3, 4]]
print(korea[0][1])

korea = np.array(korea)
print(korea[0, 1])

X = np.arange(1, 10)
print(X[[2, 5]]) # 2 / 5번째 요소 인덱싱

X = np.array([[1, 2], [3, 4], [5, 6]])
print(X[0, 1])   
print(X[[0, 1]]) 

X = np.arange(20).reshape(4, 5)
print(X[1, [1,-1]])      
print(X[0, 0:3])       
print(X[[0, 1], [2, 3]]) 

#인덱싱 / 슬라이싱 (부울)

x = np.array([1,2,3,4])
b = [False, False, False, True]
print(x[b])

x = np.array([1,2,3,4])
cond = x >= 3
print(cond)
print(x[cond])

print(x[x>=3])

x = np.arange(15).reshape(5, 3)
print(x) 

print(np.sum(x))
print(x.sum())

# 행 
print(np.sum(x, axis = 0))
print(x.sum(axis = 0))

# 열 
print(np.sum(x, axis = 1))
print(x.sum(axis = 1))

# 행일때는 0, 열일때는 1

#sum : 합계
print("열별 합계: {}".format(np.sum(x, axis = 0)))
print("전체 합계: {}".format(np.sum(x)))
#min : 최소값
print("행별 최소값: {}".format(x.min(axis = 1)))
print("행 방향 최소값: {}".format(x.min(axis = 0)))
#max : 최대값
print("전체 최댓값: {}".format(x.max()))
#std : 표준편차
print("열별 표준편차: {}".format(np.std(x, axis = 0)))
#median : 중간값
print("전체 중간: {}".format(np.median(x)))
#상위 " " %
print("전체 상위 20%: {}".format(np.quantile(x, 0.2)))
#중복을 제거한 값
print("유니크한 값 목록: {}".format(np.unique(x)))