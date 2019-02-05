#!/usr/bin/env python
 
import signal
import time
 
# define the singal handler to modify standard behaviour when the process catches the SIGINT signal (CTRL-C)
def sigint_handler(signum, frame):
    print 'Stop pressing the CTRL+C!'

#Install the signal handler
signal.signal(signal.SIGINT, sigint_handler)
 
# just an infinite loop that prints . and then sleeps for 1sec
while True:
    print '.'
    time.sleep(1)
 
