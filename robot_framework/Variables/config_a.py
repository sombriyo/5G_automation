#----------------Initial Attach--------------------------------------------
# Moving from UE -> gNB
src_path1 = 'S:/LTTS/Python stuff/5g_stuff/Attach1/UE/Request.txt'
des_path1 = 'S:/LTTS/Python stuff/5g_stuff/Attach1/gNB'

# Moving from gNB -> UE
src_path2 = 'S:/LTTS/Python stuff/5g_stuff/Attach1/gNB/Response.txt'
des_path2 = 'S:/LTTS/Python stuff/5g_stuff/Attach1/UE'

# for Validation Paths
#gNB
val1_path  = 'S:/LTTS/Python stuff/5g_stuff/Attach1/gNB/Request.txt'
#UE
val2_path =  'S:/LTTS/Python stuff/5g_stuff/Attach1/UE/Response.txt'

# attach messages
msg1 = 'Random Access Preamble Transmission - (Msg1)'
msg2 = 'Random Access Response Report - (Msg2)'
msg3 = 'UE Identification Message Report - (Msg3)'
msg4 = 'Contention Resolution Message Report - (Msg4)'

#Securing the folder
lockunlock_pass = "password"
lockunlock_path = "S:/LTTS/Python stuff/5g_stuff"

#-----------------------paging-----------------------------------------------
#moving file from gnb to ue

src_path = "S:/LTTS/Python stuff/5g_stuff/Attach1/Paging/gNB/Paging_request.txt"
des_path = "S:/LTTS/Python stuff/5g_stuff/Attach1/Paging/UE"

#UE action path

ue_path = "S:/LTTS/Python stuff/5g_stuff/Attach1//Paging/UE/Paging_request.txt"
action = "https://google.com"

#validation message
val_message = "Action is preformed successfully"

# ----------------------RNAU_update---------------------------------------
#moving  rna_update file
source_path1 = "S:/LTTS/Python stuff/5g_stuff/Attach1/UE/rna_update.txt"
desti_path1 = "S:/LTTS/Python stuff/5g_stuff/Attach1/gNB"

#validation path
val_path1 = "S:/LTTS/Python stuff/5g_stuff/Attach1/gNB/rna_update.txt"
val_mess = "Resume the RRC connection"

