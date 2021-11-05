*** Settings ***
Library     os
Resource    ${EXEC_DIR}/Res/attach_keyword.robot
Variables   ${EXEC_DIR}/Variables/config_a.py
Library     ${EXEC_DIR}/LIb/attach_function.py

*** Test Cases ***

TC_attach_1.2_some
    Moving
    Validating

TC_attach_1.2: Reg
    RACH_validation
    Registration


TC_attach_1.27: Paging
    Move
    Action
    Validation


TC_attach_1.20: RNAU_update
    Move_rna_update
    Network_validation





