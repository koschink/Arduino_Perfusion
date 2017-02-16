# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 23:06:06 2016

@author: Kay Schink
"""
import time
import serial
import pyfirmata


try:
    board.exit()

except NameError:
    ""    
finally:
    ""

board = pyfirmata.Arduino('COM4')
counter = 0

# Setup the digital pin
digital_0 = board.get_pin('d:12:i')

it = pyfirmata.util.Iterator(board)
it.start()
digital_0.enable_reporting()

board_closed=False


try:
    while (True):
        if str(digital_0.read()) == 'True':
        #    for i in range(0,100):
           print "Button pressed"
           for j in range(2,9):
                board.digital[j].write(1)
                time.sleep(0.09)
                board.digital[j].write(0)
                #time.sleep(0.5)
           for j in range(9,2,-1):
                board.digital[j].write(1)
                time.sleep(0.09)
                board.digital[j].write(0)

                #time.sleep(0.5)

except KeyboardInterrupt:
           print "Execution halted, closing all ports"    
           for k in range(2,9): 
                
               board.digital[k].write(0)    
           board.exit()
           board_closed=True
           print "Board unloaded"
#    #print "Button state: %s" % digital_0.read()
#    # The return values are: True False, and None
#    if str(digital_0.read()) == 'True':
#        print "Button pressed"
#    elif str(digital_0.read()) == 'False':
#        print "Button not pressed"
#    else: 
#        print "Button was never pressed"
#    board.pass_time(0.1)
#if board_closed == False:
try:
    ""
    board.exit()

except serial.SerialException:
    print "Port already closed"




#
#while counter < 1 :
#    #pin13 = board.get_pin('d:13:i')    
#    print board.digital[13].mode()
##    if board.digital[13].read()== 1:
##        try:
##        #    for i in range(0,100):
##            for j in range(2,10)
##                board.digital[j].write(1)
##                time.sleep(0.5)
##                board.digital[j].write(0)
##                #time.sleep(0.5)
##        except KeyboardInterrupt:
##            print "Execution halted, closing all ports"    
##            for j in range(2,10): 
##                
##                board.digital[j].write(0)    
##                board.exit()
#
# 
#board.exit()
