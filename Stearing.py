import Maneger as maneger
import Faulhaber_Comunicator as faulhaber
from Maneger import components
import Faulhaber_Parser as parser

def set_New_Setpoint(setpoint,relative = False):
    maneger.send('Stearing',parser.position_setpoint(components['Stearing'][1],setpoint,relative))
    maneger.send('Stearing',parser.enable(components['Stearing'][1]))