def cal():
    make_q = float(input("만드는 양\n"))
    make_time = float(input("만드는 시간\n"))
    
    make_value = input("만드는데 들어가는 재료\n").split()
    
    need_make = float(input("만들어야하는 양\n"))
    b = float(input("건물 생산속도\n0.5, 1, 1.5중에서 선택\n"))
    p = int(input("가속제 설정\n1: 결과물 + 25%  2: 2배속  0:사용안함\n"))
    prolif_extra, prolif_speed = 1, 1
    if p == 1:
        prolif_extra = 1.25
    elif p == 2:
        prolif_speed = 2

    need_build = need_make / (make_q * prolif_extra / make_time * b * prolif_speed)
    print("만드는 양 : 초당 ", need_make, "개\n")
    print("만드는데 필요한 건물: ", need_build, "개\n")
    if len(make_value) == 1:
        need_value = need_build * (int(make_value[0]) / make_time * b * prolif_speed)    
        print("만드는데 필요한 재료의 양: 초당 ", need_value, "개\n")
    else:
        for i in range(len(make_value)):
            need_value = need_build * (int(make_value[i]) / make_time * b * prolif_speed)    
            print("만드는데 필요한", i+1,"번째 재료의 양: 초당 ", need_value, "개\n")


### 위에는 필요한 건물 구하는 함수이고 아래는 몇개가 만들어지는지 구하는 함수
    
def cal2():
    make_q = float(input("만드는 양\n"))
    make_time = float(input("만드는 시간\n"))
    make_value = int(input("만드는데 들어가는 재료\n"))
    make_build = float(input("만드는 건물 갯수\n"))
    
    b = float(input("건물 생산속도\n0.5, 1, 1.5중에서 선택\n"))
    p = int(input("가속제 설정\n1: 결과물 + 25%  2: 2배속  0:사용안함\n"))
    prolif_extra, prolif_speed = 1, 1
    if p == 1:
        prolif_extra = 1.25
    elif p == 2:
        prolif_speed = 2

    made_out = make_build * (make_q * prolif_extra / make_time * b * prolif_speed)
    need_value = make_build * (make_value / make_time * b * prolif_speed)
    print("만들어지는 양 : 초당 ", made_out, "개\n")
    print("만드는 건물 개수: ", make_build, "개\n")
    print("만드는데 필요한 재료의 양: 초당 ", need_value, "개\n")

def cal3():
    make_q = float(input("만드는 양\n"))
    make_time = float(input("만드는 시간\n"))
    make_value = int(input("만드는데 들어가는 재료\n"))
    in_value = float(input("입력하는 재료의 양\n"))
    
    b = float(input("건물 생산속도\n0.5, 1, 1.5중에서 선택\n"))
    p = int(input("가속제 설정\n1: 결과물 + 25%  2: 2배속  0:사용안함\n"))
    prolif_extra, prolif_speed = 1, 1
    if p == 1:
        prolif_extra = 1.25
    elif p == 2:
        prolif_speed = 2

    make_build = in_value / (make_value / make_time * b * prolif_speed)
    made_out = make_build * (make_q * prolif_extra / make_time * b * prolif_speed)
    print("입력한 재료의 양: 초당 ", in_value, "개\n")  
    print("만들어지는 양 : 초당 ", made_out, "개\n")
    print("만드는데 사용할 수 있는 건물 개수: ", make_build, "개\n")
  
