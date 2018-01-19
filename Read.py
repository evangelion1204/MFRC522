#!/usr/bin/env python
# -*- coding: utf8 -*-

import time
import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    # Scan for cards    
    time.sleep(1)
    
    (status,TagType,ATQA) = MIFAREReader.Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status != MIFAREReader.MI_OK:
        continue

    print status
    print ATQA

    ATQAWord = (ATQA[0] | ATQA[1] << 8) 
    print "Card detected %04x" % ATQAWord
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.AnticollLevel(1)

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        # Print UID
        # print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        print MIFAREReader.SelectTagLevel(1, uid)
        (status2,uid2) = MIFAREReader.AnticollLevel(2)
        print MIFAREReader.SelectTagLevel(2, uid2)

        print uid[1:4] + uid2[0:4]

        # Authenticate
        # status = MIFAREReader.Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
        MIFAREReader.Read(0)
        MIFAREReader.Read(4)
        MIFAREReader.Read(8)

        # Variable for the data to write
        data = []

            # Fill the data with 0xFF
        # for x in range(0,16):
        #     data.append(x)
        #
        # MIFAREReader.Write(4, data)

        MIFAREReader.WriteString(4, 'Hallo World')

        MIFAREReader.Halt()

        # Check if authenticated
        # if status == MIFAREReader.MI_OK:
        #     MIFAREReader.Read(8)
        #     MIFAREReader.StopCrypto1()
        # else:
        #     print "Authentication error"

