
import sys
import time

sys.path.append('unitree_legged_sdk/lib/python/arm64')
import robot_interface as sdk

## comm.h

HIGHLEVEL = 0xee
LOWLEVEL  = 0xff

rate = 500 # 500hz
dt = 1.0 / rate # time between commands

def main():
    udp = sdk.UDP(HIGHLEVEL, 8080, "192.168.123.220", 8082)

    cmd = sdk.HighCmd()
    state = sdk.HighState()
    udp.InitCmdData(cmd)

    cmd.mode = 0
    cmd.gaitType = 0
    cmd.speedLevel = 0
    cmd.footRaiseHeight = 0
    cmd.bodyHeight = 0
    cmd.euler = [0, 0, 0]
    cmd.velocity = [0, 0]
    cmd.yawSpeed = 0.0
    cmd.reserve = 0
#3    for i in range(2000):       udp.Recv()
 #       udp.GetRecv(state)
  #      print(state.bms.current)
   #     udp.SetSend(cmd)
    #    udp.Send()
     #
#   time.sleep(dt)
    for i in range(int(4/dt)):
        cmd.mode = 6 # stand
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(2/dt)):
        cmd.mode = 5 # stand
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)
 
#    print("1")
#    for i in range(int(2/dt)):
#        cmd.mode = 0 # stand
#        udp.SetSend(cmd)
#        udp.Send()
#        time.sleep(dt)

#    print("6")
#    for i in range(int(4/dt)):
#        cmd.mode = 6 # stand
#        udp.SetSend(cmd)
#        udp.Send()
#        time.sleep(dt)

    #for i in range(int(2/dt)):
    #    cmd.mode = 1 # Active stand
    #    cmd.euler = [0.0, 0.3, 0.0] # Down

    #    udp.SetSend(cmd)
    #    udp.Send()
    #    time.sleep(dt)

    #for i in range(int(2/dt)):
    #    cmd.mode = 1 # Active stand
    #    cmd.euler = [0.0, -0.3, 0.0] # Up
    #    udp.SetSend(cmd)
    #    udp.Send()
    #    time.sleep(dt)

    #for i in range(int(2/dt)):
    #    cmd.mode = 2 # cmd vel
    #    cmd.yawSpeed = 0.2
    #    udp.SetSend(cmd)
    #    udp.Send()
    #    time.sleep(dt)

    #for i in range(int(2/dt)):
    #    cmd.mode = 2 # cmd vel
    #    cmd.yawSpeed = -0.2
    #    udp.SetSend(cmd)
    #    udp.Send()
    #    time.sleep(dt)

    #for i in range(int(2/dt)):
   #    cmd.mode = 2 # cmd vel
    #    cmd.velocity = [0.3, 0, 0]
    #    udp.SetSend(cmd)
    #    udp.Send()
    #    time.sleep(dt)

    #for i in range(int(2/dt)):
    #    cmd.mode = 2 # cmd vel
    #    cmd.velocity = [-0.3, 0, 0]
    #    udp.SetSend(cmd)
    #    udp.Send()
    #    time.sleep(dt)

    #for i in range(int(2/dt)):
    #    cmd.mode = 2 # cmd vel
    #    cmd.bodyHeight = -0.16 # sneak
    #    cmd.velocity = [0.3, 0, 0]
    #    udp.SetSend(cmd)
    #    udp.Send()
    #    time.sleep(dt)

    #for i in range(int(2/dt)):
    #    cmd.mode = 2 # cmd vel
    #    cmd.velocity = [-0.3, 0, 0]
    #    udp.SetSend(cmd)
    #    udp.Send()
    #    time.sleep(dt)

    #for i in range(int(2/dt)):
    #    cmd.mode = 2 # cmd vel
    #    cmd.gaitType = 3 # stair mode
    #    cmd.velocity = [0.3, 0, 0]
    #    udp.SetSend(cmd)
    #    udp.Send()
    #    time.sleep(dt)

    #for i in range(int(2/dt)):
    #    cmd.mode = 2 # cmd vel
    #    cmd.gaitType = 3 # stair mode
    #    cmd.velocity = [-0.3, 0, 0]
    #    udp.SetSend(cmd)
    #    udp.Send()
    #    time.sleep(dt)

    #for i in range(int(1/dt)):
    #    cmd.mode = 1 # Active stand

    #    udp.SetSend(cmd)
    #    udp.Send()
    #    time.sleep(dt)

 #   print("5")
 #   for i in range(int(2/dt)):
 #       cmd.mode = 5 # lay
 #       udp.SetSend(cmd)
 #       udp.Send()
 #       time.sleep(dt)

main()
