@ECHO OFF
:: This batch file will upload files to Github automatically
TITLE GitPush

:: Section 1 - comment

ECHO ..............................

ECHO === 1.  git add * ===
git add *

ECHO ..............................

ECHO === 2.  git commit -am "-" ===
git commit -am "-"

ECHO ..............................

ECHO === 3.  git push ===
git push

ECHO  bye...

ECHO ..............................

exit /B
