from IoTtweet import *
import time
import os

version = getversion()
print(version)

userid = 'iottweet/user/id'
key = 'iottweet/key'

f = os.popen("sensors | grep Core")
lines = tuple(f)

tw_msg = "Number of Core: " + str(len(lines)) + " cores"
#print tw

max_temp = 60

slot = [0,0,0,0]

while(True):
  tw = tw_msg

  for i in range(0, len(lines)):
    print("core", i, lines[i].split('+')[1].split('.')[0])
    slot[i] = lines[i].split('+')[1].split('.')[0]

  slot_int = map(int, slot)
  temp_avg = sum(slot_int) / float(len(slot_int))
  print temp_avg

  if(temp_avg >= max_temp):
    twpb = 'CPU temp (' + str(temp_avg)  + 'c) is overhead!!!'
  else:
    twpb = 'CPU temp (' + str(temp_avg)  + 'c) is normal'

  #Send data to IoTtweet dashboard.
  res = WriteDashboard(userid, key, slot[0], slot[1], slot[2], slot[3], tw, twpb)

  #Print response JSON from IoTtweet
  print(res)
  time.sleep(3)
