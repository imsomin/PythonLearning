cur_tem = 20  #현재 온도

def set_tem(des_tem): #설정할 온도
        

    global cur_tem
    if(cur_tem<des_tem):
        while(cur_tem<des_tem):
            cur_tem += 1
            print(f"현재 온도는 {cur_tem}도 입니다.")
    else:
        while(cur_tem>des_tem):
            cur_tem -= 1
            print(f"현재 온도는 {cur_tem}도 입니다.")


print("에어컨을 작동합니다.")

while True:
    put_tem=input("원하는 온도를 설정해 주세요: ")

    if(put_tem == '종료'):
        print("에어컨을 종료합니다")
        break
    elif(put_tem<='30' and put_tem>='18'):
        print(f"현재 온도는 {cur_tem}도 입니다")
        set_tem(int(put_tem))
    else:
        print("입력을 확인해 주세요")

"""
[실행결과]
에어컨을 작동합니다.
원하는 온도를 설정해 주세요: 12
입력을 확인해 주세요
원하는 온도를 설정해 주세요: 20
현재 온도는 20도 입니다      
원하는 온도를 설정해 주세요: 28
현재 온도는 20도 입니다 
현재 온도는 21도 입니다.
현재 온도는 22도 입니다.
현재 온도는 23도 입니다.
현재 온도는 24도 입니다.
현재 온도는 25도 입니다.
현재 온도는 26도 입니다.
현재 온도는 27도 입니다.
현재 온도는 28도 입니다.
원하는 온도를 설정해 주세요: 종료
에어컨을 종료합니다
"""