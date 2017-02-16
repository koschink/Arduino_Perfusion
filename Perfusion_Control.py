# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 12:27:29 2016

@author: kaysch
Controlling Perfusion system by Arduino



"""


import time
import serial
import pyfirmata




ActivePorts = [2,1]

Time_active = [5,5]

cycles = 25
try:
    board.exit()

except NameError:
    ""    
finally:
    ""

board = pyfirmata.Arduino('COM3')
counter = 0

# Setup the digital pin
digital_0 = board.get_pin('d:12:i')

it = pyfirmata.util.Iterator(board)
it.start()
digital_0.enable_reporting()

board_closed=False


try:
#    while (True):
#        if str(digital_0.read()) == 'True':
#        #    for i in range(0,100):
#           print "Button pressed"
    t = 0
    while t <cycles:
        t = t+1
        for i, j in enumerate(ActivePorts):
               board.digital[j+1].write(1)
               print "Cycle " + str(t)
               print "Port active: " + str(j+1) 
               time.sleep(Time_active[i])
               board.digital[j+1].write(0)
    board.digital[2].write(1)
    time.sleep(10)
    board.digital[2].write(0)
    print "Cycle finished"
          # time.sleep(Time_active[i])
            
          # board.digital[j+1].write(0)
        #time.sleep(0.5)
   
        #time.sleep(0.5)

except KeyboardInterrupt:
           print "Execution halted, closing all ports"    
           board.digital[2].write(1)
           time.sleep(10)
           board.digital[2].write(0)
           for k in range(2,9): 
               board.digital[k].write(0)    
           board.exit()
           board_closed=True
           print "Board unloaded"
##    #print "Button state: %s" % digital_0.read()
##    # The return values are: True False, and None
##    if str(digital_0.read()) == 'True':
##        print "Button pressed"
##    elif str(digital_0.read()) == 'False':
##        print "Button not pressed"
##    else: 
##        print "Button was never pressed"
##    board.pass_time(0.1)
##if board_closed == False:
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
#
