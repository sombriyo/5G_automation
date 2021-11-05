import shutil
import os
import sys
sys.path.insert(0, r'S:/LTTS/Python stuff/robot_framework/Variables')
import config_a
import webbrowser


class attach_function:

    #ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass

    def mov_ue2gnb(self):
        try:
            src = config_a.src_path1
            des = config_a.des_path1
            shutil.move(src, des)
            print('Move UE -> gNB')
        except shutil.Error:
            print('gNB: File already exist')

    def mov_gnb2ue(self):
        try:
            src = config_a.src_path2
            des = config_a.des_path2
            shutil.move(src, des)
            print('Move gNB -> UE')
        except shutil.Error:
            print('UE: File already exist')

    def validate_gnb(self):
        path = config_a.val1_path
        if not path:
            return 'gNB: No such file exits'
        req_file = open(path, 'r')
        readfile = req_file.read()
        if config_a.msg1 in readfile and config_a.msg3 in readfile:
            print('Validation for gnb is Successful')
        else:
            print('Validation is Unsuccessful')
        req_file.close()

    def validate_ue(self):
        path = config_a.val2_path
        if not path:
            return 'UE: No such file exits'
        req_file = open(path, 'r')
        readfile = req_file.read()
        if config_a.msg2 in readfile and config_a.msg4 in readfile:
            print('Validation for UE is Successful')
        else:
            print('Validation is Unsuccessful')
        req_file.close()

    #paging----------------------------------------------------------------------------
        
    def paging_req(self):
        src = config_a.src_path
        des = config_a.des_path
        if os.path.isfile(src):
            shutil.move(src, des)
            print('Paging request has being sent to UE ')
            print('UE wake up from idle state')

        else:
            print('Paging Request is already sent to UE')

    def ue_action(self):
        path = config_a.ue_path
        if path:
            webbrowser.open(config_a.action)
            file = open(path, 'w')
            st = "Action is preformed successfully"
            file.write(st)
            file.close()
        else:
            print('Paging Request has not being received')
    
    def gnb_validation(self):
        path = config_a.ue_path
        file = open(path, 'r')
        readfile = file.read()
        st = config_a.val_message
        if st in readfile:
            print('UE validation is successful')
        else:
            print('UE does not perform the task')
        file.close()


    # RNAU------------------------------------------------------------------

    def ran_ue2gnb(self):
        source = config_a.source_path1
        desti = config_a.desti_path1
        if os.path.isfile(source):
            shutil.move(source, desti)
            print("rna_update has been sent to network")
        else:
            print('rna_update is already has been sent to network')

    def validating_network(self):
        path = config_a.val_path1
        openfile = open(path, 'r')
        readfile = openfile.read()
        message = config_a.val_mess
        if message in readfile:
            print('Validation is successful')
        else:
            print('rna_update has not been received')
        openfile.close()


    #Registration procedure ----------------------------------------------

    def validate_RACH(self):
        #step1
        path1 = config_a.valrach1
        path2 = config_a.valrach2
        if path1 and path2:
            print('RACH_validation is successful')
        else:
            print("RACH_validation is not validate")




    def initial_reg(self):
        #step2
        path1 = config_a.p1
        path2 = config_a.des_path1
        shutil.move(path1, path2)
        print('RRC setup complete message from UE -> gNb')

        #step 3
        path3 = config_a.p3
        path4 = config_a.p4
        shutil.move(path3, path4)
        print('Registration Request from gNb -> New AMF')

        #step4
        path5 = config_a.p5
        path6 = config_a.p6
        shutil.move(path5, path6)
        print("Namf_Communication_UEContextTransfer_request: New AMF -> Old AMF")

        #step5
        path7 = config_a.p7
        path8 = config_a.p8
        path9 = config_a.p9
        if path7:
            shutil.move(path8, path9)
            print('Namf_Communication_UEContextTransfer_response: Old AMF -> New AMF')
        else:
            print("Namf_Communication_UEContextTransfer_request file not found")

        #step 6
        path10 = config_a.p10
        path11 = config_a.des_path2
        shutil.move(path10, path11)
        print("Identity Request: New AMF -> UE")

        #step 7
        path12 = config_a.p12
        path13 =config_a.p13
        path14= config_a.p14
        if path12:
            shutil.move(path13, path14)
            print('Identity Response: UE -> New AMF')
        else:
            print("Identity Request file not found")

        #step 8
        print('AMF selects AUSF for authentication')

        #step 9
        path15 = config_a.p15
        path16 = config_a.p16
        shutil.move(path15, path16)
        print("Nausf_UEAuthenticate_authenticate Request: New AMF -> AUSF")

        #step 10
        path17 = config_a.p17
        path18 = config_a.p18
        shutil.move(path17, path18)
        print("Nudm_UEAuthenticate_Get Request: AUSF -> UDM")

        #step11
        path19 = config_a.p19
        path20 = config_a.p20
        path21 = config_a.p21
        if path19:
            shutil.move(path20, path21)
            print("Nudm_UEAuthenticate_Get Response: UDM -> AUSF")
        else:
            print("Nudm_UEAuthenticate_Get Request file not found")

        #step12
        path22 = config_a.p22
        path23 = config_a.p23
        shutil.move(path22, path23)
        print("Nausf_UEAuthenticate_authenticate Response: AUSF -> New AMF")

        #step13
        path24 = config_a.p24
        path25 = config_a.p25
        shutil.move(path24, path25)
        print("Authentication Request: New AMF -> UE")

        path26 = config_a.p26
        path27 = config_a.p27
        shutil.move(path26, path27)
        print("Authentication Response: UE -> New AMF")

        #step14
        path28 = config_a.p28
        path29 = config_a.p29
        shutil.move(path28, path29)
        print("NAS Security Mode Command: New MAF -> UE")

        path30 = config_a.p30
        path31 = config_a.p31
        shutil.move(path30, path31)
        print("NAS Security Mode Complete: UE -> New AMF")

        #step15
        path32 = config_a.p32
        path33 = config_a.p33
        shutil.move(path32, path33)
        print("N5g-eir_EquipmentIdentityCheck_Request: New AMF -> 5G_EIR")

        path34 = config_a.p34
        path35 = config_a.p35
        path36 = config_a.p36
        if path34:
            shutil.move(path35, path36)
            print("N5g-eir_EquipmentIdentityCheck Response: 5G_EIR -> New AMF")
        else:
            print("N5g-eir_EquipmentIdentityCheck Request file not found ")

        #step16
        path37 = config_a.p37
        path38 = config_a.p38
        shutil.move(path37, path38)
        print("Nudm_UEContextManagement_Registration_Request: New AMF -> UDM")

        path39 = config_a.p39
        path40 = config_a.p40
        path41 = config_a.p41
        if path39:
            shutil.move(path40, path41)
            print("Nudm_UEContextManagement_Registration_Response: UDM -> New AMF")
        else:
            print("Request file not found")

        #step17
        path42 = config_a.p42
        path43 = config_a.p43
        shutil.move(path42, path43)
        print("Nudm_SubscriberDataManagement_Get_Request: New AMF -> UDM")

        path44 = config_a.p44
        path45 = config_a.p45
        path46 = config_a.p46
        if path44:
            shutil.move(path45, path46)
            print("Nudm_SubscriberDataManagement_Get_Response: UDM -> New AMF")
        else:
            print("Request file not Found")

        #step18
        path47 = config_a.p47
        path48 = config_a.p48
        shutil.move(path47, path48)
        print("Nudm_UEContextManagement_Deregistration_Notify: UDM -> Old AMF")

        #step19
        path49 = config_a.p49
        path50 = config_a.p50
        shutil.move(path49, path50)
        print("Npcf_AMPolicyControl_Create_Request: New AMF -> PCF")

        path51 = config_a.p51
        path52 = config_a.p52
        path53 = config_a.p53
        if path51:
            shutil.move(path52, path53)
            print("Npcf_AMPolicyControl_Create_Response: PCF -> New AMF")
        else:
            print('Request file not found')

        #step20
        path54 = config_a.p54
        path55 = config_a.p55
        shutil.move(path54, path55)
        print("Nsmf_PDUSession_UpdateSMContext_Request: New AMF -> SMF")

        #step21
        path56 = config_a.p56
        path57 = config_a.p57
        path58 = config_a.p58
        if path56:
            shutil.move(path57, path58)
            print("Nsmf_PDUSession_UpdateSMContext_Response: SMF -> New AMF")
        else:
            print("File not found")

        #step22
        path59 = config_a.p59
        path60 = config_a.p60
        shutil.move(path59, path60)
        print("Registration Accept: New AMF -> UE")
        path61 = config_a.p61
        path62 =config_a.p62
        path63 = config_a.p63
        if path61:
            shutil.move(path62, path63)
            print("Registration Complete: UE -> New AMF")
        else:
            print("Registration Failure")




    # locking and unlocking the folder---------------------------------------
    def locking_folder(self):
        pas1 = "password"
        pas2 = config_a.lockunlock_pass
        if pas1 == pas2:
            os.chdir(config_a.lockunlock_path)
            if os.path.exists("Attach1"):
                os.rename("Attach1", "Attach1.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Attach1.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Attach1 folder has been successfully locked")
        else:
            print("wrong password! Try again later")


    def unlocking_folder(self):
        pas1 = "password"
        pas2 = config_a.lockunlock_pass
        if pas1 == pas2:
            os.chdir(config_a.lockunlock_path)
            if not os.path.exists("Attach1"):
                os.popen('attrib -h -s -r Attach1')
                os.rename("Attach1.{645ff040-5081-101b-9f08-00aa002f954e}", "Attach1")
                print("Attach1 Folder has been Successfully Unlocked")
                # break
            else:
                print("Attach1 folder is not LOCKED")
        else:
            print("wrong password! Try again later")









