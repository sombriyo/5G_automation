import shutil
import os
import sys
sys.path.insert(0, r'S:/LTTS/Python stuff/robot_framework/Variables')
import config_a

class Handover:
    def __init__(self):
        pass

    def TC_handover(self):
        #step2
        path1 = config_a.h1
        path2 = config_a.h2
        shutil.move(path1, path2)
        print("Measurment_control: Source gNB -> UE")

        # step3
        path3 = config_a.h3
        path4 = config_a.h4
        path5 = config_a.h5
        if path3:
            shutil.move(path4, path5)
            print("Measurement_report: UE -> gNB")
        else:
            print("Measurment_control messge is not found")

        #step4
        path6 = config_a.h6
        path7 = config_a.h7
        shutil.move(path6, path7)
        print('gNBConfiguration_Transfer: Source gNB -> AMF')

        #step5
        path8 = config_a.h8
        path9 = config_a.h9
        path10 = config_a.h10
        if path8:
            shutil.move(path9, path10)
            print("AMFConfiguration_Transfer: AMF -> target gNB")
        else:
            print("AMFConfiguration_Transfer: File transfer failed")

        #step6
        path11 = config_a.h11
        path12 = config_a.h12
        path13 = config_a.h13
        if path11:
            shutil.move(path12, path13)
            print("gNBConfiguration_Transfer: target gNB -> AMF")
        else:
            print("gNBConfiguration_Transfer: File transfer failed")

        #step7
        path14 =config_a.h14
        path15 = config_a.h15
        path16 = config_a.h16
        if path14:
            shutil.move(path15, path16)
            print("AMFConfiguration_Transfer: AMF -> Source gNB")
        else:
            print("AMFConfiguration_Transfer: File transfer failed")

        #step8
        path17 = config_a.h17
        path18 = config_a.h18
        path19 = config_a.h19
        if path17:
            shutil.move(path18, path19)
            print("Xn_setup_request: Source gNB -> Target gNB")
        else:
            print("Xn_setup_request: File transfer failed")

        #step9
        path20 =config_a.h20
        path21 = config_a.h21
        path22 = config_a.h22
        if path20:
            shutil.move(path21, path22)
            print("Xn_setup_Response: Target gNB -> Source gNB")
        else:
            print("Xn_setup_Response: File transfer failed")
        #step10
        print('Xn interface is established between source and target gNB')

        #step11
        path23 = config_a.h23
        path24 = config_a.h24
        path25 =config_a.h25
        if path23:
            shutil.move(path24, path25)
            print("Handover_Request: Source gNB -> Target gNB")
        else:
            print("Handover_Request: File transfer failed")

        #step12
        path26 = config_a.h26
        path27 = config_a.h27
        path28 = config_a.h28
        if path26:
            shutil.move(path27, path28)
            print("Handover_Request_Ack: Target gNB -> Source gNB")
        else:
            print("Handover_Request_Ack: File transfer failed")

        #step13
        path29 = config_a.h29
        path30 = config_a.h30
        path31 = config_a.h31
        if path29:
            shutil.move(path30, path31)
            print("RRC_configuration: Source gNB -> UE")
        else:
            print("RRC_configuration: File transfer failed")
            







