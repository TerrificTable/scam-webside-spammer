@echo off
title Installing Requirements
python -m pip install colorama
python -m pip install requests

cls
echo 1 = exe
echo 2 = py
set /p action= %cd% $ 
if '%action%'=='1' goto exe
if '%action%'=='2' goto py

:exe
@echo off & cls
start scam-spammer.v.1.1.exe
exit

:py
@echo off & cls
start scam-spammer.v.1.1.py
exit
