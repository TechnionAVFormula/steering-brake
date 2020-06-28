import Manager as manager 
import Faulhaber_Comunicator as faulhaber
from Manager import components
import Faulhaber_Parser as parser

def set_New_Setpoint(setpoint, relative = False):
    manager.send('Stearing',parser.position_setpoint(components['Stearing'][1],setpoint,relative))
    manager.send('Stearing',parser.enableNextSetPoint(components['Stearing'][1], relative)) # 