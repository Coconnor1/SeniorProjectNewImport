import RPi.GPIO as GPIO
from datetime import datetime
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import base64
import time
from datetime import datetime

# local image from drive
file = 'O:\SenProject\GP.jpg'
image = open(file, 'rb')
image_read = image.read()
image1 = base64.encodebytes(image_read)


# Pushsafer API endpoint
url = "https://www.pushsafer.com/api"


# Set up GPIO for PIR sensor
PIR_PIN = 4  # GPIO pin connected to PIR sensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# Function to send Pushsafer notifications
def send_notification(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    post_fields = {
        "t" : 'Security ALert',
        "m" : f'{message} \nTimestamp: {timestamp} ',
        "s" : 25,
        "v" : 3,
        "i" : 5,
        "c" : '#FF0000',
        "d" : 'gs5549',
        "pr": "2",
        "u" : 'https://www.pushsafer.com',
        "ut" : 'Open Pushsafer',
        "k" : 't8qbIf0FBOmSDvp5spEN',
        "p" : 'data:image/jpeg;base64,'+str(image1.decode('ascii')),
    }

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)

try:
    print("PIR Sensor initializing... Press CTRL+C to exit.")
    time.sleep(2)  # Wait for PIR sensor to initialize

    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
            send_notification("Motion has been detected!")
            time.sleep(10)  # Wait before detecting another motion to avoid multiple notifications
        else:
            print("No motion detected.")
        time.sleep(1)

except KeyboardInterrupt:
    print("Program exited.")
    GPIO.cleanup()  # Clean up GPIO pins
