import requests
from datetime import datetime
import csv
import os
import time


csv_directory = 'csv_data'
os.makedirs(csv_directory, exist_ok=True)
current_timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M")
csv_file = f'{csv_directory}/ip_log_{current_timestamp}.csv'

if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Date', 'Time', 'IP address'])



duration = 30  # Change the runtime duration as needed,  in seconds
delay = 10     # Change the delay between each request,  in seconds
start_time = time.time()


while True:
    def record_ip():
        data = requests.get('https://ipinfo.io/ip')
        ip_address = data.text
        now = datetime.now()
        today = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")
        with open(csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([today, current_time, ip_address])
    if (time.time() - start_time) < duration:
        record_ip()
        time.sleep(delay)
    else:
        record_ip()
        break
