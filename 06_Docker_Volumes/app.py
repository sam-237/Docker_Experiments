import time
import logging

# Set up logging
logging.basicConfig(filename='/logs/app.log', level=logging.INFO)

while True:
    logging.info(f'Logging a new entry at {time.ctime()}')
    time.sleep(5)  # Simulate a delay of 5 seconds between log entries