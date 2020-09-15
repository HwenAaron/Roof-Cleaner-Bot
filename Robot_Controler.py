from gpiozero import Servo
import RPi.GPIO as GPIO
import pigpio
from time import sleep 
import sys, tty, termios, time

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
 
#PiGPIO variables
pi = pigpio.pi()
user_gpio = 0-31.
pulsewidth = 0, 500-2500
 
# servo pins and vars
global vpwm
global hpwm
 
vpwm = 1950
hpwm = 1900
 
global nvpwm
global nhpwm
 
nvpwm = 1950
nhpwm = 1900

v_pin = 5
h_pin = 6
s_pin = 2
 
GPIO.setup(v_pin, GPIO.OUT)
GPIO.setup(h_pin, GPIO.OUT)
GPIO.setup(s_pin, GPIO.OUT) 

#Motor pin and vars
in1 = 27
in2 = 22
enA = 17
in3 = 9
in4 = 11
enB = 10

GPIO.setmode(GPIO.BCM)
#motor2
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
p1=GPIO.PWM(enB,1000)
p1.start(25)

#motor 1
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
p=GPIO.PWM(enA,1000)
p.start(25)
print("\n")
print("Starting...")
print("w/s for excelerate")
print("a/s for turning")
print("o/l for pan up and down")
print("k/; for pan left and right")
print("spacebar to spray")
print("q to quit the program")


 
def look_down():      #moves shoulder servo up
    global vpwm
    global nvpwm
    vpwm = nvpwm
    pi.set_servo_pulsewidth(v_pin, vpwm)
    nvpwm = vpwm - 20
    if nvpwm < 1000:
        nvpwm = 1000
    
def look_up():    #Moves shoulder Servo down
    global vpwm
    global nvpwm
    vpwm = nvpwm
    pi.set_servo_pulsewidth(v_pin, vpwm)
    nvpwm = vpwm   + 20
    if nvpwm > 2500:
        nvpwm = 2500
    
def pan_left():         #Moves elbow servo Up
    global hpwm
    global nhpwm
    hpwm = nhpwm
    pi.set_servo_pulsewidth(h_pin, hpwm)
    nhpwm = hpwm - 20
    if nhpwm < 1000:
        nhpwm = 1000
 
def pan_right():       #Moves elbow servo down
    global hpwm
    global nhpwm
    hpwm = nhpwm
    pi.set_servo_pulsewidth(h_pin, hpwm)
    nhpwm = hpwm + 20
    if nhpwm > 2500:
        nhpwm = 2500
 
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
    
delay = .3

while True:
    # Keyboard character retrieval method is called and saved
    # into variable
    char = getch()
 
    # The shoulder will move down when the "w" key is pressed
    if(char == "o"):
        look_up()
 
    # The shoulder will move up when the "s" key is pressed
    if(char == "l"):
        look_down()
 

    # The "r" key will move the elbow down
    if(char == ";"):
        pan_right()
 
    # The "f" key will move the elbow up
    if(char == "k"):
        pan_left()
    
    if(char == " "):
        pi.set_servo_pulsewidth(s_pin, 1000)
        pi.set_servo_pulsewidth(s_pin, 2500)
        pi.set_servo_pulsewidth(s_pin, 1000)
        pi.set_servo_pulsewidth(s_pin, 2500)
        
    

  
        
    # The "x" key will break the loop and exit the program
    if(char == "q"):
        print("Program Ended")
        break
    
    if (char == 's'):
        p.ChangeDutyCycle(50)
        p1.ChangeDutyCycle(50)
        
        GPIO.output(in1, 1)
        GPIO.output(in2, 0)
        GPIO.output(in3, 1)
        GPIO.output(in4, 0)

        time.sleep(delay)
    
    if (char == 'w'):
        p.ChangeDutyCycle(50)
        p1.ChangeDutyCycle(50)
        
        GPIO.output(in1, 0)
        GPIO.output(in2, 1)
        GPIO.output(in3, 0)
        GPIO.output(in4, 1)

        time.sleep(delay)

    if (char == 'a'):
        p.ChangeDutyCycle(50)
        p1.ChangeDutyCycle(50)
        
        GPIO.output(in1, 0)
        GPIO.output(in2, 1)
        GPIO.output(in3, 1)
        GPIO.output(in4, 0)

        time.sleep(delay)

    if (char == 'd')
        p.ChangeDutyCycle(50)
        p1.ChangeDutyCycle(50)
        
        GPIO.output(in1, 1)
        GPIO.output(in2, 0)
        GPIO.output(in3, 0)
        GPIO.output(in4, 1)

        time.sleep(delay)
    p.ChangeDutyCycle(0)
    p1.ChangeDutyCycle(0)
    
    char = ""
 
# Program will cease all GPIO activity before terminating
GPIO.cleanup()


