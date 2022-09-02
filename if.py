from operator import truediv


money = True
if money :
    print("택시를 타고 가라")
else :
    print("걸어 가라")
#--------------------------------------------------------------------
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket :
    pass
elif card :
    print("택시를 타고가라.")
else :
    print("걸어가라")
#--------------------------------------------------------------------

treehit = 0
while treehit < 10 :
    treehit = treehit +1
    print("나무를 %d번 찍었습니다." % treehit)
    if treehit == 10 :
        print("나무 넘어갑니다.")
#--------------------------------------------------------------------

score = 70
if score >= 60 :
    message = "success"
else : 
    message = "failure"
print(message)

#--------------------------------------------------------------------

coffee = 10
money = 300
while money :
    print("돈을 받았으니 커피를 줍니다.")
    print("남은 커피의 양은 %d개 입니다." % coffee)
    coffee = coffee -1
    if not coffee : 
        print("커피가 다 떨어졌습니다. 판매를 중단합니다.")
        break
