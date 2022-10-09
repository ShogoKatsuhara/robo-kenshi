from RPi import GPIO

A=2
B=3

GPIO.setmode(GPIO.BCM)
GPIO.setup(A,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(B,GPIO.IN,pull_up_down=GPIO.PUD_UP)

print(GPIO.input(A))
print(GPIO.input(B))