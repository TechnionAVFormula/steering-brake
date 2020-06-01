import sys
sys.path.append("C:/temp/Canlib_SDK_v5.9/Samples/Python")
from canlib import canlib, Frame
from canlib.canlib import ChannelData
import time



channel = 0
ch = canlib.openChannel(channel)

ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
ch.setBusParams(canlib.canBITRATE_1M)
ch.busOn()
#frame = Frame(0,bytearray(b'\x01\x00'))
#frame = Frame(0,[1,3,3])
#ch.write(frame)


# CAN state -> operetional id=0,cs=1,nod_id=1
ch.write_raw(0,[1,1])

# PDO1: controlword -> shotdown (to ready to switch on)
ch.write_raw(512+1,[6,0])

# pp = [136,19,0,0] # set position 5000
#pp = [0x1E,00,0,0] # set position 30 angle
#pp = [0xFF,0xFF,0xFF,0xE2] # set position -30 angle


for i in range(9):
   controlword = [127,0] # move immidiatly and relative
   if i == 0:
      pp = [0x0F,0,0,0]
   elif i%2 == 0:
      pp = [0x1E,00,0,0] # set position 30 angle
   else:
      pp = [0xFF,0xFF,0xFF,0xE2] # set position -30 angle
   ch.write_raw(768+1,controlword + pp)
   ch.write_raw(512+1,[111,0])
   time.sleep(2)
    
    

