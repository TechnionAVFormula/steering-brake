import Kvaser_Comunicator as kvaser
import Faulhaber_Comunicator as faulhaber

#motor controller types
FAULHABER = 1
TENSSY = 0
#device Ids
STEARING_ID = 1
EBS_ID = 2
BRAKE_ID = 3
DASHBOARD_ID = 4
MOTEC_ID = 5
#motor controller per system
components = {
    'Stearing':[FAULHABER,STEARING_ID],
    'EBS':[FAULHABER,EBS_ID],
    'Brake':[FAULHABER,BRAKE_ID],
    'Dashboard':[TENSSY,DASHBOARD_ID],
    'MoTec':[TENSSY,MOTEC_ID]
}
#types Can comunicators
KVASER = 0  
NVIDIA = 1
#current used comunicator
CURRENT_COMPUTER = KVASER
#checklist
did_init = False
did_wakeup = False
#funcitons
def initilization():
    if(CURRENT_COMPUTER == KVASER):
        kvaser.Init()
    else:
        #Nvidia_Comunicator.init
        return
    did_init = True

def new_Setpoint(identity,setpoint,relative = False):
    if(did_init == False):
        initilization()
        did_init = True
    if(components[identity][0] == FAULHABER):
        if(did_wakeup == False):
            faulhaber.wakeup(components[identity][1])
            did_wakeup = True
        if(components[identity][1] == STEARING_ID): #if its in need of velocity or tourq controll change here!!
            faulhaber.setpoint(components[identity][1],setpoint,relative)
#tenssy stuff in here
#if i recive from stearing use faulhaber if i recive from otehr thing use tensy
#pass on request to correct motorcontroller
#call kvaer or nvidia 
#call init and make sure that init has happend before sending stuff