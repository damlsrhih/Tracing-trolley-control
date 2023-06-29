#完成电机的前后左右的方向切换
import RPi.GPIO as GPIO

#电机对应的引脚,注意确定转向
L = [19,26]
R = [13,6]
#pwm的对象
pL = [0,0]
pR = [0,0]

#设置方向标志是用英文的单词进行标志
dir_flag = 'stop'
#设置启动的标志
start_flag = 0

#电机初始化
def moto_init():
    GPIO.setup(L,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(R,GPIO.OUT,initial = GPIO.LOW)
    pL[0] = GPIO.PWM(L[0],50) #将控制引脚设置为pwm模式
    pL[1] = GPIO.PWM(L[1],50) #将控制引脚设置为pwm模式
    pR[0] = GPIO.PWM(R[0],50) #将控制引脚设置为pwm模式
    pR[1] = GPIO.PWM(R[1],50) #将控制引脚设置为pwm模式
    pL[0].start(0)
    pL[1].start(0)
    pR[0].start(0)
    pR[1].start(0)


#向前的函数
def go():
    dir_flag = 'go'
    pL[0].ChangeDutyCycle(30)
    pR[0].ChangeDutyCycle(30)
    pL[1].ChangeDutyCycle(0)
    pR[1].ChangeDutyCycle(0)

#向后的函数
def back():
    dir_flag = 'back'
    pL[0].ChangeDutyCycle(0)
    pR[0].ChangeDutyCycle(0)
    pL[1].ChangeDutyCycle(30)
    pR[1].ChangeDutyCycle(30)

#向左的函数
def left():
    dir_flag = 'left'
    pL[0].ChangeDutyCycle(0)
    pL[1].ChangeDutyCycle(30)
    pR[0].ChangeDutyCycle(30)
    pR[1].ChangeDutyCycle(0)

#向右的函数
def right():
    dir_flag = 'right'
    pL[0].ChangeDutyCycle(30)
    pL[1].ChangeDutyCycle(0)
    pR[0].ChangeDutyCycle(0)
    pR[1].ChangeDutyCycle(30)

#停止的函数
def stop():
    dir_flag = 'stop'
    pL[0].ChangeDutyCycle(0)
    pL[1].ChangeDutyCycle(0)
    pR[0].ChangeDutyCycle(0)
    pR[1].ChangeDutyCycle(0)

#电机清除状态
def moto_del():
    stop()
    pL[0].stop()
    pL[1].stop()
    pR[0].stop()
    pR[1].stop()