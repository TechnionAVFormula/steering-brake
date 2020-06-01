
' read anlog 1 input . 

' SETOBJ $2313.$01   'gain (scaling factor) - numerator/denominator. numerator: 0-15 bits, denominator: 16-31 bits
' SETOBJ $2313.$02   'offset
' SETOBJ $2313.$03   'filter time in 100us (1 order filter)
' SETOBJ $2313.$05   'resolution of the encoder
' SETOBJ $2313.$06   'lower limit for the input value
' SETOBJ $2313.$07   'upper limit for the input value


' SETOBJ $2313.$04   'scaled value
' SETOBJ $2314.$07   'Analuge 1 value after filtering (before scaling?)





'--------------------------------------------
'Author:
'Date:
'--------------------------------------------
'Description:
'--------------------------------------------
#INCLUDE "MotionParameters.bi"   'right mouse click opens the file
#INCLUDE "MotionMacros.bi"   'right mouse click opens the file 
#INCLUDE "MotionFunctions.bi" 'premade library with several move functions
                    
#DEFINE POSITION_MODE 1'position mode                   
#DEFINE SPEED_MODE 3'speed mode                          
'SETOBJ $605B.$00 = 0 'this is shutdown forsome reason its requierd TO get TO anable state, 0 is defualt value 0 anable movment  
SETOBJ $6040.$00 = $0006 'this is shutdown? 
SETOBJ $6040.$00 = $0007 'this is switch on?
SETOBJ $6040.$00 = $001F 'set te controll word TO enable mode TO deable switch TO quick stop with ___ AND then set 605C.00 TO 1
SETOBJ $6060.$00 = POSITION_MODE 'set position mode 
'can use statuse word at 6041 00 TO see sate

SETOBJ $607A.$00 = $0000  'see 116 drive functions FOR more help
''FOR loop
FOR i = 1 TO 10 
   MoveRel(2000,0)
   'do something
NEXT i
 'move TO zero second one changes the controll word
'now use CAN TO send setpoints TO $607A.$00 'need TO change controll word when changing setpoint                                                               
'repete FOR difrent modes or DO in funciton.     
END     
'----------------------------------------------------------------------
'Static Functions
