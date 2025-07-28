## modi 기본 설정
import modi_plus
import time
bundle = modi_plus.MODIPlus()
bundle.modules
## led 다루기
led = bundle.leds[0] #여러개의 led module 중 첫번째 것을 설정함

led.red = 100
time.sleep(3)
led.red = 0
time.sleep(1) #동일한 방법으로 led.green / led.blue 로 rgb를 조절할 수 있음
led.turn_on() #기본적으로 흰색을 킴
time.sleep(2)
led.turn_off()
time.sleep(1)
led.rgb = (100,0,100) #한꺼번에 rgb를 설정
time.sleep(2)
led.turn_off() #
## display 다루기
display = bundle.displays[0] #마찬가지

display.text = "Hello Modi"
time.sleep(3)
display.reset()
time.sleep(1)
## speaker 다루기
speaker = bundle.speakers[0]

speaker.tune = 3951, 50 #주파수, 음량
time.sleep(2)
speaker.frequency = 1975 #주파수만 할당
time.sleep(2)
speaker.volume = 100 #음량을 할당
time.sleep(2)
speaker.reset()
## motor 다루기
motor = bundle.motors[0]

motor.angle = 0,10 # 모터 각도, 속도
time.sleep(2)

motor.speed(50) # -100 ~ 100 범위 설정
