*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Test Cases ***

Opening_bro
    Open browser    https://google.com/     chrome
    maximize browser window
    sleep    5
    close browser







*** Keywords ***
