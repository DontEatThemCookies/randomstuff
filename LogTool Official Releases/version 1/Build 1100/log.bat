SET path=C:\Users\%Username%\Desktop\log.txt
SETX path "C:\Users\%Username%\Desktop\log.txt"
SET CustomMessage=This is an entry log.
SETX CustomMessage "This is an entry log."
cls
@echo off
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
color 0a
goto MENU
:MENU
cls
color 0a
cls
echo LogTool v1
echo Build developed July 1 2021
echo Running as Administrator is recommended.
echo ------------------------------------------------------------------------------------------
echo 1 - Log
echo 2 - Options
echo 3 - Info
set input=
set /p input= Input choice and press Enter: 
if %input%==1 goto REG if NOT goto MENU
if %input%==2 goto OPT if NOT goto MENU
if %input%==3 goto CRE if NOT goto MENU
exit
:REG
cls
echo Are you sure you want to register a log? If yes,
pause 
echo Entry logged!>>%path%
echo "%CustomMessage%">>%path%
echo %mytime%, %mydate%>>%path%
echo ⠀>>%path%
echo Log successfully performed.
pause >nul
goto MENU 
:OPT
cls
echo 1 - Change save path of log file
echo 2 - Add custom message to entry
set input=
set /p input= Input choice and press Enter: 
if %input%==1 goto OPT1 if NOT goto MENU
if %input%==2 goto OPT2 if NOT goto MENU
exit
:OPT1
cls
echo The CURRENT directory is %path%
echo Would you like to change it?
set input=
set /p input= Y/N: 
if %input%==Y goto OPT1A if NOT goto MENU
if %input%==N goto MENU if NOT exit
goto MENU
:OPT1A
cls
@echo off
set /p path= "Specify path: (e.g. D:\log.txt) "
setx path "%path%"
echo The path has been set to %path% 
pause
goto MENU
:OPT2
cls
echo The CURRENT custom message set is: %CustomMessage%
echo Would you like to change it?
set /p input= Y/N: 
if %input%==Y goto OPT2A if NOT goto MENU
if %input%==N goto MENU if NOT exit
goto MENU
:OPT2A
cls
@echo off
set /p CustomMessage= "Specify custom message: (e.g. Hello world!): "
setx CustomMessage "%CustomMessage%"
echo The custom message has been set to: %CustomMessage% 
pause
goto MENU
pause
exit
:CRE
cls
color 0a
echo David, 1st of July 2021
echo v1, Build 1100, 7/1/2021
echo ------------------------------------------------------------------------------------------
echo 1 - Bugs                          2 - Help
echo 3 - Changelog                     4 - Exit to Menu
echo 5 - Exit program
set input=
set /p input= Input choice and press Enter: 
if %input%==1 goto BUGS if NOT exit
if %input%==2 goto HELP if NOT exit
if %input%==3 goto CHG if NOT exit
if %input%==4 goto MENU if NOT exit
if %input%==5 exit
exit
:BUGS
cls
@echo off
color 0c
echo No known bugs at this time. Please e-mail veryrisible@gmail.com if you wish to report one.
pause
goto CRE
:HELP
cls
@echo off
echo Guide to using LogTool is COMING SOON!
echo Check back in later versions!
pause
goto CRE
:CHG
cls
@echo off
echo Build 1100
echo -------------------------------------
echo Fixed a color bug
echo Added feature allowing custom text to an entry
echo -------------------------------------
echo Working on a fix for setx and not saving configurations!
echo Coming Soon: Help Guide
pause
goto CRE