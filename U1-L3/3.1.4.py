Num=87
i=0
guess=0
while i<5:
    guess=int(input("请输入1-100之间的数字"))
    if guess==Num:
        print("猜对了")
        break
    elif guess>Num:
        print("猜大了")
    else:
        print("猜小了")
    i=i+1