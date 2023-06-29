#红外线虚拟机模块
import RPi.GPIO as GPIO
import moto

#设置引脚 为输入模式
Trace = [12,16,20,21]

#循环标志
flag = False

def trace_init():
    GPIO.setup(Trace,GPIO.IN)

def trace_start():
    global flag
    flag = True

def trace_stop():
    global flag
    flag = False

def read_trace_statu():
    R1 = GPIO.input(Trace[0])
    R2 = GPIO.input(Trace[1])
    R3 = GPIO.input(Trace[2])
    R4 = GPIO.input(Trace[3])
    return R1,R2,R3,R4

#寻迹逻辑
def trace():
    global flag
    while flag:
        R1,R2,R3,R4 = read_trace_statu()
        if R1 == GPIO.LOW and R2 == GPIO.HIGH and R3 == GPIO.HIGH and R4 == GPIO.LOW:
            moto.go()
            print("寻迹-直行")
        elif R1 == GPIO.HIGH and R2 == GPIO.HIGH and R3 == GPIO.HIGH and R4 == GPIO.HIGH:
            moto.stop()
            print("寻迹-抵达终点,停止")
        elif R1 == GPIO.HIGH and R2 == GPIO.HIGH and R3 == GPIO.HIGH and R4 == GPIO.LOW:
            moto.left()
            print("寻迹-向左调整")
        elif R1 == GPIO.HIGH and R2 == GPIO.HIGH and R3 == GPIO.LOW and R4 == GPIO.LOW:
            moto.left()
            print("寻迹-向左调整")
        elif R1 == GPIO.LOW and R2 == GPIO.HIGH and R3 == GPIO.HIGH and R4 == GPIO.HIGH:
            moto.right()
            print("寻迹-向右调整")
        elif R1 == GPIO.LOW and R2 == GPIO.LOW and R3 == GPIO.HIGH and R4 == GPIO.HIGH:
            moto.right()
            print("寻迹-向右调整")
        elif R1 == GPIO.LOW and R2 == GPIO.LOW and R3 == GPIO.LOW and R4 == GPIO.LOW:
            moto.stop()
            print("寻迹-跑出轨道,停止")
        else:
            print("unknown")
    moto.stop()
    print("寻迹-小车停止")