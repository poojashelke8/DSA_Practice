# class Device:
#     def __init__(self,name):
#         print("inisde the init")
#         self.name = name

#     def show(self):
#         print("Device",self.name)

# d1 = Device("laptop")
# d2 = Device("tab")

# d1.show()
# d2.show()


# from threading import Thread
# from multiprocessing import Process
# from time import sleep

# def hello():
#     for i in range(5):
#         print("Hello",i+1)
#         sleep(0.3)

# def hi():
#     for i in range(5):
#         print("hi",i+1)
#         sleep(0.3)


# if __name__ == '__main__':

#     t1 = Thread(target=hello)
#     # sleep(0.2)
#     t2 = Thread(target=hi)

#     t1.start()
#     t2.start()

#     # wait for them to complete once done join them

#     t1.join()
#     t2.join()

#     print("Byeee")

#     t1 = Process(target=hello)
#     # sleep(0.2)
#     t2 = Process(target=hi)

#     t1.start()
#     t2.start()

#     # wait for them to complete once done join them

#     t1.join()
#     t2.join()

#     print("Byeee")
class Demo:
    def show(self):
        print("in demo")

class value:
    def show(self):
        print("in value")

class temp(Demo):
    # pass
    def show(self):
        print("in temp")

o = temp()
o.show()


# 
class Workload:
    def __init__(self,duration,workload_type):
        self.duration = duration
        self.w_type = workload_type
    
    def start_fn(self):
        print (f"dd duration = {self.duration} workload_type={self.w_type} bs=1M")
    
    def display(self):
         print("Workload type:", self.w_type)
         
class vdbench(Workload):
    def __init__(self,duration,w_type,eda):
        super().__init__(duration,w_type)
        self.EDA = eda
            
    def start_ch(self):
        super().display()
        super().start_fn()
        print (f"dd duration = {self.duration} workload_type={self.w_type} EDA={self.EDA} bs=1M")
        
w1 = Workload(10,"abc")
print(w1.duration)
print(w1.w_type)

res = w1.start_fn()
# res2 = w1.display()
ch = vdbench(50,"xyz","profile1")
ch.start_ch()
# print("start",res)
