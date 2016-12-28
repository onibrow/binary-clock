import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

while(True):
    HOUR = int(time.strftime("%H"))
    MIN  = int(time.strftime("%M"))

    #########
    # ROW 0 #
    #########

    row0 = HOUR // 10

    row02 = row0 // 2
    row01 = row0 - row02 * 2

    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    GPIO.output(21, row02)
    GPIO.output(23, row01)

    #########
    # ROW 1 #
    #########

    row1 = HOUR % 10

    row14 = row1 // 8
    row13 = (row1 - row14 * 8) // 4
    row12 = (row1 - row14 * 8 - row13 * 4) // 2
    row11 = (row1 - row14 * 8 - row13 * 4 - row12 * 2)

    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)

    GPIO.output(31, row14)
    GPIO.output(33, row13)
    GPIO.output(35, row12)
    GPIO.output(37, row11)
    #########
    # ROW 2 #
    #########

    row2 = MIN // 10

    row23 = row2  // 4
    row22 = (row2 - row23 * 4) // 2
    row21 = (row2 - row23 * 4 - row22 * 2)

    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)

    GPIO.output(22, row23)
    GPIO.output(24, row22)
    GPIO.output(26, row21)

    #########
    # ROW 3 #
    #########

    row3 = MIN % 10

    row34 = row3 // 8
    row33 = (row3 - row34 * 8) // 4
    row32 = (row3 - row34 * 8 - row33 * 4) // 2
    row31 = (row3 - row34 * 8 - row33 * 4 - row32 * 2)

    GPIO.setup(32, GPIO.OUT)
    GPIO.setup(36, GPIO.OUT)
    GPIO.setup(38, GPIO.OUT)
    GPIO.setup(40, GPIO.OUT)

    GPIO.output(32, row34)
    GPIO.output(36, row33)
    GPIO.output(38, row32)
    GPIO.output(40, row31)

    time.sleep(1)

############
# EPILOGUE #
############

time.sleep(1)

GPIO.output(21, 0)
GPIO.output(23, 0)
GPIO.output(31, 0)
GPIO.output(33, 0)
GPIO.output(35, 0)
GPIO.output(37, 0)
GPIO.output(22, 0)
GPIO.output(24, 0)
GPIO.output(26, 0)
GPIO.output(32, 0)
GPIO.output(36, 0)
GPIO.output(38, 0)
GPIO.output(40, 0)

