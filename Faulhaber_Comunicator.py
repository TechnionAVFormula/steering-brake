import Maneger as maneger
import Kvaser_Comunicator as kvaser
import Faulhaber_Parser as parser

#wake up
def wakeup(id):
    #use id 0 to wake the whole system 
    if(maneger.CURRENT_COMPUTER == maneger.KVASER):
        # CAN state -> operetional id=0,cs=1,nod_id=1
        kvaser.send(parser.operasional(id))
        # PDO1: controlword -> shotdown (to ready to switch on)
        kvaser.send(parser.shutdown(id))
    #if(maneger.CURRENT_COMPUTER == maneger.NVIDIA)
    return
#send position
    #call parser to set postion 
    #check wake up
def setpoint(id,setpoint,relative,command = parser.commands.set_position, imidiate = True):
    if(maneger.CURRENT_COMPUTER == maneger.KVASER):
        kvaser.send(parser.position_setpoint(id,setpoint,relative,command,imidiate))
        kvaser.send(parser.enable(id))
    return