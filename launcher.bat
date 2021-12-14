@echo off&setlocal
for %%i in ("%~dp0.") do set "folder=%%~fi"
cd /d %folder%
curl https://raw.githubusercontent.com/Cars0419/LUG-INFO/main/ngrok_add.txt > %folder%\temp
title Lego Universe Gaming (US 1)
%folder%\Patcher.py %folder%