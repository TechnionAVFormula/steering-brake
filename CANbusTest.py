from canlib import canlib, Frame
import numpy as np

# int.to_bytes(length, byteorder, *, signed=False),
# int.from_bytes(bytes, byteorder, *, signed=False),
# int.bit_length()

# identifier
# node id 7 bits (0-6)
# function code 4 bits (7-10)

# function codes
class FunctionCodes:
    TPDO1 = 0b0011
    RPDO1 = 0b0100
    TPDO2 = 0b0101
    RPDO2 = 0b0110
    TPDO3 = 0b0111
    RPDO3 = 0b1000
    TPDO4 = 0b1001
    RPDO4 = 0b1010

# identifier for node id=0
class BaseIdentifiers:
    TPDO1 = 384
    RPDO1 = 512
    TPDO2 = 640
    RPDO2 = 768
    TPDO3 = 896
    RPDO3 = 1024
    TPDO4 = 1152
    RPDO4 = 1280

# state machine commands
STM_COMMANDS = {'shutdown':0b0110, 
                'switch_on':0b1110, 
                'disable_voltage':0b0000, 
                'quick_stop':0b0100, 
                'disable_oparation':0b1110, 
                'enable_opration':0b1110, 
                'fault_reset':0b0000 #its a dont care 0bxxxx TODO do we need it here?
                }

# state machine status TODO

# return bytearray of controlword. size=2 bytes 
def Controlword(stm_command, mode=0): #TODO do we need extra parameters for halt,reset..
    return stm_command.to_bytes(2, byteorder='big')

def createPDOFrame(function_code, node_id, controlword, data=0):
    #do not except binary as function code
    #identifier = function_code.to_bytes(11, byteorder='big') + node_id.to_bytes(11, byteorder='little')
    identifier = np.binary_repr(function_code + node_id , width=11)
    controlword_bytes = controlword.to_bytes(2, byteorder='big')
    return Frame(identifier,controlword_bytes)  

print(createPDOFrame(BaseIdentifiers.TPDO1, 1, 7))
print(Controlword(STM_COMMANDS['shotdown']))

# import sys
# sys.path.append("C:/temp/Canlib_SDK_v5.9/Samples/Python")
# from canlib import canlib, Frame
# from canlib.canlib import ChannelData
# import time



# channel = 0
# ch = canlib.openChannel(channel)

# ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
# ch.setBusParams(canlib.canBITRATE_1M)
# ch.busOn()
# #frame = Frame(0,bytearray(b'\x01\x00'))
# #frame = Frame(0,[1,3,3])
# #ch.write(frame)


# # CAN state -> operetional id=0,cs=1,nod_id=1
# ch.write_raw(0,[1,1])

# # PDO1: controlword -> shotdown (to ready to switch on)
# ch.write_raw(512+1,[6,0])

# pp = [136,19,0,0] # set position 5000

# for i in range(9):
#     controlword = [127,0] # move immidiatly and relative
#     ch.write_raw(768+1,controlword + pp)
#     ch.write_raw(512+1,[111,0])
#     time.sleep(2)
    
    


