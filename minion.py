import pyupm_l298 as upm_l298
import pyupm_servo as Servo
import random
import serial
from threading import Thread
import time

motor_A = upm_l298.L298(9, 2, 4)
motor_B = upm_l298.L298(6, 8, 12)

current_head = 90
current_left = 0
current_right = 180

last_head = 0
last_arm = 0

servo_head = Servo.ES08A(3)
servo_head.setAngle(current_head)
servo_left = Servo.ES08A(5)
servo_left.setAngle(current_left)
servo_right = Servo.ES08A(10)
servo_right.setAngle(current_right)

bluetooth = serial.Serial('/dev/ttyS0', 9600, timeout=0)


def forward():
    motor_A.setSpeed(100)
    motor_B.setSpeed(100)

    motor_A.setDirection(upm_l298.L298.DIR_CW)
    motor_B.setDirection(upm_l298.L298.DIR_CW)

    motor_A.enable(True)
    motor_B.enable(True)


def backward():
    motor_A.setSpeed(100)
    motor_B.setSpeed(100)

    motor_A.setDirection(upm_l298.L298.DIR_CCW)
    motor_B.setDirection(upm_l298.L298.DIR_CCW)

    motor_A.enable(True)
    motor_B.enable(True)


def left():
    motor_A.setSpeed(10)
    motor_B.setSpeed(100)


def right():
    motor_B.setSpeed(10)
    motor_A.setSpeed(100)


def stopped():
    motor_A.setSpeed(0)
    motor_B.setSpeed(0)

    motor_A.setDirection(upm_l298.L298.DIR_NONE)
    motor_B.setDirection(upm_l298.L298.DIR_NONE)

    motor_A.enable(False)
    motor_B.enable(False)


def head_left():
    turn = head_turning_left()
    while turn:
        turn = head_turning_left()
        time.sleep(0.1)


def head_right():
    turn = head_turning_right()
    while turn:
        turn = head_turning_right()
        time.sleep(0.1)


def head_center():
    global current_head

    if current_head > 90:
        while current_head > 90:
            head_turning_left()
            time.sleep(0.1)
    elif current_head < 90:
        while current_head < 90:
            head_turning_right()
            time.sleep(0.1)


def head_turning_left():
    global current_head

    if current_head <= 0:
        servo_head.setAngle(0)
        return False
    else:
        current_head -= 20
        servo_head.setAngle(current_head)
        return True


def head_turning_right():
    global current_head

    if current_head >= 180:
        servo_head.setAngle(180)
        return False
    else:
        current_head += 20
        servo_head.setAngle(current_head)
        return True


def left_up():
    global current_left

    current_left = 180
    servo_left.setAngle(current_left)


def left_down():
    global current_left

    current_left = 0
    servo_left.setAngle(current_left)


def left_center():
    global current_left

    current_left = 120
    servo_left.setAngle(current_left)


def left_turning_up():
    global current_left

    if current_left >= 180:
        servo_left.setAngle(180)
        return False
    else:
        current_left += 10
        servo_left.setAngle(current_left)
        return True


def left_turning_down():
    global current_left

    if current_left <= 0:
        servo_left.setAngle(0)
        return False
    else:
        current_left -= 10
        servo_left.setAngle(current_left)
        return True


def right_up():
    global current_right

    current_right = 0
    servo_right.setAngle(current_right)


def right_down():
    global current_right

    current_right = 180
    servo_right.setAngle(current_right)


def right_center():
    global current_right

    current_right = 70
    servo_right.setAngle(current_right)


def right_turning_up():
    global current_right

    if current_right <= 0:
        servo_right.setAngle(0)
        return False
    else:
        current_right -= 10
        servo_right.setAngle(current_right)
        return True


def right_turning_down():
    global current_right

    if current_right >= 180:
        servo_right.setAngle(180)
        return False
    else:
        current_right += 10
        servo_right.setAngle(current_right)
        return True


def head():
    global last_head

    choice = random.randint(1, 4)
    while choice == last_head:
        choice = random.randint(1, 4)

    if choice == 1:
        head_center()
        time.sleep(0.5)
        head_left()
        time.sleep(0.5)
        head_right()
        time.sleep(0.5)
        head_left()
        time.sleep(0.5)
        head_right()
        time.sleep(0.5)
        head_center()

    elif choice == 2:
        head_center()
        time.sleep(0.5)
        head_left()
        time.sleep(0.5)
        head_center()
        time.sleep(0.5)
        head_left()
        time.sleep(0.5)
        head_center()
        time.sleep(0.5)

    elif choice == 3:
        head_center()
        time.sleep(0.5)
        head_right()
        time.sleep(0.5)
        head_center()
        time.sleep(0.5)
        head_right()
        time.sleep(0.5)
        head_center()
        time.sleep(0.5)

    elif choice == 4:
        head_center()
        time.sleep(0.5)
        head_left()
        time.sleep(1)
        head_center()
        time.sleep(0.5)
        head_right()
        time.sleep(1)
        head_center()

    last_head = choice


def arm():
    global last_arm

    choice = random.randint(1, 5)
    while choice == last_arm:
        choice = random.randint(1, 5)

    if choice == 1:
        left_up()
        right_up()
        time.sleep(0.5)
        left_down()
        right_down()
        time.sleep(0.5)
        left_up()
        right_up()
        time.sleep(0.5)
        left_down()
        right_down()
        time.sleep(0.5)

    elif choice == 2:
        left_up()
        right_down()
        time.sleep(0.5)
        left_center()
        right_center()
        time.sleep(0.5)
        left_down()
        right_up()
        time.sleep(0.5)
        left_center()
        right_center()
        time.sleep(0.5)

    elif choice == 3:
        left_up()
        right_up()
        time.sleep(0.5)
        left_center()
        right_center()
        time.sleep(0.5)
        left_up()
        right_up()
        time.sleep(0.5)
        left_center()
        right_center()
        time.sleep(0.5)

    elif choice == 4:
        left_down()
        right_down()
        time.sleep(0.5)
        left_center()
        right_center()
        time.sleep(0.5)
        left_down()
        right_down()
        time.sleep(0.5)
        left_center()
        right_center()
        time.sleep(0.5)

    elif choice == 5:
        left_center()
        right_center()
        time.sleep(0.5)
        left_up()
        right_down()
        time.sleep(0.5)
        left_down()
        right_up()
        time.sleep(0.5)
        left_center()
        right_center()
        time.sleep(0.5)
        left_up()
        right_down()
        time.sleep(0.5)
        left_down()
        right_up()
        time.sleep(0.5)

    last_arm = choice


def movement():
    a = Thread(target=arm)
    h = Thread(target=head)
    a.start()
    h.start()


while True:
    command = bluetooth.read()

    if command == 'f':
        print("Forward")
        forward()
        time.sleep(0.2)

    elif command == 'b':
        print("Backward")
        backward()
        time.sleep(0.2)

    elif command == 'l':
        print("Left")
        left()
        time.sleep(0.2)

    elif command == 'r':
        print("Right")
        right()
        time.sleep(0.2)

    elif command == 's':
        print("Stopped")
        stopped()
        time.sleep(0.2)

    elif command == 'h':
        print("Head")
        head()
        time.sleep(0.2)
    elif command == 'a':
        print("Arm")
        arm()
        time.sleep(0.2)
    elif command == 'm':
        print("Movement")
        movement()
        time.sleep(0.2)
