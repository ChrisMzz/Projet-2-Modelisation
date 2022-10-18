@echo on
setlocal EnableExtensions EnableDelayedExpansion
for /D /r %%G in ("ggb*") do (
    cd %%G
    for %%i in ("!%%G") do ren %%~ni.zip %%~ni.ggt
    cd ..
)
pause
