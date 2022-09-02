import re


test_list = ['one','two','three']
for i in test_list :
    print(i)


a = [(1,2), (3,4),(5,6)]
for (first, last) in a :
    print(first + last)


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks :
    number = number +1
    if mark >= 60 :
        print("%d번 힉생은 합격입니다." % number)
    else :
        print("%d번 학생은 불합격입니다." % number)

# for문과 continue
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks :
    number = number +1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

#for문과 함께 자주 사용하는 range함수
a = range(10)
print(a)

sum = 0 
for i in range(1, 11):
    print(i)
print(sum)

add = 0
for i in range(1,11):
    add = add + i
print(add)

#range함수는 숫자 리스트를 자동으로 만들어 주는 range 함수와 함께 사용하는 경우가 많다.
#range(10)은 0부터 10미만의 숫자를 포함하는 range객체를 만들어준다.
#시작 숫자와 끝 숫자를 지정하려면 range(시작 숫자, 끝 숫자)형태를 사용하는데, 이때 끝 숫자는 포함되지 않는다.

#for와 range를 이용한 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j ,end=" ")
    print('')

#만약 구구단의 모든 결과를 리스트에 담고 싶다면 리스트 내포를 사용하여 다음과 같이 간단하게 구현할 수도 있다.
result = [x*y for x in range(2,10)
            for y in range(1,10)]
print(result)


#리스트 내포 사용하기
a = [1,2,3,4]
result = []
for num in a :
    result.append(num*3)
print(result)


#만약 [1,2,3,4]중에서 짝수에만 3을 곱하여 담고 싶다면 다음과 같이 리스트 내포 안에 "if 조건"을 사용할 수 있다.
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

