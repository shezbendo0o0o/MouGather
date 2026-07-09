::ORIGINAL CREATOR: Luca Garofalo (Lucksi)
::AUTHOR: Luca Garofalo (Lucksi)
::Copyright (C) 2021-2023 Lucksi <shizbendo@gmail.com>
::License: GNU General Public License v3.0

@ECHO OFF

START /B pip3 install -r requirements.txt  2>NUL >NUL
echo INSTALLING REQUIREMENTS DO NOT CLOSE THIS WINDOW MANUALLY...
cd ../
echo path= %CD% >>MouGather/Configuration/Configuration.ini
echo Desktop>MouGather/Display/Display.txt