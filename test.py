# import sys
# sys.path.append("C:/temp/Canlib_SDK_v5.9/Samples/Python")

# from canlib import kvrlib

# kl = kvrlib.kvrlib()
# print ("kvrlib version: %s" % kl.getVersion())

# serialNo = 16
# print ("Connecting to device with serial number %s" % serialNo)
# addressList = kvrlib.kvrDiscovery.getDefaultAddresses(kvrlib.kvrAddressTypeFlag_BROADCAST)
# print ("Found %d addresses." % addressList.count)
# #print addressList                                       
# discovery = kl.discoveryOpen()
# discovery.setAddresses(addressList)

# delay_ms = 100
# timeout_ms = 1000
# discovery.setScanTime(delay_ms, timeout_ms)
# print ("Scanning devices...\n")
# deviceInfos = discovery.getResults()
# #print "Scanning result:\n%s" % deviceInfos                
# for deviceInfo in deviceInfos:
#     if deviceInfo.ser_no == serialNo:
#         deviceInfo.connect()
#         print ('Connecting to the following device:')
#         print ('---------------------------------------------')
#         print (deviceInfo)
#         discovery.storeDevices(deviceInfos)
#         break;
# discovery.close()
# kl.unload()
class commands:
    statusword   = 384
    controlword  = 512
    get_position = 640
    set_position = 768
    get_velosity = 896
    set_velosity = 1024
    get_torque   = 1152
    set_torque   = 1280
word = commands.set_position + 8
word = word.to_bytes(4, byteorder='little', signed=True)
print(word)
print(word[:1])