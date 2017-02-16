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

board = pyfirmata.Arduino('COM3')
counter = 0

# Setup the digital pin on the arduino
digital_0 = board.get_pin('d:12:i')
# this sets up the board 
it = pyfirmata.util.Iterator(board)
it.start()
digital_0.enable_reporting()

print "Board opened"
board_closed=False

time.sleep(2)
print "Ready to start perfusion, activate switch to run"
print ""

number_of_bursts = 1
do_recovery = False
do_burst = True


settings_1 = {"bursts": 1, "recovery" : True, "burst":False }

settings_2 = {"bursts": 5, "recovery" : True, "burst":True }


pause_at = [5,10,15,20]  
time.sleep(2)
counter = 0
number_of_loops = 25
was_active = False




def cycle_port(port_number, duration):    
    board.digital[port_number+1].write(1)
    print "Port" + str(port_number) +" active"
    time.sleep(duration)
    board.digital[port_number+1].write(0)
    
    
    
cycle_length = 10






try:
    while (True): # continuous loop, runs forever
        if str(digital_0.read()) == 'False':     # read out the manual switch       
            if was_active == True: # this deals with neutralizing after the switch was flipped to "off"     
                board.digital[2].write(1) # open neutral buffer
                print "Neutralizing"
                time.sleep(15)
                board.digital[2].write(0) # close neutral buffer
                print "Run finished"
                was_active = False
                board.digital[3].write(0) # turn all ports off
                board.digital[2].write(0) # turn all ports off
                counter = 0 # resets the number of loops run so far
                
        if str(digital_0.read()) == 'True': # manual switch flipped to on
            if counter < number_of_loops:
                counter = counter+1
                was_active = True
                
            #    for i in range(0,100):
                print "Perfusion running"
                print "Loop " + str(counter)
                for i in range(0,number_of_bursts):
                    print i
                    cycle_port(2,cycle_length)
                    cycle_port(1,cycle_length)
                    
                if do_burst:
                    time.sleep(30)
                

                
                if do_recovery: # allows cells to recover after a number of cycles
                    if counter in pause_at:
                        print "____________"
                        print "Recovering"
                        print "____________"
                        time.sleep(30)

                
                
            else:
                print "Maximum number of loops reached"
                board.digital[3].write(0)
                board.digital[2].write(0)
                time.sleep(2)
                

        
            

                #time.sleep(0.5)

except KeyboardInterrupt:
           print "Execution halted, closing all ports"    
           board.digital[3].write(0)
           board.digital[2].write(0) 
           board.exit()
           board_closed=True
           print "Board unloaded"

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
