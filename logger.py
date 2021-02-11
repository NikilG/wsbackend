import logging

#logging.disable()

#Create and configure logging
logging.basicConfig(filename="logs/tracking.log", format='%(asctime)s %(levelname)s %(message)s', filemode='w')

#Creating an Object
log = logging.getLogger()

#Setting the thresold of of logger to DEBUG
log.setLevel(logging.DEBUG)

log.info("Test Info")

