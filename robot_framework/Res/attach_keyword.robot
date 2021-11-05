*** Keywords ***

#Initial Attach------------------
Moving
    mov_ue2gnb
    mov_gnb2ue

Validating
    validate_gnb
    validate_ue

#paging----------------------------

Move
    paging_req

Action
    ue_action

Validation
    gnb_validation

#RNAU_update-----------------------------
Move_rna_update
    ran_ue2gnb

Network_validation
    validating_network

#Registration Procedure
RACH_validation
    validate_RACH

Registration
    initial_reg


#locking the folder-------------------------------------
Securing
    locking_folder
    unlocking_folder



