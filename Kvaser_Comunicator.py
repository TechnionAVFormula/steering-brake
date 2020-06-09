from canlib import canlib, Frame
ch = None
emptyFrame = Frame(0,0)
def Init(channel=0):
    ch = canlib.openChannel(channel)
    ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
    ch.setBusParams(canlib.canBITRATE_1M)
    ch.busOn()

def send(messege):
    frame = Frame(messege[0],messege[1])
    ch.write(frame)
#send messeges using canlib librareys