#-------------------------registration procedure-------------------------------
valrach1 = "S:/LTTS/Python stuff/5g_stuff/Attach1/gNB/Request.txt"
valrach2 = "S:/LTTS/Python stuff/5g_stuff/Attach1/UE/Response.txt"
p1 = "S:/LTTS/Python stuff/5g_stuff/Attach1/UE/rrc_setup_complete.txt"
p3 = "S:/LTTS/Python stuff/5g_stuff/Attach1/gNB/rrc_setup_complete.txt"
p4 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
p5 =  "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF/Namf_Communication_UEContextTransfer_request.txt"
p6 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/old_AMF"
p7 =  "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/old_AMF/Namf_Communication_UEContextTransfer_request.txt"
p8 ="S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/old_AMF/Namf_Communication_UEContextTransfer_response.txt"
p9 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
p10 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF/Identity_request.txt"
p12 = "S:/LTTS/Python stuff/5g_stuff/Attach1/UE/Identity_request.txt"
p13 = "S:/LTTS/Python stuff/5g_stuff/Attach1/UE/Identity_response.txt"
p14 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
p15 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF/Nausf_UEAuthenticate_authenticate_Request.txt"
p16 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/AUSF"
p17 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/AUSF/Nudm_UEAuthenticate_Get_Request.txt"
p18 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/UDM"
p19 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/UDM/Nudm_UEAuthenticate_Get_Request.txt"
p20 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/UDM/Nudm_UEAuthenticate_Get_Response.txt"
p21 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/AUSF"
p22 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/AUSF/Nausf_UEAuthenticate_authenticate_Response.txt"
p23 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
p24 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF/Authentication_Request.txt"
p25 = "S:/LTTS/Python stuff/5g_stuff/Attach1/UE"
p26 = "S:/LTTS/Python stuff/5g_stuff/Attach1/UE/Authentication_Response.txt"
p27 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
p28 =  "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF/NAS_Security_Mode_Command.txt"
p29 = "S:/LTTS/Python stuff/5g_stuff/Attach1/UE"
p30 = "S:/LTTS/Python stuff/5g_stuff/Attach1/UE/NAS_Security_Mode_Complete.txt"
p31 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
p32 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF/N5g-eir_EquipmentIdentityCheck_Request.txt"
p33 = "S:/LTTS/Python stuff/5g_stuff/Attach1/5G_EIR"
p34 = "S:/LTTS/Python stuff/5g_stuff/Attach1/5G_EIR/N5g-eir_EquipmentIdentityCheck_Request.txt"
p35 = "S:/LTTS/Python stuff/5g_stuff/Attach1/5G_EIR/N5g-eir_EquipmentIdentityCheck_Response.txt"
p36 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
p37 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF/Nudm_UEContextManagement_Registration_Request.txt"
p38 ="S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/UDM"
p39 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/UDM/Nudm_UEContextManagement_Registration_Request.txt"
p40 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/UDM/Nudm_UEContextManagement_Registration_Response.txt"
p41 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
p42 ="S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF/Nudm_SubscriberDataManagement_Get_Request.txt"
p43 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/UDM"
p44 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/UDM/Nudm_SubscriberDataManagement_Get_Request.txt"
p45 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/UDM/Nudm_SubscriberDataManagement_Get_Response.txt"
p46 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
p47 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/UDM/Nudm_UEContextManagement_Deregistration_Notify.txt"
p48 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/old_AMF"
p49 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF/Npcf_AMPolicyControl_Create_Request.txt"
p50 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/PCF"
p51 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/PCF/Npcf_AMPolicyControl_Create_Request.txt"
p52 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/PCF/Npcf_AMPolicyControl_Create_Response.txt"
p53 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
p54 ="S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF/Nsmf_PDUSession_UpdateSMContext_Request.txt"
p55 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/SMF"
p56 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/SMF/Nsmf_PDUSession_UpdateSMContext_Request.txt"
p57 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/SMF/Nsmf_PDUSession_UpdateSMContext_Response.txt"
p58 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
p59 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF/Registration_Accept.txt"
p60 = "S:/LTTS/Python stuff/5g_stuff/Attach1/UE"
p61 = "S:/LTTS/Python stuff/5g_stuff/Attach1/UE/Registration_Accept.txt"
p62 =  "S:/LTTS/Python stuff/5g_stuff/Attach1/UE/Registration_Complete.txt"
p63 = "S:/LTTS/Python stuff/5g_stuff/Attach1/control_plane/new_AMF"
#---------------------------------------Handover_1.2-----------------------------------------------------
h1 ="S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source/Measurment_control.txt"
h2 = "S:/LTTS/Python stuff/5g_stuff/Handover/UE"
h3 = "S:/LTTS/Python stuff/5g_stuff/Handover/UE/Measurment_control.txt"
h4 = "S:/LTTS/Python stuff/5g_stuff/Handover/UE/Measurement_report.txt"
h5 =  "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source"
h6 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source/gNBConfiguration_Transfer_1.txt"
h7 = "S:/LTTS/Python stuff/5g_stuff/Handover/AMF"
h8 = "S:/LTTS/Python stuff/5g_stuff/Handover/AMF/gNBConfiguration_Transfer_1.txt"
h9 = "S:/LTTS/Python stuff/5g_stuff/Handover/AMF/AMFConfiguration_Transfer_1.txt"
h10 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/target"
h11 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/target/AMFConfiguration_Transfer_1.txt"
h12 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/target/gNBConfiguration_Transfer_2.txt"
h13 = "S:/LTTS/Python stuff/5g_stuff/Handover/AMF"
h14 =  "S:/LTTS/Python stuff/5g_stuff/Handover/AMF/gNBConfiguration_Transfer_2.txt"
h15 = "S:/LTTS/Python stuff/5g_stuff/Handover/AMF/AMFConfiguration_Transfer_2.txt"
h16 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source"
h17 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source/AMFConfiguration_Transfer_2.txt"
h18 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source/Xn_setup_request.txt"
h19 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/target"
h20 =  "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/target/Xn_setup_request.txt"
h21 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/target/Xn_setup_Response.txt"
h22 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source"
h23 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source/Xn_setup_Response.txt"
h24 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source/Handover_Request.txt"
h25 =  "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/target"
h26  = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/target/Handover_Request.txt"
h27 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/target/Handover_Request_Ack.txt"
h28 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source"
h29 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source/Handover_Request_Ack.txt"
h30 = "S:/LTTS/Python stuff/5g_stuff/Handover/gNB/source/RRC_configuration.txt"
h31 = "S:/LTTS/Python stuff/5g_stuff/Handover/UE"




