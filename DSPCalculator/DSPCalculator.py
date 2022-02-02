class DSP_Calculator():



    def _recipe(self):
        self._make_out = float(input("만드는 양\n"))
        self._make_time = float(input("만드는 시간\n"))
        self._make_in = list(map(int, input("만드는데 들어가는 재료\n").split()))
        
        
    def _setting(self):
        self._build_speed = float(input("건물 생산속도\n0.5, 1, 1.5중에서 선택\n"))
        p = int(input("가속제 설정\n1: 결과물 + 25%  2: 2배속  0:사용안함\n"))
        self._prolif_extra, self._prolif_speed = 1, 1
        if p == 1:
            self._prolif_extra = 1.25
        elif p == 2:
            self._prolif_speed = 2
            

    def _need_input(self):
        if len(self._make_in) == 1:
            self._need_in = self._need_build * (self._make_in[0] / self._make_time * self._build_speed * self._prolif_speed)    
            print("만드는데 필요한 재료의 양: 초당 ", self._need_in, "개\n")
        else:
            for i in range(len(self._make_in)):
                self._need_in = self._need_build * (self._make_in[i] / self._make_time * self._build_speed * self._prolif_speed)    
                print("만드는데 필요한", i+1,"번째 재료의 양: 초당 ", self._need_in, "개\n")
                


    def calbyoutput(self):
        self._recipe()
        self._setting()

        self._need_out = float(input("만들어야하는 양\n"))

        self._need_build = self._need_out / (self._make_out * self._prolif_extra / self._make_time * self._build_speed * self._prolif_speed)

        print("\n\n만드는 양 : 초당 ", self._need_out, "개    분당 ", 60 * self._need_out, "개\n")
        print("만드는데 필요한 건물: ", self._need_build, "개\n")
        self._need_input()


    def calbybuild(self):
        self._recipe()
        self._setting()

        self._need_build = float(input("만드는 건물 갯수\n"))
        self._need_out = self._need_build * (self._make_out * self._prolif_extra / self._make_time * self._build_speed * self._prolif_speed)
        
        print("\n\n만들어지는 양 : 초당 ", self._need_out, "개    분당 ", 60 * self._need_out, "개\n")
        print("만드는 건물 개수: ", self._need_build, "개\n")
        self._need_input()

    def calbyinput(self):
        print("*들어가는 재료 하나만 입력할 것")
        self._recipe()
        self._setting()
        
        self._need_in = float(input("입력할 재료의 양\n"))
        
        self._need_build = self._need_in / (self._make_in[0] / self._make_time * self._build_speed * self._prolif_speed)
        self._need_out = self._need_build * (self._make_out * self._prolif_extra / self._make_time * self._build_speed * self._prolif_speed)
        print("\n\n입력한 재료의 양: 초당 ", self._need_in, "개\n")
        print("만들어지는 양 : 초당 ", self._need_out, "개    분당 ", 60 * self._need_out, "개\n")
        print("만드는데 사용할 수 있는 건물 개수: ", self._need_build, "개\n")


if __name__ == "__main__" :
    c = DSP_Calculator()
    while 1:
        select = int(input("\n1: 만들고싶은 물건의 양으로 계산\n2: 만들 건물 개수로 계산\n3: 입력할 재료의 양으로 계산\n0: 종료\n"))
        if select == 1:
            c.calbyoutput()
        elif select == 2:
            c.calbybuild()
        elif select == 3:
            c.calbyinput()
        elif select == 0:
            exit()

