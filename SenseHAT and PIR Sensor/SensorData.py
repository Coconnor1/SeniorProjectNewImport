# Imports the senseHat module
from sense_hat import SenseHat

# Imports the CSV writer and datetime module
from csv import writer
import time
from datetime import datetime

# Creates sensehat variable
sense= SenseHat()

# Creates variable to read current time
timestamp=datetime.now()

# Delay log for 3 seconds
delay=3

# Function to read the sensor data from sensehat
def get_sense_data():
    sense_data=[]

    # Get Temp
    temp = sense.get_temperature()
    # Get humidity
    humidity = sense.get_humidity()
    # Get Pressure
    pressure = sense.get_pressure()

    # Appends data to the end of sense_data list with specific formatting
    sense_data.append("Temperature: %.2f C" % temp)
    sense_data.append("Humidity: %.2f %%rH" % humidity)
    sense_data.append("Pressure: %s Millibars" % pressure)

    sense_data.append(datetime.now())

    return sense_data

# Open / Creates sensor_data.csv file and creates the log file header
with open('sensor_data.csv', 'a',newline='') as file:

    data_writer=writer(file)
    data_writer.writerow(['temp','\t\t\t\t humidity','\t\t\t\t pressure','\t\t\t\t timestamp'])

    # While True loop to write sense_data to log file every 3 seconds
    while True:
        sense_data=get_sense_data()
        timestamp_difference=sense_data[-1] - timestamp
        if timestamp_difference.seconds>delay:

            # Saves the data in sense_data.csv and also prints to the terminal
            data_writer.writerow(sense_data)
            print(sense_data)
            # Updates timestamp variable after data is written
            timestamp=datetime.now()
