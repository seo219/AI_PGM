# 가급적이면 __ 써주기
# 이유 : 외부에서 직접 접근하는 것을 방지하여 데이터의 무결성을 유지하기 위해

class Television:
    def __init__(self, channel, volume, on): #생성자, 변수 3개
        self.__channel = channel
        self.__volume = volume
        self.__on = on

    def set_channel(self, channel):
        self.__channel = channel

    def get_channel(self):
        return self.__channel

tv1 = Television(1, 10, True) # 객체 생성
tv2 = Television(5, 20, False) # 객체 생성

print(tv1.get_channel())
print(tv1.__channel())
