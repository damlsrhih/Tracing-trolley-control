import socket #加载模块
import RPi.GPIO as GPIO
import moto
import trace
import _thread


GPIO.setmode(GPIO.BCM)
moto.moto_init()
trace.trace_init()

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #使用udp协议的套接字
s.bind(('192.168.137.23',8888)) #绑定地址

try:
    while True:
        msg = s.recvfrom(1024) #接收消息
        string = msg[0].decode('utf-8') #将二进制转换为字符串
        print(string)
        if string == 'GO':
            moto.go()
            pass
        elif string == 'BACK':
            moto.back()
            pass
        elif string == 'LEFT':
            moto.left()
            pass
        elif string == 'RIGHT':
            moto.right()
            pass
        elif string == 'STOP':
            moto.stop()
            pass
        elif string == 'TraceOn':
            trace.trace_start()
            _thread.start_new_thread(trace.trace,())
            pass
        elif string == 'TraceOff':
            trace.trace_stop()
            pass
        else:
            print("未知命令")
            pass
except KeyboardInterrupt:
    s.close()
    moto.moto_del()
    GPIO.cleanup()