# # 定时器初始化。period:单位为 ms（毫秒）； mode：2 种工作模式，Timer.ONE_SHOT（执行一次）、Timer.PERIODIC（周期性）；callback:定时器中断后的回调函数。
from machine import Pin, Timer
import time

led = Pin(25, Pin.OUT)
io = Pin(2, Pin.OUT)
tim1 = Timer()
tim2 = Timer()
tim3 = Timer()
tim4 = Timer()
tim5 = Timer()
tim6 = Timer()
tim7 = Timer()


def tick(timer):
    global led
    led.toggle()
    print("tick", time.time())


def label1(timer):
    print("label1", time.time())


def label2(timer):
    print("label2", time.time())
    global io
    io.value(1)
    for i in range(5000):
        pass
    io.value(0)
    for i in range(5000):
        pass


def label3(timer):
    print("label3", time.time())


def label4(timer):
    print("label4", time.time())


tim1.init(freq=2.5, mode=Timer.ONE_SHOT, callback=tick)
tim2.init(freq=2.5, mode=Timer.ONE_SHOT, callback=label1)
tim3.init(freq=2.5, mode=Timer.ONE_SHOT, callback=label2)
tim4.init(freq=2.5, mode=Timer.ONE_SHOT, callback=label3)
tim5.init(freq=2.5, mode=Timer.ONE_SHOT, callback=label4)
tim6.init(freq=2.5, mode=Timer.ONE_SHOT, callback=label2)
tim7.init(freq=2.5, mode=Timer.ONE_SHOT, callback=label2)
